from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255, blank=True)
    book = models.FileField(upload_to='fb2_files/', blank=False)
    uploadedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name