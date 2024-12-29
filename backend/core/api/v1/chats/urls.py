from django.urls import include
from django.urls import path

from .routers import chat_router
from .routers import question_router

urlpatterns = [
    path("", include((chat_router.urls, "chats"), namespace="chat")),
    path("", include((question_router.urls, "chats"), namespace="question")),
]
