from django.db import models
from organiser.models import Startup, Tag


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.CharField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)

    def __str__(self) -> str:
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"
