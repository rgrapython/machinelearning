#########################################################################
#             函数功能：使用dpkt打印源ip->目的ip
#        dpkt下载地址：http://code.google.com/p/dpkt
#########################################################################
import dpkt
import socket
def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf) #2层数据
            ip = eth.data #3层数据
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print '[+] Src: ' + src + '--> Dst: ' + dst
         except:
            pass
def main():
    f = open('geotest.pcap')  #创建一个文件对象
    pcap = dpkt.pcap.Reader(f) #创建一个pcap.reader类的对象
    printPcap(pcap)

if __name__ == '__main__':
    main()
