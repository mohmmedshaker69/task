from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import  ListView,   DetailView, TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from .models import PhoneNumber, ContactName
from .forms import ContactNameForm, PhoneNumberForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
  
       
        return context
    

class ContactCreateView(CreateView):
    model = ContactName
    form_class = ContactNameForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('contact_list')

class ContactListView(ListView):
    model = ContactName
    template_name = 'contact_list.html'
    context_object_name = 'contacts'



class ContactDetailView(DetailView):
    model = ContactName
    context_object_name = 'contact'
    template_name = 'contact_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact = self.get_object()

        phones = PhoneNumber.objects.filter(contact=contact)

        context['phones'] = phones

        return context    


def phone_form_view(request, pk):
    contact = ContactName.objects.get(pk=pk) 

    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone = form.save(commit=False)
            phone.contact = contact
            phone.save()
            return redirect('contact_list')
    else:
        form = PhoneNumberForm()

    return render(request, 'phone_number_form.html', {
        'form': form,
        'contact': contact, 
        'title': 'New phone number'
    })

