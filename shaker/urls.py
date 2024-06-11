from django.urls import path
from . import views
from .views import ContactDetailView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.HomeView.as_view(), name='home'),
    path('contact_list/', views.ContactListView.as_view(), name='contact_list'),
    path('contact_form/', views.ContactCreateView.as_view(), name='contact_form'),
    path('phone_number_form/<int:pk>/', views.phone_form_view, name='phone_number_form'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),

]