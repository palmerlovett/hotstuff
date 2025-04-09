
from django.contrib import admin
from .models import SpecialPrice, Veggie, Special, Dessert, DailySpecial

from django import forms

class SpecialPriceForm(forms.ModelForm):
    class Meta:
        model = SpecialPrice
        fields = '__all__'
        labels = {
            'name': 'Price Description',
            'total': 'Price Amount',
        }

@admin.register(SpecialPrice)
class SpecialPriceAdmin(admin.ModelAdmin):
    form = SpecialPriceForm
    list_display = ('name', 'total')
    search_fields = ('name',)
    list_filter = ('total',)

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
            ]
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
                'veggie_11',
                'veggie_12',
            ],
            'classes': ('columns-2',),
        }),
        ('Desserts', {
            'fields': ['dessert_1', 'dessert_2', 'dessert_3', 'dessert_4'],
            'classes': ('collapse',),
        }),
    )
