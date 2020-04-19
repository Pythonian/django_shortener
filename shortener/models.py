from django.db import models
import random
import string


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Shortener(models.Model):
    url = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=15, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = code_generator()
        super().save(*args, **kwargs)
