import Hello

def alphabet(ch):
    if ch>="a" and ch<='z'or ch>='A' and ch<="Z":
        print("its is an alphabet")
    else:
        print("Not a alphabet")
ch=input("String")
alphabet(ch)