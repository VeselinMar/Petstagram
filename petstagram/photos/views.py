from django.shortcuts import render, get_object_or_404, redirect

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


# Create your views here.


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, template_name='photos/photo-add-page.html', context=context)


def photo_details(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,
        'comment_form': comment_form,
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)


def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)

    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, template_name='photos/photo-edit-page.html', context=context)


def photo_delete(request, pk):
    Photo.objects.get(pk=pk).delete()
    return redirect('home')
