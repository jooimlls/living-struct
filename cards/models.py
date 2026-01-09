from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField

class Property(models.Model):
    # Basic Info
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=250)
    main_card_image = models.ImageField(upload_to='card image/', max_length=255, null=True, blank=True)
    units = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    
    # Banner Section
    bhk_type_1 = models.CharField(max_length=50, default="2 BHK")  # e.g., "2 BHK"
    bhk_units_1 = models.PositiveIntegerField(default=44)
    bhk_size_1 = models.CharField(max_length=100, default="1445 Sq. ft")
    bhk_price_1 = models.CharField(max_length=100, default="Contact for Price")
    
    bhk_type_2 = models.CharField(max_length=50, default="3 BHK")
    bhk_units_2 = models.PositiveIntegerField(default=88)
    bhk_size_2 = models.CharField(max_length=100, default="1760 – 1890 Sq. ft")
    bhk_price_2 = models.CharField(max_length=100, default="Contact for Price")
    
    land_parcel = models.CharField(max_length=100, default="2.1 Acres Land Parcel")
    location = models.TextField(default="Sarjapur-Attibele Road")
    
    # Landing Section
    welcome_title = models.CharField(max_length=200, default="Welcome to Our Project")
    welcome_subtitle = models.TextField(default="Building the future, one idea at a time.")
    landing_image = models.ImageField(upload_to='landing/', null=True, blank=True)
    
    # Description
    description_para1 = models.TextField()
    description_para2 = models.TextField(blank=True, null=True)
    
    # Highlights
    highlights = models.TextField(help_text="Enter each highlight on a new line")
    
    # Video
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    video_title = models.CharField(max_length=200, default="Discover Our Story")
    video_description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_highlights_list(self):
        """Convert highlights text to list"""
        return [h.strip() for h in self.highlights.split('\n') if h.strip()]


class PropertyImage(models.Model):
    """Gallery images for each property"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='property_gallery/')
    caption = models.CharField(max_length=200, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.property.title} - Image {self.order}"


class PropertySpecification(models.Model):
    """Specifications for each property"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='specifications')
    category = models.CharField(max_length=100)  # e.g., "Structure", "Doors and Shutters"
    details = models.TextField(help_text="Enter each detail on a new line")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.property.title} - {self.category}"
    
    def get_details_list(self):
        """Convert details text to list"""
        return [d.strip() for d in self.details.split('\n') if d.strip()]


class PropertyAmenity(models.Model):
    """Amenities for each property"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='amenities')
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, help_text="Emoji or icon class")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.property.title} - {self.name}"
# Create your models here.
