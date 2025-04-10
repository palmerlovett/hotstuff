
from django.shortcuts import render
from .models import DailySpecial

def create_specials_objects():
  # Get the most recent daily special
  latest_special = DailySpecial.objects.order_by('-date').first()
  
  # Create a list of specials with their respective sides
  specials_list = []
  veggies_list = []
  desserts_list = []
  
  if latest_special:
    # Process specials
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
    
    # Process veggies
    for num in range(1, 13):  # veggies 1-12
      veggie_field = f"veggie_{num}"
      veggie_obj = getattr(latest_special, veggie_field)
      if veggie_obj:
          veggies_list.append(veggie_obj)
    
    # Process desserts
    temp_desserts = []
    for letter in ['w','x','y','z']:  # veggies 1-12
      dessert_field = f"{letter}_dessert"
      dessert_obj = getattr(latest_special, dessert_field)
  
      if dessert_obj:
        desserts_list.append({'letter': letter.upper(), 'dessert': dessert_obj})

    specials = {
      'latest_special': latest_special,
      'specials_list': specials_list,
      'veggies_list': veggies_list,
      'desserts_list': desserts_list,
    }

    return specials

  else:
    return f"Specials not found"


def index(request):
  context = create_specials_objects()    

  return render(request, 'specials/index.html', context)

def print(request):
  context = create_specials_objects()
  

  
  # Render the template normally
  return render(request, 'specials/print.html', context)