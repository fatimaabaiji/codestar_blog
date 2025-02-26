from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")  # Simple homepage message

def hello_blog(request):
    return HttpResponse("Hello blog")  # Message for the /blog/ URL
