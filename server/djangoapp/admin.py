from django.contrib import admin
from .models import CarMake, CarModel

# 1. Define the Inline for CarModel
# This allows CarModels to be edited directly within the CarMake admin page.
class CarModelInline(admin.TabularInline):
    """
    Inline model definition for CarModel.
    Shows CarModel fields in a tabular format when viewing the parent CarMake.
    """
    model = CarModel
    extra = 3  # Display 3 extra empty forms for adding new Car Models

# 2. Define the Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CarMake model.
    Includes the CarModelInline to manage models associated with a make.
    """
    list_display = ('name', 'description')
    inlines = [CarModelInline]
    search_fields = ['name']
    list_filter = ['name']

# 3. Define the Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CarModel model.
    """
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name')
    # Use fieldsets to organize the form in the admin interface (optional, but good practice)
    fieldsets = (
        (None, {
            'fields': ('name', 'car_make')
        }),
        ('Specifications', {
            'fields': ('type', 'year'),
            'classes': ('collapse',), # Makes the section collapsible
        })
    )


# 4. Register models with their respective admin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)