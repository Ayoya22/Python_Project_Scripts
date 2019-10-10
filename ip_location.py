import re
import sys
import urllib2
import BeautifulSoup4

usage = "Run the script: ./geolocate.py IPAddress"

if len(sys.argv)!=2:
    print(usage)
    sys.exit(0)

if len(sys.argv) > 1:
    ipaddr = sys.argv[1]