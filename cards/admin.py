from django.contrib import admin
from .models import Property, PropertyImage, PropertySpecification, PropertyAmenity


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


class PropertySpecificationInline(admin.TabularInline):
    model = PropertySpecification
    extra = 1


class PropertyAmenityInline(admin.TabularInline):
    model = PropertyAmenity
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'units', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    inlines = [PropertyImageInline, PropertySpecificationInline, PropertyAmenityInline]


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'caption', 'order')
    list_filter = ('property',)


@admin.register(PropertySpecification)
class PropertySpecificationAdmin(admin.ModelAdmin):
    list_display = ('property', 'category', 'order')
    list_filter = ('property',)


@admin.register(PropertyAmenity)
class PropertyAmenityAdmin(admin.ModelAdmin):
    list_display = ('property', 'name', 'icon', 'order')
    list_filter = ('property',)
# Register your models here.
