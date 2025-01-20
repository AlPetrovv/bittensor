from django.contrib.admin import ModelAdmin
from django.contrib.admin import register

from ..models import Answer
from ..models import Chat
from ..models import Question


@register(Chat)
class ChatAdmin(ModelAdmin):
    list_display = ("id", "name", "user", "subnet")
    search_fields = ("name", "user__email")


@register(Question)
class QuestionAdmin(ModelAdmin):
    pass


@register(Answer)
class AnswerAdmin(ModelAdmin):
    pass
