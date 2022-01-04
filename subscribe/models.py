from django.db import models


class Subscribe(models.Model):
    """ Model for the subscription form """
    email = models.EmailField(max_length=254, blank=false, unique=True)

    class Meta:
        verbose_name_plural = 'Subscribe'

    def __str__(self):
        return self.email
