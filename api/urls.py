from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import GetNews, ListNews

app_name = 'api'

urlpatterns = [
    path('collect_news/', GetNews.as_view()),
    path('news', ListNews.as_view())
]
