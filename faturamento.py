
estados = ["SP", "RJ", "MG", "ES", "Outros"]
faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]


total_faturamento = 0
for valor in faturamento:
    total_faturamento += valor  


print("Percentual de representação por estado:")
for i in range(len(estados)):
    percentual = (faturamento[i] / total_faturamento) * 100  
    print(estados[i] + ": " + str(round(percentual, 2)) + "%")  
