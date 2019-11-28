#!/usr/bin/python

import os
import sys, traceback


if os.getuid() != 0:
	print "Sorry. This script requires sudo privledges"
	sys.exit()
def main():
	try:
		print ('''

 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  \033[1;36mKali linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |
 \033[1;36m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| V2.0 \033[1;m


 \033[1;32m+ -- -- +=[ Author: LionSec | Homepage: www.neodrix.com\033[1;m
 \033[1;32m+ -- -- +=[ Editor: FSystem88 | https://github.com/FSystem88 \033[1;m
 
 \033[1;31m+ -- -- +=[ PROBABLY THIS PROGRAM WILL BREAK YOUR UNIX \033[1;m


\033[1;91m[W] Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem .\033[1;m
		''')
		def inicio1():
			while True:
				print ('''
1) Add Kali repositories & Update 
2) Install all programs
3) Install classicmenu indicator
4) Install Kali menu
5) Remove all kali linux repositories
			''')

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")
			
				if opcion0 == "1":
					cmd1 = os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
					cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
					cmd3 = os.system("apt-get update -m")
				elif opcion0 == "2":
					cmd = os.system("apt-get -f install acccheck ace-voip amap  braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry  dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter  golismero goofile lbd  masscan metagoofil  nmap p0f parsero recon-ng set smtp-user-enum snmpcheck  sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark  xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant  jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner  sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey  wifite apache-users arachni bbqsql  burpsuite cutycapt davtest  dirb dirbuster  funkload  jboss-autopwn joomscan jsql  padbuster paros parsero plecost   recon-ng skipfish sqlmap sqlninja sqlsus  uniscan  webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp  httptunnel  nishang polenum powersploit pwnat ridenum sbd  webshells weevely casefile cutycapt dos2unix dradis keepnote  metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester  set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager  p0f pdf-parser pdfid  peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd  crunch  gpp-decrypt hash-identifier  john johnny   maskprocessor  ncrack oclgausscrack pack patator polenum  rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
				elif opcion0 == "3":
					print (''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

''')
					repo = raw_input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
						cmd = os.system("sudo apt-get install classicmenu-indicator")
				elif opcion0 == "4":
					repo = raw_input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("apt-get install kali-menu")
				elif opcion0 == "5":
					infile = "/etc/apt/sources.list"
					outfile = "/etc/apt/sources.list"
					delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
					fin = open(infile)
					os.remove("/etc/apt/sources.list")
					fout = open(outfile, "w+")
					for line in fin:
					    for word in delete_list:
					        line = line.replace(word, "")
					    fout.write(line)
					fin.close()
					fout.close()
					print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
