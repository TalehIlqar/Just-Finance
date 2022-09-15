from modeltranslation.translator import translator, TranslationOptions
from .models import About, Blog, Contact, FAQ, Finance, HR, Service, Tax

class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ContactTranslationOptions(TranslationOptions):
    fields = ('name', 'number', 'subject')


class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


class FinanceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class HRTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class TaxTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(About, AboutUsTranslationOptions)
translator.register(Blog, BlogTranslationOptions)
translator.register(Contact, ContactTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(Finance, FinanceTranslationOptions)
translator.register(HR, HRTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
translator.register(Tax, TaxTranslationOptions)
