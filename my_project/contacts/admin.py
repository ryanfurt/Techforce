from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ("name","number","email")
    list_display_links = ["name"]
    list_filter = ("name","number")
    search_fields = ("name","number")
    class Meta:
        model = Contact

admin.site.register(Contact, ContactModelAdmin)