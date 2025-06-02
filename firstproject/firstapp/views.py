from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForms
# Create your views here.

def hello(request):
    return HttpResponse("Hello, world!")

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world from class-based view!")
    
    def post(self, request):
        return HttpResponse("Hello, world from class-based view with POST!")
    
def Home(request):
    form = ReservationForms()

    if request.method == 'POST':
        form = ReservationForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation saved successfully!")
        else:
            return HttpResponse("Form is not valid. Please try again.")

    return render(request, 'index.html', {'form': form})
