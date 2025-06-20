from django.shortcuts import render
from rest_framework import viewsets , permissions
from .models import Project
from .serializers import *
from rest_framework.response import Response
# Create your views here.
# class ProjectView(viewsets.ModelViewSet):
#     permission_classes=[permissions.AllowAny]
#     queryset= Project.objects.all()
#     serializer_class = ProjectSerializers

#     def list(self, request):
#         queryset= self.queryset
#         serializer =self.serializer_class(queryset , many =True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status= 400)
        


# from rest_framework import status

# def retrieve(self, request, pk=None):
#     try:
#         project = self.queryset.get(pk=pk)
#     except Project.DoesNotExist:
#         return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     serializer = self.serializer_class(project)
#     return Response(serializer.data)


#     def update(self, request, pk=None):
#         project = self.queryset.get(pk = pk )
#         serializer =self.serializer_class(project , data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status= 400)
        
#     def destroy(self, request, pk=None):
#         project = self.queryset.get(pk = pk )
#         project.delete()
#         return Response(status= 204)

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializers

class ProjectView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers

    def retrieve(self, request, pk=None):
        try:
            project = self.get_object()
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            project = self.get_object()
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            project = self.get_object()
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
