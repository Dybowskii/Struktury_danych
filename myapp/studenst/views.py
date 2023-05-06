from django.shortcuts import render
from .models import Student
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import StudentSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, ValidationError


class StudentList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(owner=user)
    def put (self,request,*args,**kwargs):
        students = self.get_object()
        if students.owner != request.user:
            raise PermissionDenied('You do not have permission to update this book.')
        add = int(request.data.get('add',0))
        if add < 0:
            raise ValidationError('Price cannot be increased beyond 150 zł.')
        students.price =students.price + add
        students.save()
        serializer = self.get_serializer(students)
        return Response(serializer.data)
        
            
    
class UserBookListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(owner=user)
    