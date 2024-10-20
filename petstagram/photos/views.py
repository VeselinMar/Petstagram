from django.shortcuts import render, get_object_or_404

from petstagram.photos.models import Photo


# Create your views here.


def add_photo(request):
    return render(request, template_name='photos/photo-add-page.html')


def photo_details(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)


def photo_edit(request):
    return render(request, template_name='photos/photo-edit-page.html')
