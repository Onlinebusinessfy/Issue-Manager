from django.contrib import admin
from .models import Issue

class IssueAdmin(admin.ModelAdmin):
    list_display=[
        "name", "summary", "created_on"
    ]

admin.site.register(Issue, IssueAdmin)