krotka = [10,-3,4,9,12,-6,0]

najmniejsza = None
najwieksza = None
for i in krotka:
    if najmniejsza == None or najmniejsza > i: 
        najmniejsza = i
        
    if najwieksza == None or najwieksza < i:
        najwieksza = i
        
print ("najmniejsza liczba to:", najmniejsza)
print ("największa liczba to:", najwieksza)