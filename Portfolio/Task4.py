import sys
import urllib.request

Address = sys.argv[1:]
website = Address[0]
statusCode = urllib.request.urlopen(website).getcode

if statusCode != 200:
    print("it is down")
else:
    print("it is up")




