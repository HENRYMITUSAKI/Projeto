#Sistema de Monitoramento - RESERVATÓRIO DE ÁGUA
#AUTOR: HENRIQUE MITUSAKI

#IMPORTAÇÃO - BIBLIOTECA
from colorama import Fore, Style

#Lista
niveis_reservatorio_porcentagem = [20,40,60,80,100]

#Definição dos Status do Reservatório
def status_reservatorio (nivel):
    #Verifica na lista quais os níveis e qual o status de acordo com o nível.
    if nivel <= niveis_reservatorio_porcentagem[0]:
        return Fore.RED, "Nível Crítico: Reservatório Muito Baixo"
    elif nivel <=niveis_reservatorio_porcentagem[1]:
        return Fore.YELLOW, "Nível Baixo"
    elif nivel <=niveis_reservatorio_porcentagem[2]:
        return Fore.GREEN, "Nível Médio"
    elif nivel <=niveis_reservatorio_porcentagem[3]:
        return Fore.CYAN, "Nível Alto"
    else:
        return Fore.BLUE, "Reservatório com Nível Muito Alto: Alerta de Transbordamento."

#Exibição dos Níveis do Reservatório
nivel_atual= float(input("Qual o status atual do reservatório (%): "))
if 0<= nivel_atual <= niveis_reservatorio_porcentagem [4]:
    cor, mensagem = status_reservatorio(nivel_atual)
    print(cor+ f"Reservatório em {nivel_atual}% - {mensagem}" + Style.RESET_ALL)
else: 
    print(Fore.RED + "Erro: informe um valor entre 0 e 100%." + Style.RESET_ALL)  