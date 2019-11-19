from django.shortcuts import render

# Create your views here.
def home(request):
    nome = 'Jovenel'
    idade = 16
    lista_atividade = {
        'Karate'
        'Game'
        'Tv'
        'Cellphone'
    }

context = {
    'atividade' : lista_atividade,
    'nome' : nome,
    'idade' : idade,
}

return render(request, 'home.html', context)