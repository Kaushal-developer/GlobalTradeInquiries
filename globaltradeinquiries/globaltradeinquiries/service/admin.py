from django.contrib import admin
from .models import Category, Product,Offer,Lead

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Custom admin interface for Category model.
    """
    list_display = ('name', 'description', 'created_at', 'updated_at')  # Columns to display in the admin table
    search_fields = ('name',)  # Searchable fields
    ordering = ('name',)  # Default ordering

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Custom admin interface for Product model.
    """
    list_display = ('name', 'category', 'price', 'stock', 'created_at', 'updated_at')  # Columns to display
    list_filter = ('category', 'created_at')  # Filters for the sidebar
    search_fields = ('name', 'category__name')  # Fields for search functionality
    ordering = ('-created_at',)  # Default ordering (newest first)
    readonly_fields = ('created_at', 'updated_at')  # Fields to display but not allow edits

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'stock', 'category', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Makes timestamps collapsible
        }),
    )

    # To display the product image preview in the admin list
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('category')  # Optimizes queries for related data

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount', 'start_time', 'end_time', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'start_time', 'end_time')



@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'company_name', 'category', 'product', 'inquiry_type', 'created_at')
    search_fields = ['name', 'email', 'phone_number', 'message']
    list_filter = ['inquiry_type', 'created_at']