from django.urls import path  # path is a function
from . import views

# define a list of different addreses and their associated views
urlpatterns = [
    # first argument is address/fuction and second argument is views to be associated with this address.you can access using views.hello_world.
    path('function', views.hello_world),
    # addres is class, second argument associated class which we can acces using viewsHelloEthopia. when passing classes we need to add additional function or method which is .as_views.
    path('class', views.HelloEthopia.as_view()),
    # the address is reservation, we link it to views.home
    path('reservation', views.home),
]
# mapping urls at app level.
