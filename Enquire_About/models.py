from django.db import models

class top_section(models.Model):
    title = models.CharField(max_length=200, default="Find Your Dream Property Today!")
    subtitle = models.TextField(max_length=500, default="Your journey to the perfect home starts here. Let our experts guide you every step of the way.")

    def __str__(self):
        return self.title


class IntroSection(models.Model):
    heading = models.CharField(max_length=200, default="Ready to Make a Move?")
    description = models.TextField(default="Whether you're looking to buy flat or home our experienced team is here to guide you every step of the way. Share your requirements with us, and we'll help you find the perfect property match tailored to your needs and budget.")

    def __str__(self):
        return self.heading


class Benefit(models.Model):
    icon = models.CharField(max_length=10)  # emoji or icon class
    title = models.CharField(max_length=100, default="Free Consultation")
    description = models.TextField(default="Get expert property advice at no cost. Our team provides personalized guidance for your unique needs.")

    def __str__(self):
        return self.title


class Step(models.Model):
    step_number = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=100, default="Submit Your Requirements")
    description = models.TextField(default="Tell us what you're looking for - budget, location, property type, and preferences.")

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}"


class ContactInfo(models.Model):
    phone = models.CharField(max_length=20,)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    office_hours = models.CharField(max_length=100,default="Office Hours: Monday - Saturday, 9:00 AM - 7:00 PM")

    def __str__(self):
        return self.phone
    
class WhoWeAre(models.Model):
    label = models.CharField(max_length=50, default="WHO WE ARE")
    heading = models.CharField(max_length=200, default="A Bengaluru Developer Creating Sustainable,Future-Ready Living Spaces.")
    top_image = models.ImageField(upload_to="about/")
    bottom_image = models.ImageField(upload_to="about/")

    def __str__(self):
        return self.heading

class AboutBlock(models.Model):
    title = models.CharField(max_length=50, default="Our Mission")
    description = models.TextField( default="We aim to address urbanisation challenges through eco-conscious design and" \
    " innovation, setting benchmarks in sustainability, transparency, and global quality standards, while delivering projects" \
    " that embody trust, excellence, and long-term value for our customers and society.")

    css_class = models.CharField(
        max_length=50,
        help_text="Example: vision-section, mission-section, philosophy-section"
    )

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100, default="Suresh Surya")
    role = models.CharField(max_length=100, default=" Finance and Accounting Manager")
    image = models.ImageField(upload_to="team/")
    bio = models.TextField(default="Suresh Surya is a Chartered Accountant with over 7 years of professional experience "
    "in finance and accounting. Currently at Living Structures, he has spent the last 6 years managing financial operations "
    "within the real estate sector.")

    def __str__(self):
        return self.name



# Create your models here.
