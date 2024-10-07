from .forms import PostForm
from django.shortcuts import render
from .models import GuessNumbers
from django.http import HttpResponse
def index(request):
    lottos = GuessNumbers.objects.all() # DB에 저장된 GuessNumbers 객체 모두를 가져온
    #return HttpResponse('<h1>Hello, world!</h1>')
    #return render(request, 'lotto/default.html', {})
    return render(request, 'lotto/default.html', {'lottos':lottos})


def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request) :

    if request.method == 'POST' :
        form = PostForm(request.POST)
        if form.is_valid() :
            lotto = form.save(commit = False)
            print(type(lotto))
            print(lotto)
            lotto.generate()
            return redirect('index')
    else :
        form = PostForm()
        return render(request, "lotto/form.html", {"form":form})
    
def detail(request, lottokey) :
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/detail.html", {"lotto": lotto})


# Create your views here.
