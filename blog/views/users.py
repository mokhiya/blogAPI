from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from blogs.models import AuthorModel
from blogs.serializers import AuthorSerializer


@api_view(['GET', 'POST'])
def author_list_create(request):
    if request.method == 'GET':
        books = AuthorModel.objects.all()
        serializer = AuthorSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def author_detail(request, pk):
    author = get_object_or_404(AuthorModel, pk=pk)
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = AuthorSerializer(instance=author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PATCH':
        serializer = AuthorSerializer(instance=author, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        author.delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)
