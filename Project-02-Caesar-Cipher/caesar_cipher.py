import datetime


# Caesar Cipher Functions


def encrypt(text, shift):
    result = ""

    for char in text:

        if char.isalpha():

            start = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char)-start+shift)%26+start)

        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:

        if char.isalpha():

            start = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char)-start-shift)%26+start)

        else:
            result += char

    return result


def save_history(action, original, result, shift):

    with open("history.txt","a") as file:

        file.write("="*60+"\n")
        file.write(str(datetime.datetime.now())+"\n")
        file.write("Action : "+action+"\n")
        file.write("Shift  : "+str(shift)+"\n")
        file.write("Input  : "+original+"\n")
        file.write("Output : "+result+"\n")
        file.write("="*60+"\n\n")


while True:

    print("\n"+"="*55)
    print("      CAESAR CIPHER TOOL")
    print("="*55)
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")
    print("="*55)

    choice=input("Select Option : ")

    if choice=="1":

        text=input("Enter Message : ")

        while True:

            try:
                shift=int(input("Enter Shift Key (1-25): "))

                if 1<=shift<=25:
                    break

                else:
                    print("Shift must be between 1 and 25.")

            except:
                print("Invalid Number.")

        encrypted=encrypt(text,shift)

        print("\nEncrypted Message")
        print(encrypted)

        save_history("Encryption",text,encrypted,shift)

        print("\nSaved to history.txt")

    elif choice=="2":

        text=input("Enter Encrypted Message : ")

        while True:

            try:

                shift=int(input("Enter Shift Key (1-25): "))

                if 1<=shift<=25:
                    break

                else:
                    print("Shift must be between 1 and 25.")

            except:
                print("Invalid Number.")

        decrypted=decrypt(text,shift)

        print("\nDecrypted Message")
        print(decrypted)

        save_history("Decryption",text,decrypted,shift)

        print("\nSaved to history.txt")

    elif choice=="3":

        print("\nThank You.")
        break

    else:

        print("\nInvalid Option.")