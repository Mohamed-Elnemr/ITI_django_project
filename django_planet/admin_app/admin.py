from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

UserAdmin.list_display += ('is_active',)
UserAdmin.list_display_links = ('username',)
UserAdmin.list_editable = ('is_active',)

# class PermissionAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ['permissions info', {
#             'fields': ['name']}],
#     )
#     model = Permission
#     # fields = ['name']
#
#
# admin.site.register(Permission, PermissionAdmin)

