from django.shortcuts import render
from .models import Category
from .models import Image
from django_user_agents.utils import get_user_agent


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
		'images': images,
		'category_slug': category.slug
	}
	return render(request, 'main/gallery.html', {'context': context})

def gallery_image_detail(request, id, slug):
	images = Image.objects.filter(category__slug=slug).order_by('id')
	current = Image.objects.get(id=id)

	image_list = list(images)
	current_index = image_list.index(current)
	user_agent = get_user_agent(request)
	if user_agent.is_mobile or user_agent.is_tablet:
		template = 'main/gallery_image_detail.html'
	else:
		template = 'main/gallery_image_detail_pc.html'

	return render(request, template, {
		'images': images,
		'current_index': current_index
	})