from django.contrib import admin

# Register your models here.

from .models import Blog, Service, Finance, Tax, HR, About, Contact, FAQ, ApplicationCategory, Settings, Subscriber


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)
    readonly_fields = ('slug',)


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)
    readonly_fields = ('slug',)


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


@admin.register(ApplicationCategory)
class AdminApplicationCategory(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Settings)
class AdminSettings(admin.ModelAdmin):
    list_display = ('slogan',)
    search_fields = ('slogan',)

    def has_add_permission(self, request):
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Subscriber)
class AdminSubscriber(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
