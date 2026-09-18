
from django.contrib import admin
from .models import Veggie, Special, Dessert, DailySpecial

from django import forms

@admin.register(Veggie)
class VeggieAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_sides', 'price')
    list_filter = ('number_of_sides',)
    search_fields = ('name',)

@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)

@admin.register(DailySpecial)
class DailySpecialAdmin(admin.ModelAdmin):
    list_display = ('date_formatted', 'date_day', 'a_special', 'b_special', 'c_special')
    list_filter = ('date',)
    date_hierarchy = 'date'
    search_fields = ('a_special__name', 'b_special__name', 'c_special__name')
    change_form_template = 'admin/specials/dailyspecial/change_form.html'
    
    fieldsets = (
        ('Date Information', {
            'fields': ('date',)
        }),
        ('Specials', {
            'fields': [
                ('a_special', 'a_special_w_side'),
                ('b_special', 'b_special_w_side'),
                ('c_special', 'c_special_w_side'),
                ('d_special', 'd_special_w_side'),
                ('e_special', 'e_special_w_side'),
                ('f_special', 'f_special_w_side')
            ],
            'classes': ('even-selects',)
        }),
        ('Veggies', {
            'fields': [
                'veggie_1',
                'veggie_2',
                'veggie_3',
                'veggie_4',
                'veggie_5',
                'veggie_6',
                'veggie_7',
                'veggie_8',
                'veggie_9',
                'veggie_10',
            ],
            'classes': ('columns-2', 'even-selects'),
        }),
        ('Extra Veggies', {
            'fields': [
                'veggie_11',
                'veggie_12',
            ],
            'classes': ('columns-2', 'even-selects'),
        }),
        ('Desserts', {
            'fields': ['z_dessert', 'y_dessert', 'x_dessert', 'w_dessert'],
            'classes': ('columns-2', 'even-selects',),
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:  # Only set defaults for new objects
            # Set default date to today
            from datetime import date
            form.base_fields['date'].initial = date.today()
            
            # Get the most recent daily special entry
            latest_special = DailySpecial.objects.order_by('-date').first()
            if latest_special:
                # Set defaults for specials
                for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
                    special_field = f"{letter}_special"
                    side_field = f"{letter}_special_w_side"
                    if hasattr(latest_special, special_field):
                        form.base_fields[special_field].initial = getattr(latest_special, special_field)
                    if hasattr(latest_special, side_field):
                        form.base_fields[side_field].initial = getattr(latest_special, side_field)
                
                # Set defaults for veggies
                for num in range(1, 13):
                    veggie_field = f"veggie_{num}"
                    if hasattr(latest_special, veggie_field):
                        form.base_fields[veggie_field].initial = getattr(latest_special, veggie_field)
                
                # Set defaults for desserts
                for letter in ['w', 'x', 'y', 'z']:
                    dessert_field = f"{letter}_dessert"
                    if hasattr(latest_special, dessert_field):
                        form.base_fields[dessert_field].initial = getattr(latest_special, dessert_field)
        
        return form
