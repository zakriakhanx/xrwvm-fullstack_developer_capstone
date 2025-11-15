from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Car Make model: Represents a manufacturer of cars (e.g., Ford, Toyota)
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # The __str__ method to return a readable representation of the object
    def __str__(self):
        return self.name


# Car Model model: Represents a specific vehicle model produced by a car make (e.g., F-150, Corolla)
class CarModel(models.Model):
    # Many-To-One relationship to CarMake (One CarMake can have multiple CarModels)
    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE  # If the CarMake is deleted, all associated CarModels are also deleted
    )
    name = models.CharField(max_length=100)

    # Choices for the car type
    CAR_TYPES = (
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
    )

    type = models.CharField(
        max_length=15,
        choices=CAR_TYPES,
        default='SEDAN',
        help_text="Select car type"
    )

    # Year field with specified validators
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ],
        default=2023
    )

    # The __str__ method to return a readable representation of the object
    def __str__(self):
        return f"Model: {self.name} ({self.car_make.name}) - Type: {self.type} - Year: {self.year}"
