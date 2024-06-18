from .models import *
from modeltranslation.translator import TranslationOptions, register

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('image', 'caption')


