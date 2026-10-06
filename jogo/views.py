import random
from django.shortcuts import render
from .models import Partida


# Create your views here.
def boas_vindas(request):
    return render(request, 'jogo/boas_vindas.html')

def jogar(request):
    OPCOES = ['pedra', 'papel', 'tesoura']

    jogada_usuario = request.GET.get('jogada', None)
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

#também adicione essa view:
def historico(request):
    #partidas = Partida.objects.all()
    
    #ordem e limite
    #partidas = (Partida.objects.order_by("-criada_em")[:10])

    #filtro de resultados
    #partidas = (Partida.objects.filter(resultado = 'vitoria')[:4])
    #partidas = (Partida.objects.filter(resultado = 'vitoria').order_by("-criada_em")[:4])

    #contando resultados
    total = Partida.objects.all().count()

    #retornando colunas específicas
    #partidas = Partida.objects.values_list("jogador", "computador", "resultado")
    
    #return original
    #return render(request, "jogo/historico.html", {"partidas": partidas})

    #Exe1 Histórico (Busque todas as partidas e ordene pela data.)
    #partidas = (Partida.objects.order_by("criada_em")) 

    #2. Vitórias Conte quantas partidas tiveram resultado `vitoria`.
    #total = Partida.objects.filter(resultado = 'vitoria').count()

    #3. Filtro Mostre apenas partidas em que o jogador escolheu pedra.
    #partidas = (Partida.objects.filter(jogador = 'pedra'))

    #4. Mais recentes Mostre as cinco partidas mais recentes.
    #partidas = Partida.objects.order_by("-criada_em")[:5]

    #5. Desafio Mostre todas as partidas, da mais recente para a mais antiga, 
    # e diga quantas vitórias, derrotas e empates existem.
    partidas = (Partida.objects.order_by("-criada_em"))
    vitorias = Partida.objects.filter(resultado = 'vitoria').count()
    derrotas = Partida.objects.filter(resultado = 'derrota').count()
    empates = Partida.objects.filter(resultado = 'empate').count()

    #return adicionando o total
    return render(request, "jogo/historico.html", {"partidas": partidas, 
                                                   "total": total,
                                                   "vitorias": vitorias,
                                                   "derrotas": derrotas,
                                                   "empates": empates})
