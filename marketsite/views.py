from django.shortcuts import render
from django.utils import timezone
from .models import Orders


def index(request):
    if request.POST:
        ord = Orders(name=request.POST['name'], tel=request.POST['tel'], add_info=request.POST['add_info'],
                     count=request.POST['count'], delivery=request.POST['delivery'], size=request.POST['size'],
                     pub_date=timezone.now())
        ord.save()
        return render(request, 'marketsite/index.html')
    return render(request, 'marketsite/index.html')



# Create your views here.
