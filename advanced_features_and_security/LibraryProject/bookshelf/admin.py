from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Display the additional fields in the admin list view and user detail view
    list_display = ('username', 'email', 'date_of_birth',
                    'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_of_birth')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)
