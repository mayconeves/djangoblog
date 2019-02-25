from django.urls import path
from . import views

urlpatterns = [
	# atribuindo uma view chamada post_list à URL raiz
	path('', views.post_list, name='post_list'),
]