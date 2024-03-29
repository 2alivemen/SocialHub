from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signin', views.signin, name='signin'),
    path('logout', views.Logout, name='Logout'),
    path('delete', views.delete, name='delete'),
    path('chat/<str:room>', views.chat, name='chat'),
    path('pchat', views.pchat, name='pchat'),
    path('getMessages', views.getMessages, name='getMessages'),
    path('inbox', views.inbox, name='inbox'),
    path('forgotpass', views.forgotpass, name='forgotpass'),
    path('resetpass/<str:user>', views.resetpass, name='resetpass'),



]