from django.db import models


class Contact(models.Model):
    """ A Model for admin to get user questions """

    full_name = models.CharField(max_length=50, blank=False)
    email_address = models.EmailField(max_length=254, blank=False)
    subject = models.CharField(max_length=50, blank=False)
    message = models.TextField()

    def __str__(self):
        return self.full_name
