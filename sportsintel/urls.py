"""stan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic.base import TemplateView


from prediction.views import football_upload,vip,gol, home_view, home_wins,to_win,top_pick, home_loose, raw_predictions, away_wins, away_loose, over_goals, under_goals, now


urlpatterns = [
    path('all-predictions/', football_upload, name="football_upload"),
    path('predictions/', raw_predictions, name="raw_predictions"),
    path('goals/', over_goals, name="over_goals"),
    path('nogoals/', under_goals, name="under_goals"),
    path('home/', home_view, name="ho"),
    path('vip/', vip, name="vip"),
    path('gol/', gol, name="gol"),
    path('homewin/', home_wins, name="home_wins"),
    path('awaywin/', away_wins, name="away_wins"),
    path('homeloose/', home_loose, name="home_loose"),
    path('awayloose/', away_loose, name="away_loose"),
    path('to-win/', to_win, name="to_win"),
    path('top-pick/', top_pick, name="top_pick"),
    path('admin/', admin.site.urls),
    

    path('', now),
    
    

]   


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)