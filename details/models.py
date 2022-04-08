from django.db import models
# Create your models here.


class Contact(models.Model):
    """
    Mapped with Contact from SFDC
    """
    Users = models.CharField(max_length=255, blank=True, null=True)
    Accounts = models.CharField(max_length=255, blank=False, null=False)
    Contacts = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.Users