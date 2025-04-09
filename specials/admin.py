
from django.contrib import admin
from .models import SpecialPrice, Veggie, Special, Dessert, DailySpecial

@admin.register(SpecialPrice)
class SpecialPriceAdmin(admin.ModelAdmin):
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
            'fields': ('a_special', 'b_special', 'c_special', 'd_special', 'e_special', 'f_special'),
        }),
        ('Veggies', {
            'fields': ('veggie_1', 'veggie_2', 'veggie_3', 'veggie_4', 
                      'veggie_5', 'veggie_6', 'veggie_7', 'veggie_8'),
            'classes': ('collapse',),
        }),
        ('Desserts', {
            'fields': ('dessert_1', 'dessert_2', 'dessert_3', 'dessert_4'),
            'classes': ('collapse',),
        }),
    )
