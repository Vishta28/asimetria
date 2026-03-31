from django.shortcuts import render
from .models import Category


def welcome_page(request):
	categories = Category.objects.all()
	context = {
		'categories': categories
	}
	return render(request, 'main/welcome_page.html', context)

def gallery_page(request, slug):
	category = Category.objects.get(slug=slug)
	images = category.image_set.all()
	context = {
		'category': category,
		'images': images
	}
	return render(request, 'main/gallery.html', {'context': context})

def gallery_image_detail(request, image_url, description):
	print(image_url)
	context = {
		'image_url': image_url,
		'description': description
	}
	return render(request, 'main/gallery_image_detail.html', {'context': context})