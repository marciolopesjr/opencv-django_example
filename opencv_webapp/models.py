from django.db import models

class ImageUploadModel(models.Model):
  description = models.CharField(max_length=255, blank=True)
  document = models.ImageField(upload_to='images/%Y/%m/%d')
  uploaded_at = models.DateTimeField(auto_now_add=True)