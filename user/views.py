from django.http import Http404, JsonResponse
from django.shortcuts import render
from order.models import Order
from user.serializers import UserSerializer
from user.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
@csrf_exempt
def user(request): 
    if request.method == 'GET':
        user = User.objects.all()
        return render(request, 'user/user_list.html', {'user_list':user})
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        try:
            user = User.objects.get(user_name = user_name)
            request.session['user_id'] = user.id
            print(request.session['user_id'])
            return render(request, 'user/success.html',{'user': user})
        except:
            return Http404
        
        
    elif request.method == 'GET':
        return render(request, 'user/login.html')