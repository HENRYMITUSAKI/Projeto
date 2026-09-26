#Pesquisa de Satisfação
#Autor: Henrique Mitusaki 

#Entrada
excelente=0
ruim=0 

#PROCESSAMENTO
for i in range (50):
        nome= input("Digite seu nome:")
        idade= int(input("Digite a sua idade:"))
        opiniao= int(input("Qual sua avaliação? Digite 1 para EXCELENTE; 2 para BOM e 3 para RUIM:"))
        if opiniao== 1:
            excelente= excelente+1
        if opiniao== 3:
            ruim= ruim+1


#SAÍDA
print(f"EXCELENTES = {excelente}")
print(f"RUIM = {ruim}")