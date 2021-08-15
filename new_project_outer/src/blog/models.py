# from django.db import models
from django.db.models import (
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
)
from organiser.models import Startup, Tag

# from datetime import date


class Post(Model):
    title = CharField(max_length=63)
    slug = SlugField(max_length=63)
    text = TextField()
    pub_date = DateField()
    tags = ManyToManyField(Tag)
    startups = ManyToManyField(Startup)

    class Meta:
        get_latest_by = "pub_date"
        ordring = ["-pub_date", "title"]
        verbose_name = "blog post"

    def __str__(self) -> str:
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"
