receita = {}
despesas = 0
mes = ''
total = 0
restante = 0
sobrou = 0

while True:
    print('Controle de Gastos')
    print('Digite o mês e o quanto gastou ou digite "sair" para sair')
    mes = input('Digite o mês: ')
    if mes == 'sair':
        break
    despesas = float(input('Digite o quanto gastou: '))
    if despesas == 0:
        break
    receita[mes] = despesas

print(receita)
print(f'Total de despesas: {sum(receita.values()):.2f} ')
print(f'Mês que mais gastou: {max(receita, key=receita.get)}')
print(f'Mês que menos gastou: {min(receita, key=receita.get)}')

print('Deseja fazer o cálculo de quanto sobrou? S/N')
resp = input().upper()
if resp == 'S':
    total = float(input('Digite o capital inicial: '))
    total_gasto = sum(receita.values())
    sobrou = total - total_gasto
    print(f'Sobrou: {sobrou:.2f}')
elif resp == 'N':
    print('Encerrando o programa...')
    continuar = False
else:
    print('Opção inválida. Encerrando o programa...')
    continuar = False