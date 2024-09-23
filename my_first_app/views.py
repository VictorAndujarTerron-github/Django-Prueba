from django.shortcuts import render
from my_first_app.models import Car

# Create your views here.
def my_view(request):
    car_list = Car.objects.all()
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)