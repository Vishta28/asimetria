from django.db import models
from django_extensions.db.fields import AutoSlugField
from pytils.translit import slugify
from django.utils.safestring import mark_safe

class Category(models.Model):
	title = models.CharField('Назва', max_length=55)
	description = models.TextField('Опис', max_length=400, blank=True)
	slug = AutoSlugField(max_length=50, populate_from='title', slugify_function=slugify, unique=True)
	main_photo = models.ImageField('Головне фото', upload_to='media')

	class Meta:
		verbose_name_plural = 'Категорії'

	def __str__(self):
		return self.title

class Image(models.Model):
	image = models.ImageField(upload_to='media/')
	description = models.TextField('Опис', max_length=400, blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def image_preview(self):
		if self.image:
			return mark_safe(f'<img src="{self.image.url}" width="150" style="object-fit: contain;" />')
		return "Немає фото"