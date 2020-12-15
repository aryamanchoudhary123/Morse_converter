code={
            "a":".- ", "b":"-... ", "c":"-.-. ", "d":"-.. ", "e":". ", "f":"..-. ",
            "g":"--. ", "h":".... ", "i":".. ", "j":".--- ", "k":"-.- ", "l":".-.. ",
            "m":"-- ", "n":"-. ", "o":"--- ", "p":".--. ", "q":"--.- ", "r":".-. ",
            "s":"... ", "t":"- ", "u":"..- ", "v":"...- ", "w":".-- ", "x":"-..- ",
            "y":"-.-- ", "z":"--.. "," ":" ","1":".---- ", "2":"..--- ", "3":"...-- ",
            "4":"....- ", "5":"..... ", "6":"-.... ", "7":"--... ", "8":"---.. ",
            "9":"----. ", "0":"----- ",
            }


def encode():
    msg=input("Enter the text to be converted to morse code : ")
    ans=""
    s=len(msg)
    

    for i in msg:
        ans= ans + code[i]

    print("The result is : " + ans)    
        

def decode():
    msg=input("Enter the morse code to be converted to English : ")
    msg=msg+" "
    ans=""
    ch=""
    for i in range(len(msg)):
        if(msg[i]!=" "):
            ch=ch+msg[i]

        elif(msg[i]==" " and msg[i-1]==" "):
            ch=""
            ans=ans+" "

        elif(msg[i]==" " and msg[i-1]!=" "):
            ch=ch+" "
            for e,m in code.items():
                if m==ch:
                    ans=ans+e
                    
            ch=""

    print("The decoded message is : "+ans)        

            
if __name__ == "__main__":

    while True :
        print("1.Encode Message ")
        print("2.Decode Message")
        print("3.Exit")
        print("Enter choice : ",end=" ")
        n=int(input())

        if(n == 1):
            encode()

        elif (n==2):
            decode()

        else :
            break
        

        print("Do you want to continue ?(y/n)")
        ans=input()

        if(ans=="n"):
            break
        
        else:
            continue










        
        
        
