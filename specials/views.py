
from django.shortcuts import render
from .models import DailySpecial

def index(request):
    # Get the most recent daily special
    latest_special = DailySpecial.objects.order_by('-date').first()
    
    # Create a list of specials with their respective sides
    specials_list = []
    if latest_special:
        for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
            special_field = f"{letter}_special"
            side_field = f"{letter}_special_w_side"
            
            special_obj = getattr(latest_special, special_field)
            if special_obj:
                specials_list.append({
                    'letter': letter.upper(),
                    'special': special_obj,
                    'side': getattr(latest_special, side_field),
                })
    
    context = {
        'latest_special': latest_special,
        'specials_list': specials_list,
    }
    
    return render(request, 'specials/index.html', context)
