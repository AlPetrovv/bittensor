from django.db import models


class Chat(models.Model):
    name = models.CharField("Name", max_length=255)
    user = models.ForeignKey(
        "auth_users.AuthUser", on_delete=models.CASCADE, related_name="chats"
    )
    subnet = models.ForeignKey(
        "subnets.Subnet", on_delete=models.CASCADE, related_name="chats"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"

    def __str__(self):
        return f'Chat ""{self.name}"" with {self.user.email}'


class Question(models.Model):
    chat = models.ForeignKey(
        "chats.Chat", on_delete=models.CASCADE, related_name="questions"
    )
    user = models.ForeignKey(
        "auth_users.AuthUser", on_delete=models.CASCADE, related_name="questions"
    )
    text = models.TextField("Text")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return f"Question #{self.id} - {self.user.email}:{self.chat.name}"

    @property
    def role(self):
        return "user"


class Answer(models.Model):
    question = models.ForeignKey(
        "chats.Question", on_delete=models.CASCADE, null=True, related_name="answers"
    )
    text = models.TextField("Text")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return (
            f"Answer #{self.id} - {self.question.user.email}:{self.question.chat.name}"
        )

    @property
    def role(self):
        return "assistant"
