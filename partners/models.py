from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название раздела")
    description = models.TextField(blank=True, verbose_name="Описание раздела")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        ordering = ['name']

    def __str__(self):
        return self.name

class Card(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='cards', verbose_name="Раздел")
    title = models.CharField(max_length=255, verbose_name="Заголовок карточки")
    description = models.TextField(blank=True, verbose_name="Описание карточки")
    # JSONField для гибкого хранения дополнительных данных
    data = models.JSONField(blank=True, null=True, default=dict, verbose_name="Дополнительные данные")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
        ordering = ['title']
        unique_together = ('section', 'title') # Карточка с одним названием в одном разделе может быть только одна

    def __str__(self):
        return f"{self.title} ({self.section.name})"