from django.shortcuts import render

# Create your views here.


def display_home(request):
    return render(request, template_name='common/home-page.html')
