from django.contrib import admin

from .models import User, Ad, Achievement, Note, UsersPosts


class UsersPostsAdmin(admin.ModelAdmin):
    model = UsersPosts
    list_display = ('users', 'posts', 'created_at')


admin.site.register(User)
admin.site.register(Ad)
admin.site.register(Achievement)
admin.site.register(Note)
admin.site.register(UsersPosts, UsersPostsAdmin)
