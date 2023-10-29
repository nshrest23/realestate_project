from django.contrib import admin
from .models import Listing

class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'address', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'price', 'zipcode')
    list_per_page = 10

# Register your models here.
admin.site.register(Listing, ListAdmin)