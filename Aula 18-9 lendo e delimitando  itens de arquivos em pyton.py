import csv

f = csv.reader(open('iris.data'), delimiter=',')
Qtd = 0
for x in f:
    if '6.3' in x:
        Qtd = Qtd + 1
print(f.line_num,'Linhas lidas.')
print('O número total de ites é: ', Qtd)
print('fim')

#f = csv.reader(open('pasta1.csv'),delimiter=';')
#for (nome,nasc,fone) in f:
#    print('nome=%s nasc=%s fone=%s' % (nome,nasc,fone))

#print(f.line_num, 'linhas lidas')
#print('Fim.')

# %d = numeros inteiros
# %f = numeros rais
# %s = strings
