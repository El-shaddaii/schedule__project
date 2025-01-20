from .views import EventList, EventDetail, schedule_view, about_view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet
from . import views


router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('events/', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('api/events/<int:id>/', views.delete_event, name='delete-event'),
    path('', schedule_view, name='schedule-view'),
    path('about/', about_view, name='about'),
    # Other paths...
]
