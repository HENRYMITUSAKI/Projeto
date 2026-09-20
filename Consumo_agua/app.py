#CONSCIENTIZAÇÃO AMBIENTAL - CONSUMO DE ÁGUA E INFORMAÇÃO
#AUTOR: HENRIQUE LOPES DE FREITAS MITUSAKI

#ENTRADA
tipo_imovel= input("Digite o tipo de imóvel (Comercial, Casa ou Apartamento): ")
consumo_mensal= float(input("Qual seu consumo mensal em m³:"))

#PROCESSAMENTO

match tipo_imovel:
    case "Comercial"|"comercial":
         print("Tarifa Comercial aplicada - Consulte o Plano Corporativo.")
match consumo_mensal and tipo_imovel:
     case "Apartamento"| "apartamento" if consumo_mensal<10:
        print("Consumo econômico - Excelente controle no consumo de água.")
     case "Casa"| "casa"|"apartamento"|"Apartamento" if consumo_mensal <=25:
        print("Consumo moderado - Dentro do padrão residencial.")
     case _ if consumo_mensal >25:
        print("Consumo excessivo - adote medidas de economia e vefique vazamentos.")
