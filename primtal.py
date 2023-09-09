#Johan Eskils

import math

print('Funktionen hittar de primtal som finns i intervallet n till 99 och returnerar dem som en lista "true"')
print('\n   true = primtal(n)\n\n')
print('n anges som ett heltal i intervallet 2 - 99')

def primtal(n):

    if n < 2 or n > 99:
        print(f'Angivet n = {n} är inte ett tal i intervallet 2 till 99')
        exit()

    false = []
    true = []


    for i in range(2,n+1,1):

        #2 är det enda jämna heltalet som är ett primtal

        if i%2 == 0 and i == 2:
            true.append(i)

        #markera alla övriga heltal i valt intervall som false

        if i%2 == 0 and i > 2:
            if i not in false:
                false.append(i)

        #kontrollera ifall ett tal är ett primtal och ifall en multipler finns\
        # i intervallet markera den som false innan primtal läggs som true


        if i%2 != 0:
            for j in range(i,n+1,i):
                for k in range(2,n+1,1):
                    if j == k*i:
                        if j not in false:
                            false.append(j)
                            if i not in true:
                                true.append(i)

        #Hitta de övriga primtal i intervallet som inte har några multipler i intervallet\
        # markera 

        if i%2 !=0 and i not in false:
            for k in range(2,n+1,1):
                if i*k > n:
                    if i not in true:
                        true.append(i)

    return true

true = primtal(99)

print("_____")
print(true)