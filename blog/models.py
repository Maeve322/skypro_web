from django.db import models


class BlogPost(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
    )
    content = models.CharField(
        max_length=1000,
        verbose_name="Содержимое",
        help_text="Введите текст",
    )
    preview = models.ImageField(
        upload_to="BlogPost/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )
    is_published = models.BooleanField(default=True)

    view_count = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите кол-во просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Блог-пост"
        verbose_name_plural = "Блог-посты"

    def __str__(self):
        return self.title
