import requests
from bs4 import BeautifulSoup
import wget
url = 'http://www.football-data.co.uk/englandm.php'
htm = requests.get(url).content
html = BeautifulSoup(htm,'html.parser')
for line in html.find_all('a'):
	if line.string == 'Premier League':
		downld = line.get('href')
		downld = 'http://www.football-data.co.uk/' + downld
		print (downld)
		wget.download(downld,out=downld[-11:-7]+'.csv')
