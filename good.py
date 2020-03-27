from socket import*
import  theading 
def tname():
    print(theading.name())
    print("hello,this is a py file")
t=theading.Thead(target=tname)
print(theading.name())
