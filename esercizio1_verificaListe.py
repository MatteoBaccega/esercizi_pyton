citta= ["Roma", "Milano", "Torino", "Napoli"]
tmax=[31,28,35,34]
tmin=[15,10,12,18]
mediam=0
mediamin=0
for i in range(len(tmax)):
    mediam+=tmax[i]
    mediamin+=tmin[i]
mediam=mediam/len(tmax)
mediamin=mediamin/len(tmin)
print(f"La temperatura massima media è di {mediam}")
print(f"La temperatura minima media è di {mediamin}")
for i in range(len(citta)):
    if(tmin[i]<mediamin):
        print(f"La città di {citta[i]} ha la temperatura più bassa della media minima")
    else:
        print(f"La città di {citta[i]} ha la temperatura più alta della media minima")
#for i in range(len(citta)):
    #nomecitta=str(input("Inserire il nome di una città"))
    #print(nomecitta,citta[i])
    #print(nomecitta==citta[i])
    #if(nomecitta==citta[i]):
       # trovato=True
        #break
#print("Città esistente")
cittamax=""
tmaxc=0
cittamin=""
tminc=0
for i in range(len(tmax)):
    if(tmax[i]>tmaxc):
        tmaxc=tmax[i]
        cittamax=citta[i]
for i in range(len(tmin)):
    if(tmin[i]<tmaxc):
        tminc=tmin[i]
        cittamin=citta[i]
print(f"La citta più calda è {cittamax}")  
print(f"La citta più fredda è {cittamin}")  
