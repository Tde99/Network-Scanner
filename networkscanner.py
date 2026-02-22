import scapy.all as scapy
import optparse

#netdiscover yaptığını yaptık gibi
def start():#önceki gibi aynı muhabbet burda
    netw = optparse.OptionParser()
    netw.add_option("-i", "--ip" , dest = "ip_address", help = " you can use-i or --ip_address " )
    (userinput,arguments) = netw.parse_args()

    if not userinput.ip_address:#ip girilmezse uyarı
        print("Please enter IP address")

    return userinput
def network(ip):#bir arp dosyası gönderir ağdaki tüm cihazlara ve onlardan mac adreslerini alır
    request_package = scapy.ARP(pdst = ip)#bir arp isteği oluşturur ve Sana verdiğim ip adresi kimdeyse bana MAC adresini söylesin içeren bir pakettr
    # scapy.ls(scapy.ARP())
    broadcast_package = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")#bu paketin herkese gitmesi gerektğini duyurur
    #scapy.ls(scapy.Ether())
    package = broadcast_package/request_package #iki katmanı birleştirir yani herkese gönderilecek bir arp isteği vardır
    (reel_package, invalid_package)= scapy.srp(package,timeout = 1)
    reel_package.summary()#Gelen cevapların kısa bir özetini (Hangi IP'den hangi MAC adresi geldi) ekrana basar.
user_input = start()
network(user_input.ip_address)
#invalid_package =Cevap vermeyenlerin listesidir.
#reel_package: Cevap veren (canlı) cihazların olduğu listedir.
#timeout = 1: Eğer 1 saniye içinde cevap gelmezse beklemeyi bırakır.
#srp() (Send and Receive Packets): Paketi gönderir ve gelen cevapları bekler.