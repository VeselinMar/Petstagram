from django.urls import path, include

from petstagram.photos import views
from petstagram.photos.views import PhotoAddPage

urlpatterns = [
    path('', include([
        path('add/', PhotoAddPage.as_view(), name='add-photo'),
        path('<int:pk>/', include([
            path('', views.photo_details, name='photo-details'),
            path('edit/', views.photo_edit, name='photo-edit'),
            path('delete/', views.photo_delete, name='photo-delete')
        ]))
    ]))
]
