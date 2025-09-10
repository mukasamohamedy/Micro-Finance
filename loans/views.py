from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from .models import LoanApplication, LoanType, Repayment, AdminAction


# ✅ check if user is admin
def is_admin(user):
    return user.is_staff


# ============================
# User Views
# ============================

@login_required
def apply_loan(request):
    if request.method == "POST":
        loan_type_id = request.POST.get("loan_type")
        amount = request.POST.get("amount")
        duration = request.POST.get("duration")
        purpose = request.POST.get("purpose")

        loan_type = LoanType.objects.get(id=loan_type_id)

        Loan.objects.create(
            user=request.user,
            loan_type=loan_type,
            amount=amount,
            duration=duration,
            purpose=purpose,
        )

        return redirect("dashboard")  # back to user dashboard

    return redirect("dashboard")


@login_required
def loan_list(request):
    if request.user.is_staff:
        loans = LoanApplication.objects.all()
    else:
        loans = LoanApplication.objects.filter(user=request.user)
    return render(request, "loan/loan_list.html", {"loans": loans})


@login_required
def repayment_list(request, loan_id):
    loan = get_object_or_404(LoanApplication, id=loan_id)
    repayments = Repayment.objects.filter(loan=loan)
    return render(request, "loan/repayment_list.html", {"loan": loan, "repayments": repayments})


# ============================
# Admin Views
# ============================

@user_passes_test(is_admin)
def approve_loan(request, loan_id):
    loan = get_object_or_404(LoanApplication, id=loan_id)
    loan.status = "approved"
    loan.save()

    AdminAction.objects.create(
        loan=loan, admin=request.user, action_type="approve", action_note="Loan approved"
    )

    messages.success(request, f"Loan {loan.id} approved.")
    return redirect("loan_list")


@user_passes_test(is_admin)
def reject_loan(request, loan_id):
    loan = get_object_or_404(LoanApplication, id=loan_id)
    loan.status = "rejected"
    loan.save()

    AdminAction.objects.create(
        loan=loan, admin=request.user, action_type="reject", action_note="Loan rejected"
    )

    messages.warning(request, f"Loan {loan.id} rejected.")
    return redirect("loan_list")
