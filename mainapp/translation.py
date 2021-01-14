from modeltranslation.translator import register, TranslationOptions

from .models import Car, Contact, News


@register(Car)
class CarTranslation(TranslationOptions):
    # exclude = ('brand_car', 'model_car', 'image_car', 'price_car')
    fields = ('model_car', 'title_car')