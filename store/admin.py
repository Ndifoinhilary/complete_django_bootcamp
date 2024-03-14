from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.db.models import Count

from store import models
# Register your models here.





@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    list_display = ['title', 'price', 'slug', 'collection', 'inventory_status', 'last_update']
    prepopulated_fields = {'slug':['title']}
    list_editable = ['price', 'slug']
    list_per_page =  10

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory > 50:
            return "OK"
        else:
            return "Low"
    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        queryset_count = queryset.update(inventory = 0)

        return self.message_user(request,
            f'{queryset_count} inventory product was update successfully'
        )



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'birth_date']
    list_editable = ['phone', 'email']
    list_per_page =  10

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']
    list_display_links = ['title', 'product_count']

    def product_count(self, collection): 
        return collection.product_count
    
    def get_queryset(self, request: HttpRequest):

        return super().get_queryset(request).annotate(
            product_count = Count('product')
        )
    



admin.site.register(models.Order)
admin.site.register(models.OrderItem)
# admin.site.register(models.Product)
admin.site.register(models.Promotion)