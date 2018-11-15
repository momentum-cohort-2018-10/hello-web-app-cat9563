from django.contrib import admin
from collection.models import Cat
# Register your models here.
admin.site.register(Cat)

#set up automated slug creation 
class CatAdmin(admin.ModelAdmin):
    model = Cat
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.unregister(Cat)
admin.site.register(Cat, CatAdmin)