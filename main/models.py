from django.db import models

# ---------------- Main SECTION ----------------
class MainModel(models.Model):
    main_title = models.CharField(max_length=100, default='Welcome to our Website')
    back_image = models.ImageField(upload_to='back image/')
    para1 = models.TextField(max_length=100, default='Your perfect home is no longer a dream.')
    para2 = models.TextField(max_length=100, default='Spacious 2 & 3 BHK homes on Sarjapur-Attibele Road.')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.main_title


# ---------------- CAROUSEL ----------------
class Carousel(models.Model):
    slide_label = models.CharField(max_length=200, default='Discover Your Dream Home')
    content = models.TextField(max_length=200, default='Some representative placeholder content for the first slide.')
    Carousel_image = models.ImageField(upload_to='Carousel_images/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.slide_label or "Carousel Image"


# ---------------- CORE VALUES ----------------
class CoreValue(models.Model):
    title = models.CharField(max_length=100, default='write points here')

    def __str__(self):
        return self.title


class MissionVision(models.Model):
    mission = models.TextField(max_length=500, default='To constantly endeavour to be the Preferred Developer of Residential, Commercial and Hospitality spaces in the markets in which we operate, without compromising on our Core Values, for the benefit of all our Stakeholders.')
    vision = models.TextField(max_length=500, default='To be a World-class Organisation in our Products, Processes, People and Performance.')

    def __str__(self):
        return "Mission & Vision"


# ---------------- OVERVIEW ----------------
class Overview(models.Model):
    apartments = models.CharField(max_length=100, default='132')
    bhk_types = models.CharField(max_length=100, default='2 / 2.5 / 3')
    towers = models.CharField(max_length=100, default='Beautifully Designed 7 Towers')
    description = models.TextField(default='Nestled at the heart of the city, Living Structures offers a blissful ' \
    'living experience amidst greenery where serene natural vistas soothe the soul.' \
    ' Envisioned with modern urban living, this iconic residence is the epitome of dream living.' \
    ' Come and live your life at its best in the most coveted address where enchanting greens redefine' \
    ' your senses.')

    def __str__(self):
        return "Overview Section"     


# ---------------- STATS / PEOPLE ----------------
class Stat(models.Model):
    icon = models.CharField(max_length=10, default='⌛')
    title = models.CharField(max_length=100, default='Years Experience')
    value = models.CharField(max_length=100, default='10+')
    subtitle = models.CharField(max_length=100 , default='Years Experience')

    def __str__(self):
        return self.icon

