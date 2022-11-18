from sqlite3 import IntegrityError
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Parking
from django.contrib import messages

# Create your views here.


def index(request):
    # return HttpResponse('this is home page')
    if (request.method == "POST"):
        state = request.POST.get('state')
        vehicle_no = request.POST.get('vehicle_no')
        vehicle_type = request.POST.get('vehicle_type')

        parking = Parking(state=state, vehicle_no=vehicle_no,
                          vehicle_type=vehicle_type, park_time=datetime.now().time(), park_date=datetime.today())

        try:
            parking.save()
            messages.success(request, ' Your slot has been booked...')
        except IntegrityError as e:
            messages.error(' Invalid Entry...')
        


    # all_vehicle = Parking.objects.all().count()
    two_wheel = Parking.objects.filter(vehicle_type="2 Wheeler").count()
    four_wheel = Parking.objects.filter(vehicle_type="4 Wheeler").count()

    context = {'total': (two_wheel+four_wheel), 'remain': (100-(two_wheel+four_wheel)),
               'two_wheel': 50-two_wheel, 'four_wheel': 50-four_wheel, 'booked_two': two_wheel, 'booked_four': four_wheel}
    return render(request, 'index.html', context)


def parking(request):
    all_vehicle = Parking.objects.all()
    exit_time = datetime.now().time()
    exit_date = datetime.today()
    context = {'vehicles': all_vehicle,
               'exit_time': exit_time, 'exit_date': exit_date}
    return render(request, 'parking.html', context)
