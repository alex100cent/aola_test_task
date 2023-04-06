from django.contrib import admin

from .models import User, Ad, Achievement, Note, UsersEvents


class UsersAchievementsAdmin(admin.ModelAdmin):
    model = UsersEvents
    list_display = ('user', 'event', 'created_at')


admin.site.register(User)
admin.site.register(Ad)
admin.site.register(Achievement)
admin.site.register(Note)
admin.site.register(UsersEvents, UsersAchievementsAdmin)
