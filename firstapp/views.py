from django.shortcuts import render
from django.http import HttpResponse
from django.views import View  # import view class
from .forms import ReservationForm  # forms we created before
# Create your views here.


def hello_world(request):  # request send by user when using application.
    return HttpResponse("Hello world")  # user will get respose hello world


class HelloEthopia(View):  # will inherit from the view class
    def get(self, request):  # self,requeast as parameters.
        # when the user sends a get request to this view, it will return httpresponse.
        return HttpResponse("Hello Ethopia")


def home(request):  # function based view. we imported reservation form our forms.py file
    # in our view we create variable and its equal to our resrvation form class.
    form = ReservationForm()

    # check if user sends a post request which will be sent when user submits the form.
    if request.method == 'POST':
        # if it is a post request we pass in request.post to our reservation form. request.post contains details of what the user inputed inside the form.
        form = ReservationForm(request.POST)
        # when we have the user data, we check its vadility using the is_valid function and if it returns true we save it to our model.
        if form.is_valid():
            form.save()                       # save it in our model
            return HttpResponse("success")    # return "success"
    # here we used the render function which takes in request as first argument, HTML file to be rendered as second argument and dictionary where the key is the variable we want to use in our template and the value is the actual variable we have in our view file and we gave both the name form.
    return render(request, 'index.html', {'form': form})
