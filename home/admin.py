from django.contrib import admin
from .models import PortfolioItem


@admin.register(PortfolioItem)
class PortfolioItemModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'repository', 'order']
    list_editable = ['order']
    list_filter = ['status']
