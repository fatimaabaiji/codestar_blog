from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Event

# create your views here:

class PostList(generic.ListView):
     
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "blog/index.html"
    paginate_by = 6


def event_detail(request, event_id):
    
    queryset = Event.objects.all()
    event = get_object_or_404(event, event_id=event_id)

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "coder": "GitHub Copilot"
        }
    )