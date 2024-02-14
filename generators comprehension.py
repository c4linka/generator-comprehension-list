"""
evenNumbers = [element
               for element in range(400)
               if element % 2 == 0
               ]

evenNumbersGenerator = (element
                        for element in range(400)
                        if element % 2 == 0
                        )

print(evenNumbers)

print(evenNumbersGenerator) # wypisze tylko -> <generator object <genexpr> at 0x101657f40>

for item in evenNumbersGenerator:
    print((item))

"""

#ZADANIE: zsumuj liczby od 2 do 100 podniesione do potegi 2


generator = (number**2 for number in range(2,101))



print(sum(generator)) #w kolejnosci po princie elementow generaro bedzie pusty, wynik = 0



for item in generator:  #wypisze elementy wygenerowane powyzej w generator tyle razy ile
    print(item)         #jest itemów, czyli jesli sie je wypisze czy uzyje w jakis inny sposob 
                        #wczesniej to bedzie pustow efekcie nie bedzie nic a nic ;)
                        #pętla wykona sie tyl razy - 0
#-----------------------------------------------------------------------------------------

    
