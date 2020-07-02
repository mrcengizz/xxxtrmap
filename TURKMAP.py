#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install nmap")
os.system("apt-get install figlet")

os.system("clear")
os.system("figlet TURKMAP")
print("""
TÜRK MAP Programına Hoş Geldiniz.
    
    
------------------------------------------------------
0)  Çıkmak için
1)  Hızlı Tarama
2)  Servis ve Versiyon Bilgisi yaparak tarar 
3)  İşletim Sistemi Bilgisi
4)  İp ve mac adresi gizleyerek tarama ve ayrıntılı  güvenlik duvarına yakalanmadan tarar
5)  Çok ayrıntılı tarama  güvenlik duvarına yakalanmadan tarar
6)  Açık taraması (ayrıntılı)(Brute-Force)
7)  Agresif Tarama
8)  Normal Tarama
9)  Syn tarama 
10) Udp tarama
11) Host up 
12) Giden paketleri takip eder
13) Ip adresinden Host name
------------------------------------------------------
01) Nikto web tarama ya geç
02) Gobuster'a geç(şuan yok)
DİPNOT:nmap ta port taramasının kısayol versiyonu (Nmap çakması) ;) TryHackMe vb.. bounty mounty vb.. 'de başarılar .D(geliştiriliyor)
""")

islem = raw_input("İşlem Numarasını Girin: ")

if(islem=="1"):
 
       os.system("figlet Hizli Tarama")
       hedefip = raw_input("Hedef İp Girin: ")
       os.system("nmap " + hedefip)
elif(islem == "0"):
     while True:
         print("Çıkış yapıldı.")
         break        
elif(islem == "01"):
        os.system("clear")
        os.system("apt-get install nikto")
        os.system("clear")
        os.system("figlet TURKMAP")
        print("""
        -----------------------------------------
        Nikto
        -----------------------------------------
        0)Çıkış yapmak için
        1)Temel Tarama
        2)Evasion kullanarak tarama
        3)Port Açık Tarama 
        4)Ssl desteği varsa ona göre tarama yapar
          4.1)ssl desteğinde port tarama
          4.2)ssl desteğinde ederek evasion tarama
 
         DİPNOT:nikto  taramasının kısayol versiyonu ;) TryHackMe vb.. bounty mounty vb.. 'de başarılar .D(geliştiriliyor)
         """)
        islem1 = raw_input("İşlem Numarasını Girin: ")
        if(islem1 == "1"):
            os.system("clear")
            os.system("figlet Hizli Tarama")
            domain = raw_input("Domain Girin: ")
            os.system("nikto -h  "+ domain)
        elif(islem1 == "0"):
                while True:
                    print("Çıkış yapıldı.")
                    break                
        elif(islem1 == "2"):
            os.system("clear")
            os.system("figlet Evasion Tarama ")
            domain = raw_input("Domain Girin: ")
            os.system("nikto -h  "+ domain + " -e 168")
        elif(islem1 == "3"):
            os.system("clear")
            os.system("figlet Port Acik Tarama")
            domain = raw_input("Domain Girin: ")  
            port = raw_input("Portları Giriniz(port yazıp boşluk bırakın)(Örnek:80 443): ")           
            os.system("nikto -h "+ domain + " -p " + port)    
        elif(islem1 == "4"):
            os.system("clear")
            os.system("figlet Destekli Tarama ")
            domain = raw_input("Domain Girin: ")
            os.system("nikto -h  "+ domain+ " -ssl")   
        elif(islem1 == "4.1"):  
            os.system("clear")
            os.system("figlet Destekli Tarama ")
            domain = raw_input("Domain Girin: ")
            port = raw_input("Portları Giriniz: ")            
            os.system("nikto -h "+ domain + " -p " + port)  
        elif(islem1 == "4.2"):
            os.system("clear")
            os.system("figlet Destekli Tarama ")
            domain = raw_input("Domain Girin: ")
            os.system("nikto -h  "+ domain+ " -e 168 -ssl")   
       
elif(islem == "9"):
        os.system("figlet syn scan")
        hedefip = raw_input("Hedef İp Girin: ")
        os.system("nmap -sS "+ hedefip)
