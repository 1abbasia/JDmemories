from django.db import models
from PIL import Image
# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField()

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     exif_data = img._getexif()
    #     if exif_data:
    #         for tag, value in exif_data.items():
    #             if tag == 36867:
    #                 self.uploaded_at = value
    #                 self.save()