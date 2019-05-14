#coding=utf-8
#Author:Roger Date:2019/05/14
from scapy.all import *
def create_pks_512ips():
    try:
        keyvalue = {}
        keyvalue['https flood'] = (6, 24, 443)
        #keyvalue['http flood'] = (6, 24, 80)
        aaa = PcapWriter('d:\\0515.pcap', append=True, sync=True)
        i = 1
        #Query ip:http://ip.yqie.com/cn/guangdong/
        gdprovice_yd_ips = [('43.254.159.' + str(i)) for i in range(1,201)]
        gdprovice_nyd_ips = [('27.43.191.'+str(i)) for i in range(1,201)]
        uk_ips = [('2.20.183.' + str(i)) for i in range(1, 113)]
        ips_all = gdprovice_yd_ips + gdprovice_nyd_ips + uk_ips
        for ip in ips_all:
            src_ip = '27.45.167.100'
            dst_ip =  ip #ip from foshan of gd
            nexthop = '90.7.1.1'
            a = keyvalue[key][0]
            b = keyvalue[key][1]
            c = keyvalue[key][2]
            input = random.randint(1, 65535)
            output = random.randint(1, 65535)
            dpkts = 100
            dOctets = 10000

            pks = Ether(src='00:0C:29:31:3A:72', dst='00:0C:29:7A:00:D9') / IP(dst='10.242.39.6', src='10.10.10.10') / UDP(dport=9999, sport=3333) / NetflowHeader(
                version=5) / NetflowHeaderV5(count=1, sysUptime=7.00, unixSecs=1539751877, unixNanoSeconds=261158,
                                             flowSequence=9789, engineType=0, engineID=0) / NetflowRecordV5(
                src=src_ip, dst=dst_ip, nexthop=nexthop, input=input, output=output, dpkts=dpkts, dOctets=dOctets,
                tcpFlags=b, prot=a, srcport=c)
            aaa.write(pks)
                
            i += 1
            if i > 2000:
                break
            else:
                pass
    except Exception, e:
        print e
 
 
if __name__=='__main__':
    create_pks_512ips()
