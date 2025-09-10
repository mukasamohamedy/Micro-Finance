from django.contrib import admin
from .models import LoanType, LoanApplication, Repayment, AdminAction

@admin.register(LoanType)
class LoanTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "interest_rate")
    search_fields = ("name",)


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "loan_type", "amount", "duration_months", "status", "applied_at")
    list_filter = ("status", "loan_type")
    search_fields = ("user__username", "loan_type__name")
    actions = ["approve_loans", "reject_loans"]

    def approve_loans(self, request, queryset):
        queryset.update(status="approved")
    approve_loans.short_description = "Approve selected loans"

    def reject_loans(self, request, queryset):
        queryset.update(status="rejected")
    reject_loans.short_description = "Reject selected loans"


@admin.register(Repayment)
class RepaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "loan", "payment_date", "amount_paid", "balance_remaining")
    search_fields = ("loan__user__username",)


@admin.register(AdminAction)
class AdminActionAdmin(admin.ModelAdmin):
    list_display = ("id", "admin", "loan", "action_type", "action_date")
    list_filter = ("action_type",)
