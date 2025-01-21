from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from petstagram.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from petstagram.accounts.models import Profile
from petstagram.photos.models import Photo

# Create your views here.

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class AppUserLoginView(LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'


class AppUserLogoutView(LogoutView):
    pass


class AppUserDetailView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        photos_with_likes = self.object.photo_set.annotate(likes_count=Count('like'))

        context['total_likes_count'] = sum(p.likes_count for p in photos_with_likes)
        context['total_photos_count'] = self.object.photo_set.count()
        context['total_pets_count'] = self.object.pet_set.count()
        context['user_photos'] = (
            Photo.objects
            .filter(user_id=self.object.pk)
            .order_by('-date_of_publication')
        )

        return context


class ProfileEditView(UpdateView, LoginRequiredMixin):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk
            }
        )


class AppUserDeleteView(DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())
