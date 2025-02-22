from django.contrib import admin
from .models import UserProfile  # Ensure the model is imported

admin.site.register(UserProfile)
