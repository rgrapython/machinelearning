###########################################################################
#              函数功能：定位目标ip的地址位置
#      地理库下载地址：https://dev.maxmind.com/geoip/geoip2/geolite2/
###########################################################################
import pygeoip
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def printRecord(tgt):
    try:
        #
    		rec = gi.record_by_name(tgt)
				city = rec['city']
				region = rec['region_name']
				country = rec['country_name']
				long = rec['logitude']
				lat = rec['latitude']
				print '[*] Target: ' + tgt + ' Geo-located. '
				print '[+] ' + str(city) + ', '+ str(region) + ', ' + str(country)
				print '[+] Latitude: ' + str(lat) + ', Longitude: ' + str(long)
		except Exception,e:
			print e
if __name__ == '__main__':
    tgt = '173.255.226.98'
    printRecord(tgt)