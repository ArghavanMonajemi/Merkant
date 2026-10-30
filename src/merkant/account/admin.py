from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User,Profile, Address

class CustomUserAdmin(UserAdmin):
    model = User
    list_per_page = 20
    list_display = (
        "email",
        "type",
        "is_active",
        "is_verified",
        "created_date",
    )
    list_filter = (
        "type",
        "is_active",
        "is_verified",
        "created_date",
        "updated_date"
    )
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "type")}),
        ("Groups Permissons", {"fields": ("groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff"),
            },
        ),
    )
    ordering = ("created_date",)

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["full_name","user_email","created_date","updated_date"]
    # @admin.display(description="Name", ordering="last_name")
    # def full_name(self, obj):
    #     return f"{obj.first_name} {obj.last_name}"
    @admin.display(description="Email", ordering="user__email")
    def user_email(self, obj):
        return obj.user.email
    readonly_fields = ["created_date","updated_date","user"]
    list_per_page = 20
    list_filter = (
            "user__type",
            "created_date",
            "updated_date"
        )

class AddressAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["profile","title","country","city","created_date","updated_date"]
    readonly_fields = ["created_date","updated_date","profile"]
    list_per_page = 20
    list_filter = (
        "profile",
        "country",
        "state",
        "city"
    )


admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Address,AddressAdmin)