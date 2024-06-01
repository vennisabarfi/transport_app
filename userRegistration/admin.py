from django.contrib import admin

#import models
from userRegistration.models import UserProfile

# Register models with admin site
# admin.site.register(CustomUser)
admin.site.register(UserProfile)

