from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializer import TaskSerializer
from .models import Task

class TaskView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            try:
                data = Task.objects.get(pk=pk)
            except Task.DoesNotExist:
                raise NotFound({"message": "Task not found."})
            serializer = TaskSerializer(data)
        else:
            data = Task.objects.all()
            serializer = TaskSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Task created successfully"})
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk=None):
        if pk:
            data = Task.objects.get(pk=pk)
            serializer = TaskSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
    
    def patch(self, request, pk=None):
        if pk:
            data = Task.objects.get(pk=pk)
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
    
    def delete(self, request, pk=None):
        if pk:
            data = Task.objects.get(pk=pk)
            data.delete()
            return Response({"message":"Task deleted successfully"})
        return Response({"message":"No data to delete"}, status=400)

    
        