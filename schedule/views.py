from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, generics
from .models import Event, Comment
from .serializers import EventSerializer
from .forms import CommentForm




class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def schedule_view(request):
    # Fetch events for rendering the schedule
    events = Event.objects.all()
    hours = range(24)  # Example working hours (0 to 23)

    # Handle adding comments
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule-view')  # Redirect to refresh the page after comment submission
    else:
        form = CommentForm()

    # Fetch all comments to display
    comments = Comment.objects.all()

    context = {
        'events': events,
        'hours': hours,
        'form': form,
        'comments': comments,
    }

    return render(request, 'schedule/schedule.html', context)

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def about_view(request):
    return render(request, 'me.html')




@csrf_exempt
@require_http_methods(["DELETE"])
def delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        event.delete()
        return JsonResponse({'message': 'Event deleted successfully'}, status=200)
    except Event.DoesNotExist:
        return JsonResponse({'message': 'Event not found'}, status=404)

