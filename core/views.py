from django.shortcuts import redirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models import Task
from core.serializers import TaskSerializer


def home(request):
    return redirect('/tarefa')


class TaskList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


tasks = TaskList.as_view()


class TaskReadCreateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


task_read_update_delete = TaskReadCreateDelete.as_view()
