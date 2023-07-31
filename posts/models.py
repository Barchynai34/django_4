from django.db import models

CATEGORY_CHOICES = (
    ("SP", "Спорт"),
    ("POL", "Политика"),
    ("ECO", "Экономика"),
    ("SOC", "Общество"),
)


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3, default="SOC", verbose_name="Категория")
    status = models.BooleanField(default=True, verbose_name="Статус публикации")
    cover = models.ImageField(default="image.jpg", upload_to="uploads/posts", blank=True, verbose_name="Обложка")

    def __str__(self):
        return f"{self.title} - {self.created}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"