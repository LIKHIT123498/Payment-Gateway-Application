from django.db import models

# Create your models here.
class Payment(models.Model):
    razorpay_order_id=models.CharField(max_length=100,unique=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_signature=models.CharField(max_length=255,blank=True,null=True)
    amount=models.IntegerField()
    status=models.CharField(max_length=50,default='created')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.razorpay_order_id}-{self.status}"