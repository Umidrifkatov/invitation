from django.contrib import admin
from .models import Visitor


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'seating_place', 'custom_method',)
    search_fields = ('name', 'seating_place')  # Add fields for search
    list_filter = ('seating_place',)  # Add a filter for seating place
    
    def custom_method(self, obj):
        return f"umidsevinch.invitation.uz/{obj.unique_identifier}"
    custom_method.short_description = 'Custom Display'

admin.site.register(Visitor, VisitorAdmin)



