from django.urls import path
from . import views

urlpatterns = [
    path('ideas/', views.ideas_list_view, name='ideas_list'),
    path('ideas/<int:idea_id>/reply/', views.reply_view, name='reply_idea'),
]
