from django.test import TestCase

# Create your tests here.
@csrf_exempt
def Imagesend(request):
    if request.method=='POST':
        print(request.FILES)
        print('working')
    return render(request,'image.html')