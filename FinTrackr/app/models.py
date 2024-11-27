from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Transaction Model
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"

# Budget Model
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")
    category = models.CharField(max_length=100)
    monthly_limit = models.DecimalField(max_digits=10, decimal_places=2)
    current_spending = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    month_year = models.DateField()

    def __str__(self):
        return f"Budget for {self.category}"

# Investment Model
class Investment(models.Model):
    INVESTMENT_TYPES = [
        ('Stocks', 'Stocks'),
        ('Mutual Funds', 'Mutual Funds'),
        ('Real Estate', 'Real Estate'),
        ('Others', 'Others'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="investments")
    investment_type = models.CharField(max_length=50, choices=INVESTMENT_TYPES)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    current_value = models.DecimalField(max_digits=10, decimal_places=2)
    investment_date = models.DateField()

    def __str__(self):
        return f"{self.investment_type} - {self.amount_invested}"

# Savings Goal Model
class SavingsGoal(models.Model):
    GOAL_STATUSES = [
        ('In Progress', 'In Progress'),
        ('Achieved', 'Achieved'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="savings_goals")
    goal_name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=GOAL_STATUSES, default='In Progress')

    def __str__(self):
        return self.goal_name

# Account Model
class Account(models.Model):
    ACCOUNT_TYPES = [
        ('Checking', 'Checking'),
        ('Savings', 'Savings'),
        ('Credit Card', 'Credit Card'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.account_name

# Transfer Model
class Transfer(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="outgoing_transfers")
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="incoming_transfers")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transfer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transfer {self.amount} from {self.from_account} to {self.to_account}"

# Report Model
class Report(models.Model):
    REPORT_TYPES = [
        ('Income vs Expense', 'Income vs Expense'),
        ('Budget Analysis', 'Budget Analysis'),
        ('Investment Overview', 'Investment Overview'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)
    report_date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return self.report_type
