from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


class PostPagination(PageNumberPagination):
    """
    Configuração para paginar os resultados.
    """
    page_size = 10  # Número de itens por página.
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostListView(ListCreateAPIView):
    """
    View para listar e criar posts com suporte à paginação.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def create(self, request, *args, **kwargs):
        """
        Personaliza a criação de posts.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    """
    View para obter, atualizar ou excluir um post específico.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        """
        Atualiza parcialmente um post. Não é permitido alterar id, username ou created_datetime.
        """
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        data = request.data.copy()

        # Impede a alteração de "id", "username" ou "created_datetime".
        for field in ['id', 'username', 'created_datetime']:
            if field in data:
                return Response({field: "Cannot update this field."}, status=status.HTTP_400_BAD_REQUEST)

        # Atualiza o post com os dados enviados, mas não altera os campos protegidos
        serializer = self.get_serializer(instance, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        Deleta um post específico.
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
