from django.db import models
class Footer(models.Model):
    # Company Info
    tagline = models.TextField(max_length=200, default='Your trusted real-estate partner helping you find your dream home.')
    
    # Contact Info
    Footer_email = models.EmailField(default='Livingstructuresakura@gmail.com')
    Footer_phone = models.CharField(max_length=20, default='+91 6364863933')
    Footer_location = models.CharField(max_length=200, default='Bengaluru, India')
    
    # Social Media
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    
    # Team Members (simple approach)
    team_members = models.TextField(
        max_length=500, 
        default='Mohan Reddy G, Nagesh K V, Suresh Surya, Bridged Suren',
        help_text='Enter member names separated by commas'
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Footer Content'
        verbose_name_plural = 'Footer Content'

    def __str__(self):
        return f"Footer - {self.tagline}"
    
    def get_team_members_list(self):
        """Returns team members as a list"""
        return self.team_members.split(',')
    
# Create your models here.
