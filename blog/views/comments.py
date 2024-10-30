from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from blog.models import CommentsModel
from blog.serializers import CommentsSerializer


@api_view(['GET', 'POST'])
def comment_list_create(request):
    if request.method == 'GET':
        comment = CommentsModel.objects.all()
        serializer = CommentsSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CommentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def comment_detail(request, pk):
    comment = get_object_or_404(CommentsModel, pk=pk)
    if request.method == 'GET':
        serializer = CommentsSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CommentsSerializer(instance=comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PATCH':
        serializer = CommentsSerializer(instance=comment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def blog_user_detail(request, pk):
    if request.method == 'GET':
        blog = CommentsModel.filter(user_id=pk)
        if not blog.exists():
            return Response({"detail": "No blogs found for this user."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentsSerializer(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)