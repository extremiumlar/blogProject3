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
    NewsDeleteView,
    NewsCreateView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', news_list, name='all_news_list'),
    # path('<int:id>/',news_detail,name='news_detail'),
    path('news/<str:title>/', single_View, name='single'),
    # path('news/<path:title>/edit', NewsUptadeView.as_view(), name='news_edit'),
    # path('news/<path:title>/edit/', NewsUptadeView.as_view(), name='news_edit'),
    # path('news/<title>/edit/', NewsUptadeView.as_view(), name='news_edit'),
# urls.py
    path('news/<str:title>/edit/', NewsUptadeView.as_view(), name='news_edit'),
    path('news/<str:title>/delete/', NewsDeleteView.as_view(), name='news_delete'),


    # path('news/create/', NewsCreateView.as_view(), name='news_create'), # new/create qilsa xatolik beryapti
    path('create', NewsCreateView.as_view(), name='news_create'), # exitcreate ni o'zi qolsa xatolik yo'q

    path('contact/', ContactPageView.as_view(), name='contact'),
    path('404/', page_404_View, name="page_404"),
    path('uzbekiston/', UzbekistonPageView.as_view(), name='uzbekiston'),
    path('jahon/', JahonPageView.as_view(), name='jahon'),
    path('iqtisod', IqtisodPageView.as_view(), name='iqtisod'),
    path('sport', SportPageView.as_view(), name='sport'),
]
