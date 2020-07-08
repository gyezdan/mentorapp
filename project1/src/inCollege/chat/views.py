from django.shortcuts import render
from django.contrib.auth.models import User                                # Django Build in User Model
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Message                                                   # Our Message model
from chat.serializers import MessageSerializer
from django.contrib.auth.decorators import login_required

@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



def message_view(request, sender, receiver): 
    # if request.method == "GET":
    return render(request, "chat/messages.html",
                      {'users': User.objects.exclude(username=request.user.username), #List of users
                       'receiver': User.objects.get(id=receiver), # Receiver context user object for using in template
                       'usermessages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)}) 


def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('forum')
    if request.method == "GET":
        return render(request, 'chat/chatplatform.html',
                      {'users': User.objects.exclude(username=request.user.username)}) #Returning context for all users except the current logged-in use

