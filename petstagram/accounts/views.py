from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from petstagram.accounts.forms import AppUserCreationForm, AppUserLoginForm
from petstagram.accounts.models import Profile

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

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class AppUserLogoutView(LogoutView):
    pass


def show_profile_details(request, pk: int):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request, pk: int):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk: int):
    return render(request, template_name='accounts/profile-delete-page.html')
