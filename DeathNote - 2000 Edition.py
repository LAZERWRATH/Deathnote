import ast, os, pyperclip
from time import sleep
from sys import stdout
from copy import deepcopy
from random import randint

settingz = ["FP", "TTP"]
def importkeypairs():
    keypairgen()
    

def keypairgen():
    print("Generating Keypairs...")
    List1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
    List2 = deepcopy(List1)
    Dict1 = {}
    for i in range(0,26):
        L1 = randint(0,len(List1)-1)
        L2 = randint(0,len(List2)-1)
        L1a = List1[L1]
        L2a = List2[L2]
        Dict1[(List1[L1])] = List2[L2]
        List1.remove(L1a)
        List2.remove(L2a)
    sets = open("KeypairsRAND", "w")
    sets.write(str(Dict1))
    sets.close()
    print("Keypairs Generated")
    clear()
def wait():
    PENIS = input(print_str("Press Enter To Continue... "))
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_str(string):
    if settings["FP"] == "Y":
        for i in range(len(string)):
            sleep(settings["TTP"])
            stdout.write(string[i])
            stdout.flush()
    else:
        print(string)
    return ""
def defaults():
    global settings
    settings = {
                "FP" : "Y", #FancyPrints
                "TTP" : 0.05, #TimeToPrint
                }
def save_settings():
    global settings
    sets = open("Settings.txt", "r+")
    sets.write(str(settings))
    sets.close()
def load_settings():
    sets = open("Settings.txt", "r+")
    global settings
    settings = ast.literal_eval(sets.read())
    sets.close()
def load_keypairs():
    global encode
    global decode
    sets = open("Keypairs.txt", "r+")
    encode = ast.literal_eval(sets.read())
    sets.close()
    sets = open("Depairs.txt", "r+")
    decode = ast.literal_eval(sets.read())
    sets.close()
load_keypairs()
load_settings()
def setting():
    clear()
    for i in settings:
        print_str("{:^10} : {:^4}".format(i, settings[i])) #Fancy Printing;    Y
        print("")
    x = input(print_str("What Setting Would You Like To Change? "))
    if x == "defaults":
        defaults()
    else:
        settings[x] = input(print_str("From {} to ".format(settings[x])))
def check_keys(str, dict):
    for i in str:
        #print i
        if i in dict:
            pass
        else:
            print_str("{} is unsupported".format(i))
            print("")
            return False
class value(object):
    def __init__(self, value):
        self.value = value
close = False
while close != True:
    clear()
    request = input(print_str("What Would You Like To Do? "))
    clear()
    if request == "help":
        breaK = False
        help = open("Documentation/help.txt", "r+")
        print_str(help.read())
        while breaK == False:
            request = input(print_str("What Would You Like To Know More About? "))
            request = open("Documentation/{}.txt".format(request), "r+")
            print_str(request.read())
            request.close()
            request = raw_input(print_str("Would You Like To Know About Anything Else? (Y/N) "))
            if request.upper() == "N":
                breaK = True
        help.close()
    if request == "settings":
        setting()
        save_settings()
    if request == "keypairs":
        load_keypairs()
    if request == "encrypt":
        string = input(print_str("Enter String To Encode "))
        if string == "":
            string = pyperclip.paste()
        string = string.upper()
        if check_keys(string, encode) != False:
            encoded = ""
            for i in string:
                encoded = encoded + encode[i]
            print_str(encoded)
            pyperclip.copy(encoded)
            print("")
            wait()
            clear()
        else:
            wait()
            clear()
    if request == "decrypt":
        string = input(print_str("Enter String To Decode "))
        if string == "":
            string = pyperclip.paste()
        string = string.upper()
        if check_keys(string, decode) != False:
            decoded = ""
            for i in string:
                decoded = decoded + decode[i]
            print_str(decoded)
            pyperclip.copy(decoded)
            print("")
            wait()
            clear()
        else:
            wait()
            clear()
    if request == "file encrypt":
        string = input(print_str("Enter Filename To Encrypt "))
        sets = open("Files/{}".format(string), "r+")
        string = sets.read().upper()
        sets.close()
        if check_keys(string, encode) != False:
            encoded = ""
            for i in string:
                encoded = encoded + encode[i]
            sets = open("Files/Encrypted.txt", "w")
            sets.write(encoded)
            sets.close()
            clear()
        else:
            wait()
            clear()
    if request == "file decrypt":
        string = input(print_str("Enter Filename To Decrypt "))
        sets = open("Files/{}".format(string), "r+")
        string = sets.read().upper()
        sets.close()
        if check_keys(string, decode) != False:
            decoded = ""
            for i in string:
                decoded = decoded + decode[i]
            sets = open("Files/Decrypted.txt", "w")
            sets.write(decoded)
            sets.close()
            clear()
        else:
            wait()
            clear()
    if request == "exit":
        clear()
        top_eye =       "{cunt:^80}".format(cunt="  ,-''-.  ")
        midtop_eye =    "{cunt:^80}".format(cunt=" / ,--. \ ")
        mid_eye =       "{cunt:^80}".format(cunt="| ( () ) |")
        midbot_eye =    "{cunt:^80}".format(cunt=" \ `--' / ")
        bot_eye =       "{cunt:^80}".format(cunt="  `-..-'  ")
        for i in range(0,6):
            if i < 1: print(top_eye)
            else: print("")
            if i < 2: print(midtop_eye)
            else: print("")
            if i < 3: print(mid_eye)
            else: print ("")
            if i < 4: print(midbot_eye)
            else: print("")
            if i < 5: print(bot_eye)
            else: print("")
            if i == 5: print("{cunt:^80}".format(cunt="Goodbye"))
            if i < 5: sleep(0.5)
            else: sleep(1)
            clear()
        close = True
