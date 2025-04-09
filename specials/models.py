from django.db import models

# Create your models here.

class SpecialPrice(models.Model):
  special_price_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  total = models.DecimalField(max_digits=4, decimal_places=2)

  def __str__(self):
    return f'${self.price_total}'

class Veggie(models.Model):
  veggie_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)

class Special(models.Model):
  daily_special_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  number_of_sides = models.IntegerField(max_length=1)
  price = models.ForeignKey(SpecialPrice, on_delete=models.SET_NULL)

  def __str__(self):
     return f'{self.name} ({self.special_price})'

class Dessert(models.Model):
  dessert_id = models.AutoField(primary_key=True)
  name = models.CharField()
  price = models.DecimalField(max_digits=5, decimal_places=2)
  
  def __str__(self):
    return self.name

class DailySpecial(models.Model):
  daily_special_id = models.AutoField(primary_key=True)
  date = models.DateField()
  a_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                on_delete=models.SET_NULL)
  b_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                on_delete=models.SET_NULL)
  c_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                on_delete=models.SET_NULL)
  d_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                on_delete=models.SET_NULL)
  e_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                on_delete=models.SET_NULL)
  f_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                on_delete=models.SET_NULL)

  veggie_1 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               on_delete=models.SET_NULL)
  veggie_2 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               on_delete=models.SET_NULL)
  veggie_3 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               on_delete=models.SET_NULL)
  veggie_4 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               on_delete=models.SET_NULL)
  veggie_5 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               on_delete=models.SET_NULL)
  veggie_6 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               on_delete=models.SET_NULL)
  veggie_7 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               on_delete=models.SET_NULL)
  veggie_8 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               on_delete=models.SET_NULL)

  dessert_1 = models.ForeignKey(Dessert, 
                                null=True,
                                default="",
                                on_delete=models.SET_NULL)
  dessert_2 = models.ForeignKey(Dessert, 
                                null=True,
                                default="",
                                on_delete=models.SET_NULL)
  dessert_3 = models.ForeignKey(Dessert, 
                                null=True,
                                default="",
                                on_delete=models.SET_NULL)
  dessert_4 = models.ForeignKey(Dessert, 
                                null=True,
                                default="",
                                on_delete=models.SET_NULL)


  def date_formatted(self):
    return self.date.strftime('%m/%d/%y')

  def date_day(self):
    return self.date.strftime("%A")
  
  def __str__(self):
    return f"{self.date_day}'s Specials, {self.date_formatted}"