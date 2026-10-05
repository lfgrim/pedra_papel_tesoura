import random
from django.shortcuts import render
from .models import Partida


# Create your views here.
def boas_vindas(request):
    return render(request, 'jogo/boas_vindas.html')

def jogar(request):
    OPCOES = ['pedra', 'papel', 'tesoura']

    jogada_usuario = request.GET.get('jogada', None)
    
    if jogada_usuario == None:
        jogada_usuario = random.choice(OPCOES)

    ctx = {'jogada_usuario': jogada_usuario}

    jogada_pc = random.choice(OPCOES)
    resultado = 'empate'

    if jogada_usuario in OPCOES:
        ctx['jogada_pc'] = jogada_pc
        
        if jogada_usuario == jogada_pc:
            resultado = 'empate'
        elif (
            (jogada_usuario=='pedra' and jogada_pc=='tesoura') or
            (jogada_usuario=='papel' and jogada_pc=='pedra') or
            (jogada_usuario=='tesoura' and jogada_pc=='papel')
        ):
            resultado = 'vitoria'
        else:
            resultado = 'derrota'
        
        ctx['resultado'] = resultado

    Partida.objects.create(
        jogador=jogada_usuario,
        computador=jogada_pc,
        resultado=resultado,
    )
    
    return render(request, 'jogo/jogar.html', ctx)


