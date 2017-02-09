from django.conf.urls import url
from .views import gamelist,detail,logout_page
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    url(r'^home/(?P<name>.*)$', login_required(gamelist.as_view()),name='home_page'),
    url(r'detail/(?P<pk>.*)$', login_required(detail.as_view()),name='Deatail_page'),
    url(r'logout/$', logout_page,name='exit_page'),
    
    ]