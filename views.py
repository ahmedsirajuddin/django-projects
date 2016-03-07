class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsCreateOrDeleteOrRetrieveOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    # Users should be able to like the post.
    @detail_route(methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        post.usersVoted.add(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Users should be able to unlike the post.
    @detail_route(methods=['post'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        post.usersVoted.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

class IsCreateOrDeleteOrRetrieveOnly(permissions.BasePermission):
    """
    Permission.
    Allow create, delete or retrieve only.
    """
    message = 'You do not have access to the action you are trying to perform.'

    def has_permission(self, request, view):
        return (
                view.action == 'create' or
                view.action == 'destroy' or
                view.action == 'retrieve'
        )
