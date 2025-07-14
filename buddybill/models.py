from django.core.validators import MinValueValidator
from django.db import models

from users.models import User
from utils.models import BaseModel


class TopicTag(BaseModel):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)


class TransactionCategory(models.TextChoices):
    EXPENSE = "EXPENSE"
    SETTLEMENT = "SETTLEMENT"


class Transaction(BaseModel):
    particulars = models.CharField(
        max_length=255,
    )
    total_amount = models.IntegerField(validators=[MinValueValidator(0)])
    topic = models.ForeignKey(TopicTag, on_delete=models.PROTECT, null=True)
    category = models.CharField(
        choices=TransactionCategory,
        max_length=15,
        default=TransactionCategory.EXPENSE,
    )
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)


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


class UserFriend(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="friends")
    friend = models.ForeignKey(User, on_delete=models.PROTECT, related_name="+")
