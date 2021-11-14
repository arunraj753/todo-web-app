from rest_framework import routers
from .viewsets import ToDoViewSet

router = routers.DefaultRouter()
router.register('todo', ToDoViewSet, basename='todo')


