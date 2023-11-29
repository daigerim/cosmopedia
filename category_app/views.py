from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import *

class CategoriesApiView(APIView):
    permission_classes = [permissions.AllowAny, ]
    def get(self, request):
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     name = request.data.get('name')
    #     category = Category(name=name)
    #     category.save()
    #     return Response({'message': 'Category created!'}, status=status.HTTP_201_CREATED)

    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailApiView(APIView):
    permission_classes = [permissions.AllowAny, ]
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        data = CategorySerializer(category).data
        return Response(data, status=status.HTTP_200_OK)

    # def patch(self, request, pk):
    #     category = Category.objects.get(id=pk)
    #     new_name = request.data['name']
    #     category.name = new_name
    #     category.save()
    #     data = CategorySerializer(category).data
    #     return Response(data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = Category.objects.get(id=pk)
        category.delete()
        return Response({'message': 'Object is deleted'}, status=status.HTTP_200_OK)








