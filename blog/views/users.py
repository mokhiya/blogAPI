from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from blog.models import UserModel
from blog.serializers import UserSerializer


@api_view(['GET', 'POST'])
def user_list_create(request):
    if request.method == 'GET':
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def user_detail(request, pk):
    author = get_object_or_404(UserModel, pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = UserSerializer(instance=author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PATCH':
        serializer = UserSerializer(instance=author, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        author.delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)
