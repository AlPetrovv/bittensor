from rest_framework.routers import SimpleRouter

from .handlers import ChatsViewSet
from .handlers import QuestionsViewSet

chat_router = SimpleRouter()
chat_router.register("chats", ChatsViewSet)

question_router = SimpleRouter()
question_router.register("question", QuestionsViewSet)
