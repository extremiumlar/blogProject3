from django.contrib import admin
from .models import News, Category, Contact, Comentary

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','publish_time','status']
    list_filter = ['status','created','publish_time']
    #prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title']
    ordering = ['status','publish_time']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_didplay = ['id','name']

admin.site.register(Contact)


class ComentaryAdmin(admin.ModelAdmin):
    list_display = ['user','body','active','created']
    list_filter = ['active','created']
    search_fields = ['body','user']
    actions = ['disable_coments','active_coments']

    def disable_coments(self,request,queryset):
        queryset.update(active=False)
    def active_coments(self,request,queryset):
        queryset.update(active=True)

admin.site.register(Comentary,ComentaryAdmin)
