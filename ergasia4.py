# dwse dyo arithmous kai praxeis
number1, operation, number2, junk= input("dwse praxi").split('(')
#emfanizei tis lexeis pou edwse o xrhsths
print (number1,operation,number2)
#synarthsh allaghs lexewn se arithmous
def wordstonumber(lexi):
 if  lexi=="zero":
    lexi=0
 if lexi=="one":
    lexi=1
 if lexi=="two":
    lexi=2
 if lexi=="three":
    lexi=3
 if lexi=="four":
    lexi=4
 if lexi=="five":
    lexi=5
 if lexi=="six":
    lexi=6
 if lexi=="seven":
    lexi=7
 if lexi=="eight":
    lexi=8
 if lexi=="nine":
    lexi=9
 return lexi
numb1=wordstonumber(number1)
numb2=wordstonumber(number2)
#elegxos eidos praxis kai ektypwsh apotelesmatos
if operation == "plus":
    print (numb1+numb2)
elif operation=="minus":
    print (numb1-numb2)
elif operation=="times":
    print (numb1*numb2)
elif operation=="modulo" and numb2==0:
       print("Den orizetai h diairesh")
else:print(numb1%numb2)
