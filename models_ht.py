from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    season_menu = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField()
    ingredients = models.CharField(max_length=250)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    category = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name='menu')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Chefs(models.Model):
    first_name = models.TextField(max_length=20, unique=True)
    second_name = models.TextField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    experience = models.CharField(max_length=250)
    position = models.PositiveSmallIntegerField(unique=True)  #position on the page
    chef_position = models.CharField(max_length=30)  #(executive, head, deputy, station, etc.)
    photo = models.ImageField(upload_to='chefs/', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Events(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    date = models.DateTimeField()
    description = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}'


class About(models.Model):
    restaurant_name = models.CharField(max_length=100)
    city_name = models.TextField(max_length=30)
    street_name = models.TextField(max_length=30)
    building_number = models.DecimalField()
    restaurant_type = models.TextField(max_length=50)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    parking = models.BooleanField(default=True)
    executive_chef = models.ForeignKey(Chefs, on_delete=models.PROTECT)  #check

    def __str__(self):
        return f'{self.restaurant_name}'

