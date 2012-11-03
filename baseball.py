import urllib2
from BeautifulSoup import BeautifulSoup

class Pass:
    def __init__(self,url):
        self.url_text = urllib2.urlopen(url).read()
        decode = self.url_text.decode("utf-8","replace")


    def base(self):
        soup = BeautifulSoup(self.url_text)
        self.retrunt = soup
        self.left = soup.findAll(attrs={"class":"teams"} )
        self.right = soup.findAll(attrs={"class":"SPscore SPlineR"} )

    def text(self):
        soup = BeautifulSoup(self.left)
        soup.re_left = soup.findAll(attrs = {"class":"score_r"})
        self.re_right = soup.findAll(attrs = {"class" : "strong"})
        
        
    def prettify(self):
        pre = BeautifulSoup(self.url_text)
        self.prett = pre.prettify()


        
    
pas = Pass("http://baseball.yahoo.co.jp/npb/schedule/?&date=20120801")
pas.base()
"""print pas.prett"""
##print pas.left
##print pas.right

oneday= pas.retrunt.findAll(attrs = {"class":"LinkCenter"})
print oneday[0].text
##leagueŽæ“¾


print "-----------"
for i in pas.left:
    li = i
    lli =  li.findAll(attrs = {"class":"score_r"})
    tlli = li.findAll(attrs = {"class":"yjMS bb"})
    tlli2 = li.findAll(attrs = {"class":"yjMS bt bb"})
    
    tili3 = li.findAll("em")
    count = li.findAll("td" , colspan="2")
    for counts in count:
        print counts.text
        
    for em in tili3:
        print em.text
    
    for tii in tlli:
        print tii.text

    for tii2 in tlli2:
        print tii2.text
        
    for ii in lli:
        print ii.text
    print "----------------"

##pas.text()




"""for r in pas.re_left:
    ri = r
    print ri
    
##print 
##print li.text
##print ri.text
"""
