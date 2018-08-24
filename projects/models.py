from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()

    def __str__(self):
        return self.title
