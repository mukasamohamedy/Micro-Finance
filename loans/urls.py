from django.urls import path
from . import views

urlpatterns = [
    # User routes
    path("apply/", views.apply_loan, name="apply_loan"),
    path("list/", views.loan_list, name="loan_list"),
    path("repayments/<int:loan_id>/", views.repayment_list, name="repayment_list"),

    # Admin routes
    path("approve/<int:loan_id>/", views.approve_loan, name="approve_loan"),
    path("reject/<int:loan_id>/", views.reject_loan, name="reject_loan"),
]
