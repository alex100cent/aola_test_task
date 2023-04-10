from random import choices

from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from .paginations import FeedPaginator
from .serializers import AdSerializer, PostSerializer
from ..models import Ad, User, Achievement, Note

POST_KEYWORDS = {
    'achievement': Achievement,
    'note': Note,
    'ad': Ad
}


class FeedAPIView(GenericAPIView):
    pagination_class = FeedPaginator
    filter_backends = (SearchFilter,)
    search_fields = ('title',)

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        ad = choices(Ad.objects.all(), k=1)
        ad = AdSerializer(ad, many=True).data

        filter_param = self.request.query_params.get('filter')
        if filter_param:
            if filter_param in POST_KEYWORDS:
                user_posts = user.posts.instance_of(POST_KEYWORDS[filter_param])
            else:
                user_posts = []
        else:
            user_posts = user.posts.all()

        user_posts = self.filter_queryset(user_posts)

        user_posts = PostSerializer(user_posts, many=True).data
        user_posts = self.paginate_queryset(user_posts)
        result = ad + user_posts

        return Response(result)
