from rest_framework.pagination import LimitOffsetPagination


class FeedPaginator(LimitOffsetPagination):
    default_limit = 2
