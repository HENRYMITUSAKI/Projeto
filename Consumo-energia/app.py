#Calculadora de Consumo Elétrico Inteligente
#Autor: Henrique Lopes de Freitas Mitusaki

#Entrada
aparelho=input("Qual aparelho você deseja calcular o consumo elétrico? ")
potencia=float(input("Qual a potência do aparelho em Watts? "))
tempo=float(input("Quantas horas por dia você utiliza o aparelho? "))
#Processamento
consumo_mensal=potencia*tempo*30/1000
tarifa_kwh=float(0.4724)
custo_mensal=consumo_mensal*tarifa_kwh
#Saída
print(f"O consumo mensal do {aparelho} é de {consumo_mensal} kWh.")
print(f"O custo mensal do {aparelho} é de R$ {custo_mensal:.2f}.")
