from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .models import PublishedManager
from .views import (
    news_list,
    home_View,
    ContactPageView,
    single_View,
    page_404_View,
    HomeView,
    UzbekistonPageView,
    JahonPageView,
    SportPageView,
    IqtisodPageView,
    NewsUptadeView,
    NewsCreateView,
    NewsDeleteView,
)

urlpatterns = [
    path('news/', news_list, name='all_news_list'),
    # path('<int:id>/',news_detail,name='news_detail'),
    path('news/<path:title>/', single_View, name='single'),
    # path('news/<path:title>/edit', NewsUptadeView.as_view(), name='news_edit'),
    # path('news/<path:title>/edit/', NewsUptadeView.as_view(), name='news_edit'),
    path('news/<slug:title>/edit/', NewsUptadeView.as_view(), name='news_edit'),


    path('news/<path:title>/delete', NewsDeleteView.as_view(), name='news_delete'),
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('404/', page_404_View, name="page_404"),
    path('uzbekiston/', UzbekistonPageView.as_view(), name='uzbekiston'),
    path('jahon/', JahonPageView.as_view(), name='jahon'),
    path('iqtisod', IqtisodPageView.as_view(), name='iqtisod'),
    path('sport', SportPageView.as_view(), name='sport'),
]
