#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install nmap")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TURKMAP")
print("""
TÜRK MAP Programına Hoş Geldiniz.

1) Hızlı Tarama
2) Servis ve Versiyon Bilgisi yaparak tarar
3) İşletim Sistemi Bilgisi
4) ip ve mac adresi gizleyerek tarama ve ayrıntılı  güvenlik duvarına yakalanmadan tarar
5) çok ayrıntılı tarama  güvenlik duvarına yakalanmadan tarar
6) açık taraması (ayrıntılı)


DİPNOT:nmap ta port taramasının kısayol versiyonu ;)
""")

islem = raw_input("İşlem Numarasını Girin: ")


if(islem=="1"):
	hedefip = raw_input("Hedef İp Girin: ")
	os.system("nmap " + hedefip)
elif(islem=="2"):
	hedefip = raw_input("Hedef İp Girin: ")
	os.system("nmap -sS -sV " + hedefip)
elif(islem=="3"):
	hedefip = raw_input("Hedef İp Girin: ")
	os.system("nmap -O " + hedefip)
elif(islem == "4"):
        hedefip = raw_input("Hedef İp Girin:")
        os.system("nmap --spoof-mac 0 -D 31.31.31.31 " + hedefip)
elif(islem == "5"):
        hedefip == raw_input("Hedef İp Girin:")
        os.system("nmap -vvv -T1 -p- " + hedefip) 


elif(islem == "6"):
         secenek = raw_input("açık taramasaı yapılırken ip ve mac gizlensinmi? Y/H :")
         if(secenek == "H" or secenek == "h"):
        
            os.system("clear")
            print("hangi servise yönelik brute force denesin")
            print("""
            1)ftp
            2)smtp
            3)telnet
            4)HTTP
            5)POP3       
            6)SMB
            7)MySQL
            8)Bütün servislere yapılsın
        

            """)
            print("-------------------------------")
            deger = raw_input("Değeri giriniz:")
            if(deger == "1"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=ftp-brute " + hedefip) 
            elif(deger == "2"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=smtp-brute " +  hedefip) 
            elif(deger == "3"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=telnet-brute " + hedefip) 
            elif(deger == "4"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=http-brute " + hedefip) 
            elif(deger == "5"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=pop3-brute " + hedefip) 
            elif(deger == "6"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=smb-brute " + hedefip) 
            elif(deger == "7"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=mysql-brute " + hedefip) 
            elif(deger == "8"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("figlet ftp")
                print("---------------------------------------------------------")
                os.system("nmap -vv --script vuln --script=ftp-brute " + hedefip) 
                os.system("figlet smtp")
                print("---------------------------------------------------------")
                os.system("nmap -vv --script vuln --script=smtp-brute " + hedefip) 
                os.system("figlet telnet")
                print("---------------------------------------------------------")
                os.system("nmap -vv --script vuln --script=telnet-brute " + hedefip) 
                os.system("figlet http")
                print("---------------------------------------------------------")
                os.system("nmap -vv --script vuln --script=http-brute " + hedefip) 
                os.system("figlet pop3")
                print("---------------------------------------------------------")
                os.system("nmap -vv --script vuln --script=pop3-brute " + hedefip) 
                os.system("figlet smb")
                print("---------------------------------------------------------")
                os.system("nmap -vv --script vuln --script=smb-brute " + hedefip) 
                os.system("figlet mysql")
                print("---------------------------------------------------------")
                os.system("nmap -vv --script vuln --script=mysql-brute " + hedefip) 
            else:
                 print("tekrar deneyin")
         elif(secenek == "Y" or secenek == "y"):
        
            os.system("clear")
            print("hangi servise yönelik brute force denesin")
            print("""
            1)ftp
            2)smtp
            3)telnet 
            4)HTTP
            5)POP3       
            6)SMB
            7)MySQL
            8)Bütün servislere yapılsın 
        

            """)
            print("------------------------------")
            deger = raw_input("Değeri giriniz:")
            if(deger == "1"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31 -vv --script vuln --script=ftp-brute " + hedefip) 
            elif(deger == "2"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=smtp-brute " +  hedefip) 
            elif(deger == "3"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=telnet-brute " + hedefip) 
            elif(deger == "4"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=http-brute " + hedefip) 
            elif(deger == "5"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=pop3-brute " + hedefip) 
            elif(deger == "6"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=smb-brute " + hedefip) 
          
            elif(deger == "7"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=mysql-brute " + hedefip) 
            elif(deger == "8"):
                hedefip = raw_input("Hedef İp Girin:")
                os.system("clear")
                os.system("figlet TARAMA BASLIYOR")
                os.system("figlet FTP")
                print("---------------------------------------------------------")
                os.system("nmap  --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=ftp-brute " + hedefip) 
                os.system("figlet SMTP")
                print("---------------------------------------------------------")
                os.system("nmap   --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=smtp-brute " + hedefip) 
                os.system("figlet TELNET")
                print("---------------------------------------------------------")
                os.system("nmap  --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=telnet-brute " + hedefip) 
                os.system("figlet HTTP")
                print("---------------------------------------------------------")
                os.system("nmap  --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=http-brute " + hedefip) 
                os.system("figlet POP3")
                print("---------------------------------------------------------")
                os.system("nmap  --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=pop3-brute " + hedefip) 
                os.system("figlet SMB")
                print("---------------------------------------------------------")
                os.system("nmap  --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=smb-brute " + hedefip) 
                os.system("figlet MYSQL")
                print("---------------------------------------------------------")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=mysql-brute " + hedefip) 
        
     

         else:
              print("kardeşim doğru düzgün bir değer gir yoksa çıkmak mı istiyorsun?Ctrl+c yap bunun içinde beni uğraştırma :D")
       





else:
	print("Hatalı Seçim Yaptınız. Program Kapatılıyor.")
