"""myquiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from quiz import views
from django.conf import settings
from django.conf.urls.static import static
from quiz.models import BookmarkFeed
from django.contrib.auth.decorators import login_required

app_name = 'ajax'
urlpatterns = [
    url(r'^$',views.front_page,name='front'),
    url(r'^feeds$',views.index_view,name='index'),
    url(r'^feed/(?P<pk>\d+)/bookmark/$',
        login_required(views.BookmarkView.as_view(model=BookmarkFeed)),
        name='feed_bookmark'),
    url(r'^follow-me$',views.follow_me,name='follow'),
    url(r'^feed-form$',views.FeedFormView.as_view(),name='feed'),
    url(r'^profile-form$',views.ProfileFormView.as_view(),name='profile'),
    url(r'^profile/(?P<pk>\d+)$',views.ProfileDetail.as_view(),name='profile-detail'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('django_registration.backends.activation.urls')),
    url(r'^admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)