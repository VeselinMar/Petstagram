from django.contrib import admin

from petstagram.common.models import Comment, Like


# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
