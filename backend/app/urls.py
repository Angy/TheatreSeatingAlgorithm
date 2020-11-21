from django.conf.urls import url

from app.views import HallView, UserView, RowView, UserGroupView, GetRowView, \
    SeatsView

urlpatterns = [
    url('^halls/$', HallView.as_view()),
    url('^rows/$', RowView.as_view(), name='rows'),
    url('^rows/(?P<pk>[0-9A-Z-a-z-]+)/$', GetRowView.as_view()),
    url('^seats/$', SeatsView.as_view(), name='seats'),
    url('^sections/$', SectionView.as_view()))
    url('^users/$', UserView.as_view()),
    url('^users/(?P<pk>[0-9A-Z-a-z-]+)/$', UserGroupView.as_view()),
]
