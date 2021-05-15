from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to = 'images')

    is_criminal = models.NullBooleanField(
        null=True,
    )
    
    def __str__(self):
          return f'Photo {self.pk}'

    