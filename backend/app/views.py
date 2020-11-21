from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from app.models import Hall, User, Row, Seat, Section
from app.serializers import HallSerializer, UserSerializer, RowSerializer, \
    SeatSerializer, SectionSerializer


class HallView(ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGroupView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        users_with_privilege = User.objects.filter(rank=self.kwargs["pk"])
        users_json = UserSerializer(instance=users_with_privilege, many=True).data

        return Response(data=users_json)


class RowView(ListCreateAPIView):
    queryset = Row.objects.all()
    serializer_class = RowSerializer


class GetRowView(RetrieveAPIView):
    queryset = Row.objects.all()
    serializer_class = RowSerializer


class SeatsView(ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class SectionView(ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

