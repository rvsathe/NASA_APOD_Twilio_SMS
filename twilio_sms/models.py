from django.db import models

# Create your models here.
class SMS(models.Model):
    created_on = models.DateTimeField("Created on", auto_now_add=True)
    title = models.CharField("Title", max_length=255)
    image_url = models.URLField(
        "Image URL", max_length=255, help_text="The URL to the image file itself")
    description = models.TextField("Description")

    def __str__(self):
        return self.title


