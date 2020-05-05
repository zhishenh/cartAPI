from django.db import models

# Create your models here.
class CartItem(models.Model):
    user_id = models.IntegerField()
    item_number = models.CharField(max_length=10)
    qty = models.IntegerField()
    in_dtm = models.DateTimeField(auto_now_add=True)
    update_dtm = models.DateTimeField(auto_now=True)
