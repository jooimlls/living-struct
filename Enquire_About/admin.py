from django.contrib import admin
from .models import top_section, IntroSection, Benefit, ContactInfo, Step

admin.site.register(top_section)
admin.site.register(IntroSection)
admin.site.register(Benefit)
admin.site.register(Step)
admin.site.register(ContactInfo)


from .models import WhoWeAre, AboutBlock, TeamMember

admin.site.register(WhoWeAre)
admin.site.register(AboutBlock)
admin.site.register(TeamMember)

# Register your models here.

