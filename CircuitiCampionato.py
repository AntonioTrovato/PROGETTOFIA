from Circuito import Circuito

def mostraCircuiti():
    print("Circuiti del campionato")
    print("1."+str(Circuito(4318,9,7,71,1,33)))
    print("2."+str(Circuito(4381,14,5,70,0,33)))
    print("3."+str(Circuito(4567,12,5,66,0,33)))
    print("4."+str(Circuito(4655,16,6,66,1,33)))
    print("5."+str(Circuito(7004,19,6,44,0,33)))
    print("6."+str(Circuito(5793,7,10,53,0,33)))
    print("7."+str(Circuito(5848,9,10,53,2,78)))
    print("8."+str(Circuito(5148,15,7,60,0,22)))
    print("9."+str(Circuito(4684,4,7,66,0,22)))
    print("10."+str(Circuito(4318,9,7,71,1,33)))
    print("11."+str(Circuito(5338,6,9,58,2,33)))
    print("12."+str(Circuito(5769,23,8,57,0,33)))
    print("13."+str(Circuito(3543,11,3,87,1,87)))
    print("14."+str(Circuito(5554,21,10,55,2,88)))
    print("15."+str(Circuito(4567,12,5,66,0,33)))
    circuito = eval(input("Scegli circuito, 0 per concludere: "))
    if(circuito==0):
        exit(0)
    if(circuito==1):
        return Circuito(4318,9,7,71,1,33)
    if(circuito==2):
        return Circuito(4381,14,5,70,0,33)
    if(circuito==3):
        return Circuito(4567,12,5,66,0,33)
    if(circuito==4):
        return Circuito(4655,16,6,66,1,33)
    if(circuito==5):
        return Circuito(7004,19,6,44,0,33)
    if(circuito==6):
        return Circuito(5793,7,10,53,0,33)
    if(circuito==7):
        return Circuito(5848,9,10,53,2,78)
    if(circuito==8):
        return Circuito(5148,15,7,60,0,22)
    if(circuito==9):
        return Circuito(4684,4,7,66,0,22)
    if(circuito==10):
        return Circuito(4318,9,7,71,1,33)
    if(circuito==11):
        return Circuito(5338,6,9,58,2,33)
    if(circuito==12):
        return Circuito(5769,23,8,57,0,33)
    if(circuito==13):
        return Circuito(3543,11,3,87,1,87)
    if(circuito==14):
        return Circuito(5554,21,10,55,2,88)
    if(circuito==15):
        return Circuito(4567,12,5,66,0,33)
