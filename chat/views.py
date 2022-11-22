from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from chat.models import Room,FileModel,Message
from core.settings import BASE_DIR
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie



def index_view(request):
    return render(request, 'index.html', {
        'rooms': Room.objects.all(),
    })


def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'room.html', {
        'room': chat_room,
    })

@csrf_exempt
def Imagesend(request):
    user_obj=Message.objects.filter(user_id =  request.user.id).last()
    print(user_obj,"---rishi----")
    if request.method == "POST":
        img = request.FILES.getlist('files[]',None)
        # print(img,"--------- ")
        fullfil = img[0]
        print(fullfil," #######----")
        strfile = str(fullfil)
        extention = strfile.split(".")[-1]
        a=''
        if extention == 'jpeg' or extention =='png' or extention == "jpg" or extention =="img" :
            a='image'
        elif extention == 'mp4':
            a='video'
        else:
            a='others'
        print()
        
        image_save=FileModel(doc=img[0])
        image_save.save()
        print(image_save.doc.url,"---9***d99")
        return JsonResponse({'url':image_save.doc.url,'msgtype':a})

        


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    