elif(islem == "10"):
        os.system("figlet udp scan")
        hedefip = raw_input("Hedef İp Girin: ")
        os.system("nmap -sU "+ hedefip)  
elif(islem == "11"):
        os.system("figlet Host up")
        hedefip = raw_input("Hedef İp Girin: ")
        os.system("nmap -sP "+ hedefip)   
elif(islem == "12"):
        os.system("figlet Paket Nereye")
        hedefip = raw_input("Hedef İp Girin: ")
        os.system("nmap -traceroute "+ hedefip)  
elif(islem == "13"):
        os.system("figlet Reverse Look 0_= ")
        hedefip = raw_input("Hedef İp Girin: ")
        os.system("nmap -R "+ hedefip)             

elif(islem=="2"):
        os.system("figlet Servis Versiyon ")
	hedefip = raw_input("Hedef İp Girin: ")
        os.system("nmap -sS -sV " + hedefip)
       
elif(islem=="3"):
        os.system("figlet Isletim System Info ")
        hedefip = raw_input("Hedef İp Girin: ")
        os.system("nmap -O " + hedefip)
        
elif(islem == "4"):
        os.system("figlet Gizli Tarama ")
        hedefip = raw_input("Hedef İp Girin:")
        os.system("nmap --spoof-mac 0 -D 31.31.31.31 " + hedefip)
        
elif(islem == "5"):
        os.system("clear")
        os.system("figlet Seytan Ayrintida.. ;) ")
        hedefip == raw_input("Hedef İp Girin:")
        os.system("nmap -vvv -T1 -p- " + hedefip) 
elif(islem =="7"):
        os.system("clear")
        os.system("figlet Agresif Tarama")
        hedefip = raw_input("Hedef İp Girin:")
        os.system("nmap -A "+ hedefip)
elif(islem == "8"):
        os.system("clear")
        os.system("figlet Normal Tarama")
        hedefip == raw_input("Hedef İp Girin:")
        os.system("nmap -A -T5 -vv " + hedefip)         

elif(islem == "6"):
         secenek = raw_input("Açık taraması yapılırken ip ve mac gizlensinmi? Y/H :")
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
                os.system("figlet ftp ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=ftp-brute " + hedefip) 
            elif(deger == "2"):
                os.system("figlet smtp ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=smtp-brute " +  hedefip) 
            elif(deger == "3"):
                os.system("figlet telnet")     
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=telnet-brute " + hedefip) 
            elif(deger == "4"):
                os.system("figlet HTTP ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=http-brute " + hedefip) 
            elif(deger == "5"):
                os.system("figlet POP3 ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=pop3-brute " + hedefip) 
            elif(deger == "6"):
                os.system("figlet SMB ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=smb-brute " + hedefip) 
            elif(deger == "7"):
                os.system("figlet mysql ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap -vv --script vuln --script=mysql-brute " + hedefip) 
            elif(deger == "8"):
                os.system("figlet ALL SERVİCE ")
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
                 print("Tekrar Deneyin")
         elif(secenek == "Y" or secenek == "y"):
        
            os.system("clear")
            print("Hangi servise yönelik brute force denesin")
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
                os.system("figlet ftp ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31 -vv --script vuln --script=ftp-brute " + hedefip) 
            elif(deger == "2"):
                os.system("figlet smtp ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=smtp-brute " +  hedefip) 
            elif(deger == "3"):
                os.system("figlet telnet ")   
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=telnet-brute " + hedefip) 
            elif(deger == "4"):
                os.system("figlet HTTP ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=http-brute " + hedefip) 
            elif(deger == "5"):
                os.system("figlet POP3 ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=pop3-brute " + hedefip) 
            elif(deger == "6"):
                os.system("figlet SMB ")
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=smb-brute " + hedefip) 
          
            elif(deger == "7"):
                os.system("figlet mysql ")   
                hedefip = raw_input("Hedef İp Girin:")
                os.system("nmap --spoof-mac 0 -D 31.31.31.31  -vv --script vuln --script=mysql-brute " + hedefip) 
            elif(deger == "8"):
                os.system("figlet ALL service ")
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
       
elif(islem == "02"):
       print("Şuan bu sürümde yok güncellemeleri takip ediniz 0_=")


else:
	print("Hatalı Seçim Yaptınız. THE END.")
