import logging
import random
from xmlrpc.client import TRANSPORT_ERROR

import apps.chats.services as chat_services
from apps.chats.models import Answer
from apps.chats.models import Chat
from bittensor.settings import CLIENT

logger = logging.getLogger("chats")


def make_answers(chat: Chat) -> list[Answer]:
    try:
        messages = chat_services.get_messages(chat)
        response = CLIENT.chat.completions.create(
            model=chat.subnet.openai_model,
            messages=messages,
        )

        answers = []

        for response_answer in response.choices:
            answer = Answer.objects.create(
                text=response_answer.message.content,
                question=chat.questions.first(),
            )
            answers.append(answer)
    except Exception as exc:
        logger.error(f"Error while making answers: {exc}")
        return []
    return answers


def make_fake_answers(chat: Chat) -> list[Answer]:
    answers = []
    for i in range(0, random.randint(1, 5)):
        answer = Answer.objects.create(
            text=f"Fake answer {i}",
            question=chat.questions.first(),
        )
        answers.append(answer)
    return answers
