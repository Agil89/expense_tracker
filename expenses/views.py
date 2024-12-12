from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Sum
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpensesByDateRangeView(generics.ListAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if not user_id or not start_date or not end_date:
            raise ValueError("user_id, start_date, and end_date are required.")

        return Expense.objects.filter(user_id=user_id, date__range=[start_date, end_date])


class ExpenseCategorySummaryView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        if not user_id or not month or not year:
            return Response(
                {"error": "user_id, month, and year are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        summary = (
            Expense.objects.filter(user_id=user_id, date__year=year, date__month=month)
            .values('category')
            .annotate(total=Sum('amount'))
        )
        return Response(summary, status=status.HTTP_200_OK)
