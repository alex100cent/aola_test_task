from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from .paginations import FeedPaginator
from .serializers import AdSerializer, UsersPostsSerializer
from ..models import Ad, User


class FeedAPIView(GenericAPIView):
    pagination_class = FeedPaginator

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        ad = Ad.objects.all()[:1]
        posts = AdSerializer(ad, many=True).data

        user_posts = user.posts.all()

        filter_param = self.request.query_params.get('filter')
        if filter_param:
            user_posts = [p for p in user_posts if p.post_content_type.model == filter_param]

        search_param = self.request.query_params.get('search')
        if search_param:
            user_posts = [p for p in user_posts if p.post.title == search_param]

        # user_posts = [p.post for p in user_posts]
        user_posts = UsersPostsSerializer(user_posts, many=True).data
        posts = posts + user_posts
        posts = self.paginate_queryset(posts)

        return Response(posts)
