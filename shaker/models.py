from django.db import models

# Create your models here.


class ContactName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class PhoneNumber(models.Model):
    number = models.CharField(max_length=255, null=True, blank=True)
    contact = models.ForeignKey(ContactName, on_delete=models.CASCADE)

    def __str__(self):
        return self.number