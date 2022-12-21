from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
from xml.etree.ElementTree import parse
import xmltodict
from json.decoder import JSONDecoder
from os import error
import glob

data = []

page = 1
url = "http://openapi.work.go.kr/opi/opi/opia/wantedApi.do"
key = "WNLB0BQ31I58AQ2YDZ4ET2VR1HK"
occupation = "&occupation=023|024|025|026"

for page in range(1,11):
    queryParams =  '?' + urlencode({quote_plus('authKey') : 'WNLB0BQ31I58AQ2YDZ4ET2VR1HK', quote_plus('callTp'): 'L', quote_plus('returnType'): 'XML',quote_plus('startPage'): page, quote_plus('display'): '200',
                                    quote_plus('occupation'): '023|024|025|026'})



    request = urllib.request.Request(url + unquote(queryParams))

    response_body = urlopen(request, timeout=60).read() # get bytes data


    decode_data = response_body.decode('utf-8')
    print(type(decode_data))

    xml_parse = xmltodict.parse(decode_data)# string인 xml 파싱
    xml_dict = json.loads(json.dumps(xml_parse))

    print(xml_dict)
    with open('job' +str(page) + '.json', 'w') as f:
        json.dump(xml_dict, f)

for f in glob.glob("job*.json"):
    with open(f, encoding="utf-8") as infile:
        data.append(json.load(infile))

with open("job.json",'w', encoding="utf-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent="\t")

#http post 통신 코드
# headers = {}
# headers = {'content-type': 'application/json'}
# postData = xml_dict
# response = requests.post("https://test.com", headers=headers, data=postData)
