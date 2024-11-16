from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import Photo


# Create your models here.

UserModel = get_user_model()


class Comment(models.Model):
    comment_text = models.TextField(
        max_length=300,
    )
    publication_date_time = models.DateTimeField(
        auto_now_add=True,
    )
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-publication_date_time']


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
