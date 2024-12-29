from apps.chats.models import Chat


def get_messages(chat: Chat) -> list[dict[str, str]]:
    messages = list()
    for question in chat.questions.order_by("created_at"):
        messages.append({"role": question.role, "content": question.text})
        for answer in question.answers.order_by("created_at"):
            messages.append({"role": answer.role, "content": f"{answer.text}"})
    return messages
