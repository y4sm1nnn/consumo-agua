try:
    # entrada de informações do usuário
    tipo_imovel = input("digite o tipo de imóvel (comercial, casa ou apartamento): ")
    consumo = float(input("digite o consumo mensal de agua em metros cúbicos: "))

    # classificação do tipo de imóvel
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")

    elif tipo_imovel == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")

    elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
        print("consumo moderado - dentro do padrao residencial.")

    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

# codigo final
except ValueError:
    print("Por favor, insira um valor numérico válido para o consumo de água.")