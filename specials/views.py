
from django.shortcuts import render
from .models import DailySpecial

def index(request):
    # Get the most recent daily special
    latest_special = DailySpecial.objects.order_by('-date').first()
    
    context = {
        'latest_special': latest_special,
    }
    
    return render(request, 'specials/index.html', context)
