from django.http import HttpResponse
from django.shortcuts import render
from vendor.models import Vendor


from vendor.models import Vendor

# Create your views here.



def testing(request):
    vendors = Vendor.objects.all()

    context = {
        'vendors': vendors,
    }

    return render(request, 'testing.html', context)





