from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


from .models import Car, Contact, News


@admin.register(Car)
class CarAdmin(TranslationAdmin):
    list_display = ('brand_car', 'model_car')


admin.site.register(Contact)
admin.site.register(News)

# Register your models here.
