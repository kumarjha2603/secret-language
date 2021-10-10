import pickle
def NS(s):
    f=open("secret.dat","wb")
    pickle.dump(s,f)
    f.close()
    f=open("secret.dat","r")
    return f.read()
def SN(s):
    f=open("secret.dat","w")
    f.write(s)
    f.close()
    f=open("secret.dat","rb")
    c=pickle.load(f)
    return c

    
