from django.shortcuts import render
import random
# Create your views here.


def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus = ['피자', '족발','번데기']
    pick = random.choice(menus)
    context = {
        'pick':pick,
        'pick':pick,
        'pick':pick,
        'pick':pick,
    }
    return render(request, 'dinner.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)


def dtl_practice(request):
    menus = ['탕수육', '찹살탕수육', '사천탕수육']
    empty_list = []
    context = {
        'menus': menus,
        'empty_list': empty_list,
    }
    return render(request, 'dtl_practice.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # 사용자의 요청이 request.GET 안에 들어있다
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)