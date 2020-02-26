from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120)
    number = PhoneNumberField()
    email = models.EmailField(blank = True)
    image = models.FileField(null=True, blank = True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("contacts:detail",kwargs={"id": self.id})