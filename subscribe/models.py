from django.db import models


class Subscribe(models.Model):
    """ A model to save users email """

    email = models.EmailField(max_length=254, unique=True, blank=False)

    class Meta:
        verbose_name_plural = "subscribe"

    def __str__(self):
        return self.email
