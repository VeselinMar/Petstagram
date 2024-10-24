from django.urls import path, include

from petstagram.pets import views
from petstagram.pets.views import AddPetView, PetDetailsView, EditPetView

urlpatterns = [
    path('', include([
        path('add/', AddPetView.as_view(), name='add-pet'),
        path('<str:username>/pet/<slug:pet_slug>/', include([
            path('', PetDetailsView.as_view(), name='pet-details'),
            path('edit/', EditPetView.as_view(), name='pet-edit'),
            path('delete/', views.pet_delete, name='pet-delete'),
        ]))
    ]))
]
