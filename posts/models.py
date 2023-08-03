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

    

class Comment(models.Model):
    name = models.CharField(max_length=16, verbose_name="Имя комьентатора")
    text = models.CharField(max_length=300, verbose_name="Текст коментария") 
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment", verbose_name="Запись")

    def __str__(self):
        return f"{self.name} - {self.post.title}"

class Meta:
    verbos_name = "Комментарий"
    verbos_name_plural = "Комментарии"