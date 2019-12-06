from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    image_main = models.URLField()
    url_demo = models.URLField()
    url_source_code = models.URLField()
    tools_used = models.TextField()
    challenges = models.TextField()
    result = models.TextField()

    def __str__(self):
        return self.title
