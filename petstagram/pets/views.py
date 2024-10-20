from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

from petstagram.pets.models import Pet


# Create your views here.


def add_pet(request):
    return render(request, template_name='pets/pet-add-page.html')


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(request, template_name='pets/pet-details-page.html', context=context)


def pet_edit(request, username, pet_slug):
    return render(request, template_name='pets/pet-edit-page.html')


def pet_delete(request, username, pet_slug):
    return render(request, template_name='pets/pet-delete-page.html')
