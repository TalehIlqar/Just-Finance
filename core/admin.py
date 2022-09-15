from django.contrib import admin

# Register your models here.

from .models import Blog, Service, Finance, Tax, HR, About, Contact, FAQ

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)


@admin.register(Finance)
class AdminFinance(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)


@admin.register(Tax)
class AdminTax(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)


@admin.register(HR)
class AdminHR(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)


@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('name', 'number')
    search_fields = ('name',)


@admin.register(FAQ)
class AdminFAQ(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question',)


