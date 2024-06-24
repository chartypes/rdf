"""File to manage of the logic and functionalities of the posts app"""

from typing import Iterable, Any

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from posts.serializer import PostSerializer, Post


class PostListView(APIView):
    """View to manage get the post and create a new ones"""

    def get(self, _request: Request) -> Response:
        """Return all the posts"""
        posts: Iterable = Post.objects.all()
        serializer: PostSerializer = PostSerializer(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        """create a new post"""
        data: dict[str, Any] = request.data
        serializer: PostSerializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    def get(self, request: Request) -> Response:
        return Response()

    def put(self, request: Request) -> Response:
        return Response()

    def delete(self, request: Request) -> Response:
        return Response()