from django.contrib import admin
from expenses.models import User, Expense

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    search_fields = ('username', 'email')
    ordering = ('id',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'amount', 'date', 'category')
    list_filter = ('category', 'date')
    search_fields = ('title', 'user__username')
    ordering = ('date',)
