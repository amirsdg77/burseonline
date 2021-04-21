from django.contrib import admin

from .models import Blog, Education, Category,Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'body_text']

    class Meta:
        model = Comment


admin.site.register(Blog)
admin.site.register(Education)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
