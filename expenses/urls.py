from django.urls import path
from .views import (
    ExpenseListCreateView,
    ExpenseDetailView,
    ExpensesByDateRangeView,
    ExpenseCategorySummaryView,
)

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('expenses/date-range/', ExpensesByDateRangeView.as_view(), name='expenses-date-range'),
    path('expenses/category-summary/', ExpenseCategorySummaryView.as_view(), name='expenses-category-summary'),
]
