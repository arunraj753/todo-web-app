from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ToDoSerializer
from .models import ToDo
class ToDoViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]
    # def get_permissions(self):
    #     # Instantiates and returns the list of permissions that this view requires.
    #     if self.action == 'list':
    #         permission_classes = [AllowAny]
    #     else: 
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    def list(self, request):
        todo_queryset = ToDo.objects.filter(user = request.user)
        serializer = ToDoSerializer(todo_queryset, many=True)
        return Response(serializer.data, status=200)

    def create(self, request):

        serializer = ToDoSerializer(request.data)
        serializer.save(user = request.user)
        return Response(serializer.data)

        # new_todo = request.data.get('task', None)
        # if not new_todo:
        #     return Response({"task":['This filed is required']}, status=400)
        # if len(new_todo)>100:
        #     return Response({"task":['Only 100 characters allowed']}, status=400)
        # new_todo_obj = ToDo.objects.create(
        #     task = new_todo,
        #     user = request.user
        # )
        # return Response({'Server':'New todo created'}, status=201)

    def retrieve(self, request, pk=None):
        try:
            todo_obj    = ToDo.objects.get(pk=pk, user=request.user)
            serializer  = ToDoSerializer(todo_obj) 
            return Response(serializer.data, status=200)
        except:
            return Response({'Server':'Not found'}, status=404)

    def update(self, request, pk=None):
            return Response({'Server':'Method not accepted'}, status=404)

    def partial_update(self, request, pk=None):
        try:
            todo_obj    = ToDo.objects.get(pk=pk, user=request.user)
            
            return Response({'Server':'Task Deleted'}, status=200)
        except:
            return Response({'Server':'Not found'}, status=404)

    def destroy(self, request, pk=None):
        try:
            todo_obj    = ToDo.objects.get(pk=pk, user=request.user)
            todo_obj.delete()
            return Response({'Server':'Task Deleted'}, status=200)
        except:
            return Response({'Server':'Not found'}, status=404)

class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]