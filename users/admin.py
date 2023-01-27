from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_superuser', 'first_name', 'last_name', 'email', 'phone', 'address')
    readonly_fields = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """
        Current Login User can see only their profile via this method.
        if current Login user is SUPERUSER then he/she can view all
        the profiles.
        """
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(username=request.user.username)

    def get_readonly_fields(self, request, obj=None):
        """
        When the use logged in & the user type is SUPERUSER then
        he/she can view/delete/modified the permissions in admin site.
        but if the user is Normal Staff user and not a SUPERUSER then this
        option is only read fields.
        """
        if request.user.is_superuser:
            return ()
        else:
            return self.readonly_fields
