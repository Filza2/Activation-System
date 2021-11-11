from requests import get,post
import json,re,socket
#CUS2HOST - FLGS,IP
#@TweakPY - @vv1ck


#v0.1
Tool_key=['Main','TweakPY','vv1ck']#Change that and put any keys You want 

Login_Reg=int(input("_____________\n1- Login\n2- New user\n> : "))
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
	s.connect(('google.com', 80))
	ip=s.getsockname()[0]
	s.close()
except:ip='N/A'		
if Login_Reg==1:
	try:
		CUID=get(f'https://leaked.wiki/r/{input("[?] Hosting ID : ")}.txt').text;CU_ID=CUID.split(':')[2];HOST_Key=CUID.split(':')[3];Order_Key=CUID.split(':')[4]
		if CU_ID==ip and HOST_Key in Tool_key:
			print(f'Done With Oreder ID {Order_Key}')
		else:exit('[!] Check Your Hosting Key and try Later .')
	except:exit('[!] Check Your Hosting Key and try Later.')
elif Login_Reg==2:
	print("[!] Note: Warning This information will be used for your next login")
	username=input("[+] username : ")
	password=input("[+] password : ")
	try:
		CU_LOC=get('http://ipinfo.io/json').json()['timezone']
		UUI_DHOST=('CUS')#Here Your Program Name
		CUS_Data=json.loads('{"username":"'+username+'","password":"'+password+'","CU-ID":"'+ip+'","CU-LOC":"'+CU_LOC+'","UUI-DHOST":"'+UUI_DHOST+'"}')
		req=post('https://leaked.wiki/paste',headers={'Host': 'leaked.wiki','Cookie': 'socials=yes','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type':'application/x-www-form-urlencoded','Content-Length': '16','Origin': 'https://leaked.wiki','Referer': 'https://leaked.wiki/paste','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Te': 'trailers','Connection': 'close'},data=f'pdata={CUS_Data}')
		id=re.findall('<script type="text/javascript"> location.href = "./p/(.*?)"; </script>',req.text)[0]
		print(f'[+] Order ID : {id}')
		print("[!] Note: Give this id to The Host")
	except:print("[!] Error Try Later !")
else:print('[-] Error ..')
