from django.db import models
from django.contrib.auth.models import User


class AIFramework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="aiframework", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    aiframework = models.ForeignKey(AIFramework, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    text_desc = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


# 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