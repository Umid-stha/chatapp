from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.ChatSessionView.as_view()),
    path('chats/<uri>', views.ChatSessionView.as_view()),
    path('chats/<uri>/message', views.ChatSessionMessageView.as_view())
]