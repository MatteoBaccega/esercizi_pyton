f=int(input("Quante fascine vuoi comprare"))
s=int(input("Quanti sacchi vuoi comprare"))
b=int(input("Quanti bancali vuoi comprare"))
ptot=f*5+s*20+b*50
print("Il peso totale della legna è di:",ptot)
prtot=ptot*0.8
print("Il prezzo totale della legna è di:",prtot)
if(ptot>100):
  ps=(ptot/100)*15
  print("lo sconto applicato è di:",ps)
else:
  print("non hai lo sconto")
  ps=0
print("Le spese di trasporto sono di 3 euro")
prezzototale=(prtot-ps)+3
print("Il prezzo finale è di:",prezzototale)
