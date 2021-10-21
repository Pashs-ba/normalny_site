from django.db import models


class News(models.Model):
    en_title = models.CharField(max_length=1024)
    ru_title = models.CharField(max_length=1024, null=True)
    ru_text = models.TextField()
    en_text = models.TextField()
    image = models.FileField(null=True)

    def __str__(self):
        return self.ru_title