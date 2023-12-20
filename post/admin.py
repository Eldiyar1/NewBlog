from django.contrib import admin

from .models import Product, HashTag, Comment, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'created_at']
    list_editable = ['rate']
    list_filter = ['hashtags', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'content', 'hashtags__title']

    def has_add_permission(self, request):
        return True

    # def has_delete_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request):
    #     return False

admin.site.register(HashTag)
admin.site.register(Comment)
admin.site.register(Category)
