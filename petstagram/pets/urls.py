from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('', include([
        path('add/', views.add_pet, name='add-pet'),
        path('<str:username>/pet/<slug:pet_slug>/', include([
            path('', views.pet_details, name='pet-details'),
            path('edit/', views.pet_edit, name='pet-edit'),
            path('delete/', views.pet_delete, name='pet-delete'),
        ]))
    ]))
]
