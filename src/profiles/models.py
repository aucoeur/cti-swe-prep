from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, \
                                   help_text='User this Profile belongs to.')
    firstName = models.CharField(verbose_name="First Name", max_length=255, blank=True, help_text='First name')
    lastName = models.CharField(verbose_name="Last Name", max_length=255, blank=True, help_text='Last name')
    birthday = models.DateField(help_text='Birthday')

    def __str__(self):
        return self.firstName
