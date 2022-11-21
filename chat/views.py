from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from chat.models import Room,FileModel
from core.settings import BASE_DIR
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect



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
    if request.method == "POST" and request.FILES['file_upload']:
        print("BBBBBBBBBBBBB")
        TagID = request.FILES['file_upload']
        print(type(TagID))
        data=FileModel(doc=TagID)
        data.save()
        


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    

