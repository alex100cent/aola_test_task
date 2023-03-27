from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .paginations import FeedPaginator
from .serializers import AchievementSerializer, NoteSerializer, AdSerializer
from ..constants import FilterKeyWords
from ..models import Achievement, Note, Ad


class FeedAPIView(GenericAPIView):
    pagination_class = FeedPaginator
    filter_backends = (SearchFilter,)
    search_fields = ('title',)

    def get(self, request, user_id):
        ad = Ad.objects.all()
        result_dict = {
            'ad': AdSerializer(ad, many=True).data
        }

        filter_param = self.request.query_params.get('filter')
        if not filter_param or (filter_param == FilterKeyWords.NOTE):
            notes = Note.objects.filter(user__pk=user_id)
            notes = self.filter_queryset(notes)
            result_dict['notes'] = NoteSerializer(notes, many=True).data
        if not filter_param or (filter_param == FilterKeyWords.ACHIEVEMENT):
            achievements = Achievement.objects.filter(usersachievements__user__pk=user_id)
            achievements = self.filter_queryset(achievements)
            result_dict['achievements'] = AchievementSerializer(achievements, many=True).data

        result_data = result_dict.pop('ad')
        for key in result_dict:
            result_data += result_dict[key]

        result_data = self.paginate_queryset(result_data)

        return Response(result_data)
