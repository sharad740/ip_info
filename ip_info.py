import requests,subprocess
def my_information(Ip):
    my_info= eval(requests.get("http://ip-api.com/json/{}".format(Ip)).text)
    for s,x in my_info.items():
        if s != "status":
            print("[*]  {} ---> {}".format(str(s).ljust(10),str(x).ljust(30)))
def main():
    myip = subprocess.getoutput("curl -s ifconfig.me")
    if "curl:" not in myip:
        print("""
        ***********************************
        *   [ 1 ] For Own IP Address      *
        *   [ 2 ] For Victim IP Address   *
        *   [ 0 ] To Exit                 *
        ***********************************

        """)
        
        ip_info = input("[*] Select options [1/2]  > ")
        if ip_info=="1":
            my_information(myip)
        else:
            v_ip =input(" [#] What is Victim IP Address ?")
            my_information(v_ip)
    else:
        print("[Info] [This require Network Connection ]\n\tCheck your Connection and Try Again ....")
main()
