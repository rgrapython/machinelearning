#########################################################################
#             函数功能：使用python画谷歌地球
#         谷歌地球图形化展示攻击源到攻击目的的攻击流量
#########################################################################
import dpkt
import socket
import pygeoip
import optparse

gi = pygeoip.GeoIP("/opt/GeoIP/Geo.dat")

def retKML(ip):
    try:
         rec = gi.record_by_name(ip)
         longitude = rec['longitude']
         latitude = rec['latitude']
         kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<point>\n'
            '</Placemark>\n'
          )%(ip, longitude, latitude)
          return kml
     except Exception,e:
        print e
        return ""
    
def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf) #2层数据
            ip = eth.data #3层数据
            src = socket.inet_ntoa(ip.src)
            srcKML = retKML(src)
            dst = socket.inet_ntoa(ip.dst)
            dstKML = retKML(dst)
            kmlPts = kmlPts + srcKML + dstKML
         except:
            pass
def main():
    parser = optparse.OptionParser('usage%prog -p <pcap file>')
    parser.add_option('-p', dest='pcapFile', type='string', help='specify pcap filename')
    (options, args) = parser.parse_args()
    if options.pcapFile == None:
        print parser.usage
        exit(0)
    pcapFile = options.pcapFile
    f = open(pcapFile)  #创建一个文件对象
    pcap = dpkt.pcap.Reader(f) #创建一个pcap.reader类的对象
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?>\
      \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'
    kmlfooter = '</Document>\n</kml>\n'
    kmldoc = kmlheader + plotIPs(pcap) + kmlfooter
    print kmldoc

if __name__ == '__main__':
    main()
