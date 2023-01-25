from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_superuser', 'first_name', 'last_name', 'email', 'phone', 'address')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(username=request.user.username)

    # def get_form(self, request, obj=None, change=False, **kwargs):
    #     form = super().get_form(request, obj=None, change=False, **kwargs)
    #     if not request.user.is_superuser:
    #         form.base_fields.pop('user_permissions')
    #         form.base_fields.pop('groups')
    #     return form

