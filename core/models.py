from django.db import models


class SiteConfiguration(models.Model):
    show_chat = models.BooleanField(default=False)

    def __str__(self):
        return f"Show chat: {self.show_chat}"