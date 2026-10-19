from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import razorpay
from .models import Payment

# Create your views here.
razorpay_client=razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))

def homepage(request):
    amount=2000
    currency='INR'

    razorpay_order=razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))

    Payment.objects.create(razorpay_order_id=razorpay_order['id'],amount=amount,status='Created')

    context = {
    'razorpay_order_id': razorpay_order['id'],
    'razorpay_merchant_key': settings.RAZOR_KEY_ID,
    'razorpay_amount': amount,
    'currency': currency,
    'callback_url': '/paymenthandler/',
}
    return render(request,'index.html',context)

@csrf_exempt
def paymenthandler(request):
    if request.method=="POST":
        payment_id=request.POST.get('razorpay_payment_id','')
        razorpay_order_id=request.POST.get('razorpay_order_id','')
        signature=request.POST.get('razorpay_signature','')

        params_dict={'razorpay_order_id':razorpay_order_id,
                     'razorpay_payment_id':payment_id,
                     'razorpay_signature':signature}

        
        try:
            razorpay_client.utility.verify_payment_signature(params_dict)
            
            # GET THE OBJECT: Fetch the payment record from your DB
            payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)

            # CRITICAL ADDITION: Ensure amount is an integer (Paise)
            # Razorpay will throw an error if this is a float or string
            capture_amount = int(payment.amount)
            
            # CAPTURE THE PAYMENT: This prevents the auto-refund
            razorpay_client.payment.capture(payment_id, capture_amount)
            
            # UPDATE RECORD: Save the IDs and mark as Success
            payment.razorpay_payment_id = payment_id
            payment.razorpay_signature = signature
            payment.status = 'Success'
            payment.save()

            return render(request, 'paymentsuccess.html')

        except razorpay.errors.SignatureVerificationError:

            Payment.objects.filter(razorpay_order_id=razorpay_order_id).update(status='Failed')
            return render(request, 'paymentfail.html')
            
        except Exception as e:
            
            return HttpResponseBadRequest(f"Payment Processing Error: {str(e)}")
    else:
        return HttpResponseBadRequest("Invalid request method")
