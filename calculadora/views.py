from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def adicao(request):
    return render(request, "adicao.html")

def subtracao(request):
    return render(request, "subtracao.html")

def multiplicacao(request):
    return render(request, "multiplicacao.html")

def divisao(request):
    return render(request, "divisao.html")

def calculoAdicao(request):
    n1 = int(request.GET["n1"])
    n2 = int(request.GET["n2"])
    resultado = n1+n2
    return render(request, "resultadoAdicao.html", {"resultado":resultado} )

def calculoSubtracao(request):
    n1 = int(request.GET["n1"])
    n2 = int(request.GET["n2"])
    resultado = n1-n2
    return render(request, "resultadoSubtracao.html", {"resultado":resultado} )

def calculoMultiplicacao(request):
    n1 = int(request.GET["n1"])
    n2 = int(request.GET["n2"])
    resultado = n1*n2
    return render(request, "resultadoMultiplicacao.html", {"resultado":resultado} )

def calculoDivisao(request):
    n1 = int(request.GET["n1"])
    n2 = int(request.GET["n2"])
    resultado = n1/n2
    return render(request, "resultadoDivisao.html", {"resultado":resultado} )


