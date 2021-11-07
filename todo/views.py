from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerilizer
from .models import Todo
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerilizer
    queryset = Todo.objects.all()
