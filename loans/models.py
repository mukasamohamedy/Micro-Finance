from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class LoanType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.interest_rate}%)"


class LoanApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('paid', 'Paid'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    duration_months = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan {self.id} - {self.user.username} - {self.status}"


class Repayment(models.Model):
    loan = models.ForeignKey(LoanApplication, on_delete=models.CASCADE, related_name="repayments")
    payment_date = models.DateField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    balance_remaining = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Repayment {self.id} for Loan {self.loan.id}"


class AdminAction(models.Model):
    ACTION_CHOICES = [
        ('approve', 'Approve Loan'),
        ('reject', 'Reject Loan'),
        ('delete', 'Delete Loan'),
        ('update', 'Update Loan'),
    ]

    loan = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES)
    action_note = models.TextField(blank=True, null=True)
    action_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admin.username} - {self.action_type} - Loan {self.loan.id}"
