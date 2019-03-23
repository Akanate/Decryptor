
import cryptography.fernet as f

def main():
    print("Starting")
    choice = input("""
    1.Encrypt
    2.Decrypt
    Enter your choice: """)
    if choice == "1":
       encrypt()
    elif choice == "2":
       decrypt()
    else:
        print("Enter a valid choice")
        main()
def encrypt():
    print("Generating your key")
    where = input("Enter where you want to save your encryption key: ")
    key = f.Fernet.generate_key()
    d = open(where,"wb")
    d.write(key)
    d.close()
    print("Key saved to",where)
    print("Beggining encryption process")
    k = f.Fernet(key)
    #Starting encryption process
    what_file = input("Enter the file you want to encrypt: ")
    h = open(what_file,"rb")
    contents = h.read()
    crypt = k.encrypt(contents)
    h.close()
    h = open(what_file,"wb")
    h.write(crypt)
    print("Grandma did her job returning to main menu")
    main()

def decrypt():
    whatkey = input("Enter the file with your key in: ")
    g = open(whatkey,"rb")
    contents = g.read()
    k3 = f.Fernet(contents)
    g.close()
    decryptfile = input("Enter the file you want to decrypt: ")
    j = open(decryptfile,"rb")
    k1 = j.read()
    j.close()
    decrypted_file =k3.decrypt(k1)
    where_ = input("Where do you want to save the decryption: ")
    kd = open(where_,"a")
    decoded = decrypted_file.decode()
    kd.write(decoded)
    print("Saved to",where_)
    print("Grandma has decrypted your file")
    main()

def install():
   import os 
   try:
       print("Making sure all dependencies are installed")
       os.system("pip install fernet")
       os.system("pip install pycrypto")
       main()
   except:
       print("Not working exitting")
       exit()







install()
