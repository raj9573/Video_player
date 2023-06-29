from django.db import models

# Create your models here.
class video(models.Model):
    Video_description=models.CharField(max_length=100)
    Video_file=models.FileField(upload_to="documents")
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.Video_description
        