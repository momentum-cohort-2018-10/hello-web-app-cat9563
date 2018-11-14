from django.contrib import admin
from collection.models import Cats
# Register your models here.
admin.site.register(Cats)

#set up automated slug creation 
class CatsAdmin(admin.ModelAdmin):
    model = Cats
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.unregister(Cats)
admin.site.register(Cats, CatsAdmin)