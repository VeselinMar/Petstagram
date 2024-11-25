from django.shortcuts import render, redirect, resolve_url

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo

from pyperclip import copy


# Create your views here.


def display_home(request):
    all_photos = Photo.objects.all
    comment_form = CommentForm()
    search_form = SearchForm()

    if search_form.is_valid():
        all_photos = all_photos.filter(
            tagged_pets__name__icontains=search_form.cleaned_data['pet_name']
        )

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form
    }
    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, photo_id: int):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


def copy_link_to_clipboard(request, photo_id: int):
    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def add_comment(request, photo_id: int):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
