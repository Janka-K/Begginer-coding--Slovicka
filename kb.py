from requests_html import HTMLSession
from unidecode import unidecode 
import smtplib
from email.mime.text import MIMEText


session= HTMLSession()
stranka = session.get("https://kb.jobs.cz/volna-mista/?fulltext=&customcateg%5B%5D=analyza_dat&prefid_location_hier%5B%5D=R200000")

pozice = stranka.html.find("#positionTable")
zahlavi = '<html><body>'
zapati = '</table></body></html>'
oddelovac = '<table id="positionTable" data-url="https://kb.jobs.cz/volna-mista/volna-mista-ajax/">'
tabulka_mezera = '<table cellpadding="20" cellspacing = "10" border = "2" id="positionTable" data-url="https://kb.jobs.cz/volna-mista/volna-mista-ajax/">'
web = stranka.html.html.split(oddelovac)[1].split('</table>')
web_stranka = zahlavi + tabulka_mezera + web[0] + zapati 


"""stranka.html.render(sleep = 5)

kb = stranka.html.find(".cse-name")
pvztah = stranka.html.find(".cse-contract")
zamestnani = [mista.text for mista in kb]
zamestnani1 = ",".join([misto for misto in zamestnani])
puvazek = [uvazek.text for uvazek in pvztah]
puvazek1 = ",".join([uvazek for uvazek in puvazek])"""


#msg= MIMEText(f"Zaměstnání:{zamestnani1}\nÚvazek : {puvazek1}")
msg = MIMEText(web_stranka,'html')
msg['Subject'] = 'Kb kariera'
msg['From'] = 'JanaKorycanova@kariera.cz'
msg['To'] = 'info@janadev.cz'
s = smtplib.SMTP('smtp.web4u.cz', 587)
s.login("info@janadev.cz", 'qp4jqwwo')
s.sendmail(msg['From'],msg['To'],msg.as_string())





