from django.core.validators import MinValueValidator
from django.db import models

from users.models import User
from utils.models import BaseModel

class TopicTag(BaseModel):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL)


class Transaction(BaseModel):
    particulars = models.CharField(
        max_length=255,
    )
    total_amount = models.IntegerField(validators=[MinValueValidator(0)])
    topic = models.ForeignKey(TopicTag,on_delete=models.PROTECT,null=True)
    category = models.CharField(choices=["expense","settlement"],max_length=255)



