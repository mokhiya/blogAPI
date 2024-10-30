from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from blog.models import BlogModel
from blog.serializers import BlogSerializer


@api_view(['GET', 'POST'])
def blog_list_create(request):
    if request.method == 'GET':
        books = BlogModel.objects.all()
        serializer = BlogSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def blog_detail(request, pk):
    author = get_object_or_404(BlogModel, pk=pk)
    if request.method == 'GET':
        serializer = BlogSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BlogSerializer(instance=author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PATCH':
        serializer = BlogSerializer(instance=author, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        author.delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def blog_user_detail(request, pk):
    if request.method == 'GET':
        blog = BlogModel.filter(user_id=pk)
        if not blog.exists():
            return Response({"detail": "No blogs found for this user."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)