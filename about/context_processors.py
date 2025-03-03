from django.urls import reverse

def urls_processor(request):
    return {
        'home_url': reverse('home'),
        'about_url': reverse('about'),
    }