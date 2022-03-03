#Ex. Crie uma conversão de um valor em metros para cm e mm.

n = float(input('Digite o tamanho em metros:\n'))
cm = n*100
mm = n*1000
print(' O valor em cm é {} e em mm é {}'.format(cm, mm))    #Condições  (:.3f) Colocam 3 casas depois da vírgula.