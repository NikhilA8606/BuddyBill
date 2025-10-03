from django.core.validators import MinValueValidator
from django.db import models

from users.models import User
from utils.models import BaseModel


class TransactionCategory(models.TextChoices):
    EXPENSE = "EXPENSE"
    SETTLEMENT = "SETTLEMENT"


class Transaction(BaseModel):
    particulars = models.CharField(
        max_length=255,
    )
    total_amount = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.CharField(
        choices=TransactionCategory,
        max_length=15,
        default=TransactionCategory.EXPENSE,
    )
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="+")
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="+")
    ouccured_at = models.DateTimeField(auto_now_add=True)


class TransactionEntry(BaseModel):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    buddy = models.ForeignKey(User, on_delete=models.PROTECT)


class BuddyGroup(BaseModel):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)


class BuddyGroupUser(BaseModel):
    buddy_group = models.ForeignKey(BuddyGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
