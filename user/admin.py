from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html

from post.models import Post, Comment

User = get_user_model()

admin.site.register(Comment)
admin.site.register(User)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', '_author')
    list_filter = ('date_created',)
    list_display_links = ('title', 'text')


    def _author(self, obj):
        user = obj.author
        url = reverse('admin:user_user_changelist') + str(user.pk)
        return format_html(f'<a href="{url}">{user}</a>')

    _author.short_description = 'Автор'
