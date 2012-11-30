# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import re


class Pass:
    def __init__(self,url):
        self.url_text = urllib2.urlopen(url).read()
        self.decode = self.url_text.decode("utf-8")


    def game_type(self):
        soup =  BeautifulSoup(self.url_text)
        self.type = soup.findAll(attrs = {"class":"NpbScore clearFix"})
        self.un_type =  unicode(self.type[0])
        un_type_text = self.type[0].text
        if self.un_type.find("NpbCl yjMSt") != -1:
            print u"ペナントレース"
            return 1
        elif self.un_type.find("NpbIl yjMSt") != -1:
            self.another_game_sp = soup.findAll(attrs = {"class":"NpbSP"})
            self.another_game_cl = soup.findAll(attrs = {"class":"cm1 cl"})
            self.another_game_c2 = soup.findAll(attrs = {"class":"cm2 cl"})
            self.another_game_te = soup.findAll(attrs = {"class":"teams"})
            sp =  len(self.another_game_sp )
            self.c1 = len(self.another_game_cl)
            c2 = len(self.another_game_c2)
            te = len(self.another_game_te)

            if ((self.c1 != 0 )or(c2 != 0)):
                print u"クライマックスシリーズ"
                return 4
            elif sp != 0:
                ##NpbIl yjMStの中をパースしてみる
                find_NpbIl = soup.findAll(attrs={"class":"NpbIl yjMSt"})
                encode_NpbIl = find_NpbIl[0].text.encode("UTF-8")
                if encode_NpbIl.find('\xe6\x97\xa5\xe6\x9c\xac\xe3\x82\xb7\xe3\x83\xaa\xe3\x83\xbc\xe3\x82\xba') != -1:
                    print u"日本シリーズ"
                    return 5
                
                else:
                    print u"オールスター"
                    return 3
            else:
                print u"交流戦"
                return 1
 
   
    def normal(self):
        soup = BeautifulSoup(self.url_text)
        self.retrunt = soup
        self.teams = soup.findAll(attrs={"class":"teams"} )
        for main_html in self.teams:
            scores =  main_html.findAll(attrs = {"class":"score_r"})
            teams_l = main_html.findAll(attrs = {"class":"yjMS bb"})
            teams_r = main_html.findAll(attrs = {"class":"yjMS bt bb"})
            
            time = main_html.findAll("em")
            count = main_html.findAll("td" , colspan="2")
            for counts in count:
                print counts.text
                
            for em in time:
                print em.text
            
            for t_left in teams_l:
                print t_left.text

            for t_right in teams_r:
                print t_right.text
                
            for score in scores:
                print score.text
            print "----------------------------"
    
    def allstar(self):
        soup = BeautifulSoup(self.url_text)
        self.retrunt = soup
        self.teams = soup.findAll(attrs={"class":"NpbSP"} )        
        for main_html in self.teams:
            score_l =  main_html.findAll(attrs = {"class":"SPscore SPlineL"})
            score_r = main_html.findAll(attrs = {"class":"SPscore SPlineR"})
            teams_l = main_html.findAll(attrs = {"class":"NpbSPPl"})
            teams_r = main_html.findAll(attrs = {"class":"NpbSPCl"})
            
            start_time = main_html.findAll("em")
            count = main_html.findAll("td" , colspan="2")
            for counts in count:
                print counts.text
                
            for em in start_time:
                print em.text
            
            print score_l[0]
            print score_r[0]
                
            print lli_l[0].text
            print lli_r[0].text
            

    def cl_series(self):
        soup = BeautifulSoup(self.url_text)
        self.retrunt = soup
        if (self.c1 != 0):
            self.teams = soup.findAll(attrs={"class":"cm1 cl"} )
        else:
            self.teams = soup.findAll(attrs={"class":"cm2 cl"} )
            self.teams.append(soup.findAll(attrs={"class":"cm2 pl"} )[0])
            
        for main_html in self.teams:
            scores =  main_html.findAll(attrs = {"class":"score_r"})
            teams_l = main_html.findAll(attrs = {"class":"yjM bt bb"})
            teams_r = main_html.findAll(attrs = {"class":"yjM bb"})
            
            time = main_html.findAll("em")
            count = main_html.findAll("td" , colspan="2")
            
            for counts in count:
                print counts.text
                
            for em in time:
                print em.text
            
            for score in scores:
                print score.text
                
            print teams_l[0].text

            print teams_r[0].text
            
            print "----------------------------"
  
    def japan_series(self):
        soup = BeautifulSoup(self.url_text)
        self.retrunt = soup
        self.teams = soup.findAll(attrs={"class":"NpbSP"} )

        for main_html in self.teams:
            team_text = unicode(main_html)
            ##left
            team_l_1 = team_text.find("pnSP") + 11
            team_l_2 = team_text[team_l_1:]
            team_l_3 = team_l_2.find("</i>")

            team_name_l = team_l_2[:team_l_3]
            
            
            ##right
            team_r_1 = team_l_2.find("pnSP")+ 11
            team_r_2 = team_l_2[team_r_1:]
            team_r_3 = team_r_2.find("</i>")

            team_name_r = team_r_2[:team_r_3 ]
            
            score_l =  main_html.findAll(attrs = {"class":"SPscore SPlineL"})
            score_r =  main_html.findAll(attrs = {"class":"SPscore SPlineR"})

            time = main_html.findAll("em")
            count = main_html.findAll("td" , colspan="2")

            
            
            for counts in count:
                print counts.text
                
            for em in time:
                print em.text
            
            print team_name_l
            print team_name_r
            print score_l[0].text        
            print score_r[0].text
        
    def text(self):
        soup = BeautifulSoup(self.teams)
        soup.re_left = soup.findAll(attrs = {"class":"score_r"})
        self.re_right = soup.findAll(attrs = {"class" : "strong"})

    
        
    def prettify(self):
        pre = BeautifulSoup(self.url_text)
        self.prett = pre.prettify()


        
    
pas = Pass("http://baseball.yahoo.co.jp/npb/schedule/?series=1&series=2&")


flag = pas.game_type()

if flag ==1 :
    pas.normal()
elif flag == 3:
    pas.allstar()
elif flag == 4:
    pas.cl_series()
else:
    pas.japan_series()
    


print "-----------"

