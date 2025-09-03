from django.db import models

# Create your models here.
# class LoanType(models.Model):
#     loan_type_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return self.name
    


# class ApplicationLoan(models.Model):
#     loan_id = models.AutoField(primary_key=True)
#     amount = models.DecimalField(max_digits=12, decimal_places=2)
#     duration_months = models.PositiveIntegerField()
#     status = models.CharField(max_length=50, choices=[
#         ("Pending", "Pending"),
#         ("Approved", "Approved"),
#         ("Rejected", "Rejected"),
#         ("Completed", "Completed"),
#     ])
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loans")
#     loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE, related_name="applications")

#     def __str__(self):
#         return f"Loan {self.loan_id} - {self.user.full_name}"


# class Repayment(models.Model):
#     repayment_id = models.AutoField(primary_key=True)
#     payment_date = models.DateField()
#     amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
#     balance_remaining = models.DecimalField(max_digits=12, decimal_places=2)
#     loan = models.ForeignKey(ApplicationLoan, on_delete=models.CASCADE, related_name="repayments")

#     def __str__(self):
#         return f"Repayment {self.repayment_id} - Loan {self.loan.loan_id}"


# class Admin(models.Model):
#     admin_id = models.AutoField(primary_key=True)
#     action_type = models.CharField(max_length=100)
#     action_note = models.TextField(blank=True, null=True)
#     action_date = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     loan = models.ForeignKey(ApplicationLoan, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return f"Admin {self.admin_id} - {self.action_type}"


# class Message(models.Model):
#     message_id = models.AutoField(primary_key=True)
#     subject = models.CharField(max_length=255)
#     message = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")

#     def __str__(self):
#         return f"Message {self.message_id} from {self.user.username}"


# 