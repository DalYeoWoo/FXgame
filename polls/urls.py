from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('participate/', views.participate, name='participate'),
    path('<int:participant_id>/', views.game, name='game'),
    path('<int:participant_id>/submit', views.submit, name='submit'),
    path('<int:participant_id>/tip', views.tip, name='tip'),
    path('<int:participant_id>/tip/create', views.create, name='create'),
]