from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Event

# create your views here:

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "blog/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.first()  # Adjust this to get the relevant event
        return context


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'blog/event_detail.html', {'event': event})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})