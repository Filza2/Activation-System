from requests import get,post
import re
#HOST2CUS - FLGS,IP
#@TweakPY - @vv1ck

#v0.1

Host_Key='TweakPY'#Change that and put any keys You want 

Order_id=input("[/] Enter Order ID : ")
CA_D=get(f'https://leaked.wiki/r/{Order_id}.txt').text
if 'CU-ID' in CA_D:
	CU_user=re.findall("'username': '(.*?)'",CA_D)[0];CU_pass=re.findall("'password': '(.*?)'",CA_D)[0];CU_ID=re.findall("'CU-ID': '(.*?)'",CA_D)[0];CU_LOC=re.findall("'CU-LOC': '(.*?)'",CA_D)[0];CU_UUIDHOST=re.findall("'UUI-DHOST': '(.*?)'",CA_D)[0]
	print("\n[$] CU - information - One Active\n")
	print('[§] CU-user: ',CU_user)
	print('[§] CU-pass',CU_pass)
	print('[§] CU-ID: ',CU_ID)
	print('-----------------------\n[§] CU-LOC: ',CU_LOC)
	print('[§] CU-UUIDHOST: ',CU_UUIDHOST)
	print("\n[$] CU - information - One Active\n")
	YN=input('\n[?] Active For This User [N/y] : ')
	if YN=='N':exit('[/] This Order have been cancelled <\> .')
	elif YN=='y':
		CU_Key=CU_user+':'+CU_pass+':'+CU_ID+':'+Host_Key+':'+Order_id
		req=post('https://leaked.wiki/paste',headers={'Host': 'leaked.wiki','Cookie': 'socials=yes','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type':'application/x-www-form-urlencoded','Content-Length': '16','Origin': 'https://leaked.wiki','Referer': 'https://leaked.wiki/paste','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Te': 'trailers','Connection': 'close'},data=f'pdata={CU_Key}')
		id=re.findall('<script type="text/javascript"> location.href = "./p/(.*?)"; </script>',req.text)[0]
		print(f'[+] Hosting ID : {id}')
	else:exit('[#] ~ [N/y] only ~')
else:exit('[!] invalid Order ID !')

