from django.contrib import admin

from .models import User, Ad, Achievement, Note, UsersAchievements


class UsersAchievementsAdmin(admin.ModelAdmin):
    model = UsersAchievements
    list_display = ('user', 'achievement', 'received_at')


admin.site.register(User)
admin.site.register(Ad)
admin.site.register(Achievement)
admin.site.register(Note)
admin.site.register(UsersAchievements, UsersAchievementsAdmin)
