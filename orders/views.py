from django.shortcuts import render

def callback_page(request):
	return render(request, 'orders/callback.html')
