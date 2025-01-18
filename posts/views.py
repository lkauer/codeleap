import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer

BASE_URL = "https://dev.codeleap.co.uk/careers/"

class PostListView(APIView):
    def get(self, request):
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({"error": "Unable to fetch posts"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            response = requests.post(BASE_URL, data=serializer.validated_data)
            if response.status_code == 201:
                return Response(response.json(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    def patch(self, request, id):
        serializer = PostSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            response = requests.patch(f"{BASE_URL}{id}/", data=serializer.validated_data)
            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        response = requests.delete(f"{BASE_URL}{id}/")
        if response.status_code == 204:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Unable to delete post"}, status=status.HTTP_400_BAD_REQUEST)
