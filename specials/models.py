from django.db import models

# Create your models here.

class Veggie(models.Model):
  veggie_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100, verbose_name="Veggie Name")
  
  class Meta:
    verbose_name = "Vegetable"
    verbose_name_plural = "Vegetables"
    ordering = ['name']
  
  def __str__(self):
    return self.name

class Special(models.Model):
  daily_special_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, verbose_name="Special Name")
  number_of_sides = models.IntegerField(verbose_name="Number of Sides")
  price = models.DecimalField(max_digits=5, decimal_places=2, default='0.00')

  class Meta:
    verbose_name = "Special"
    verbose_name_plural = "Specials"
    ordering = ['name']

  def __str__(self):
     return f'{self.name}'

class Dessert(models.Model):
  dessert_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100, verbose_name="Dessert Name")
  price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price")
  
  class Meta:
    verbose_name = "Dessert"
    verbose_name_plural = "Desserts"
    ordering = ['name']
    
  def __str__(self):
    return self.name

class DailySpecial(models.Model):
  daily_special_id = models.AutoField(primary_key=True)
  date = models.DateField()
  a_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                blank=True,
                                related_name='daily_special_a',
                                on_delete=models.SET_NULL)
  a_special_w_side = models.CharField(max_length=100, default="", blank=True, verbose_name="w/side")
  
  b_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                blank=True,
                                related_name='daily_special_b',
                                on_delete=models.SET_NULL)
  b_special_w_side = models.CharField(max_length=100, default="", blank=True, verbose_name="w/side")
  
  c_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                blank=True,
                                related_name='daily_special_c',
                                on_delete=models.SET_NULL)
  c_special_w_side = models.CharField(max_length=100, default="", blank=True, verbose_name="w/side")
  
  d_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                blank=True,
                                related_name='daily_special_d',
                                on_delete=models.SET_NULL)
  d_special_w_side = models.CharField(max_length=100, default="", blank=True, verbose_name="w/side")
  
  e_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                blank=True,
                                related_name='daily_special_e',
                                on_delete=models.SET_NULL)
  e_special_w_side = models.CharField(max_length=100, default="", blank=True, verbose_name="w/side")
  
  f_special = models.ForeignKey(Special, 
                                null=True,
                                default="",
                                blank=True,
                                related_name='daily_special_f',
                                on_delete=models.SET_NULL)
  f_special_w_side = models.CharField(max_length=100, default="", blank=True, verbose_name="w/side")
  
  veggie_1 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               blank=True,
                               related_name='daily_special_veggie_1',
                               on_delete=models.SET_NULL)
  veggie_2 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               blank=True,
                               related_name='daily_special_veggie_2',
                               on_delete=models.SET_NULL)
  veggie_3 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               blank=True,
                               related_name='daily_special_veggie_3',
                               on_delete=models.SET_NULL)
  veggie_4 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               blank=True,
                               related_name='daily_special_veggie_4',
                               on_delete=models.SET_NULL)
  veggie_5 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               blank=True,
                               related_name='daily_special_veggie_5',
                               on_delete=models.SET_NULL)
  veggie_6 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               blank=True,
                               related_name='daily_special_veggie_6',
                               on_delete=models.SET_NULL)
  veggie_7 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               blank=True,
                               related_name='daily_special_veggie_7',
                               on_delete=models.SET_NULL)
  veggie_8 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               blank=True,
                               related_name='daily_special_veggie_8',
                               on_delete=models.SET_NULL)
  veggie_9 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                               blank=True,
                               related_name='daily_special_veggie_9',
                               on_delete=models.SET_NULL)
  veggie_10 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                                blank=True,
                               related_name='daily_special_veggie_10',
                               on_delete=models.SET_NULL)
  veggie_11 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                                blank=True,
                               related_name='daily_special_veggie_11',
                               on_delete=models.SET_NULL)
  veggie_12 = models.ForeignKey(Veggie, 
                               null=True,
                               default="",
                                blank=True,
                               related_name='daily_special_veggie_12',
                               on_delete=models.SET_NULL)

  
  w_dessert = models.ForeignKey(Dessert, 
                                null=True,
                                default="",
                                blank=True,
                                related_name='daily_special_dessert_1',
                                on_delete=models.SET_NULL)
  x_dessert = models.ForeignKey(Dessert, 
                                null=True,
                                default="",
                                blank=True,
                                related_name='daily_special_dessert_2',
                                on_delete=models.SET_NULL)
  y_dessert = models.ForeignKey(Dessert, 
                                null=True,
                                default="",
                                blank=True,
                                related_name='daily_special_dessert_3',
                                on_delete=models.SET_NULL)
  z_dessert = models.ForeignKey(Dessert, 
                                null=True,
                                default="",
                                blank=True,
                                related_name='daily_special_dessert_4',
                                on_delete=models.SET_NULL)


  def date_formatted(self):
    return self.date.strftime('%B %d, %Y')

  def date_day(self):
    return self.date.strftime("%A")
  
  def __str__(self):
    return f"{self.date_day()} Specials, {self.date_formatted()}"

  
    def save(self, *args, **kwargs):
      # Add functionalities here if needed before saving the DailySpecial instance
      super(DailySpecial, self).save(*args, **kwargs)
      import sys

  class Meta:
    verbose_name = "Daily Special"
    verbose_name_plural = "Daily Specials"
    ordering = ['-date']