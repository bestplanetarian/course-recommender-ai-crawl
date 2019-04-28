from selenium import webdriver
#你要去安装这个
from selenium.webdriver.support.ui import Select
import time
import mysql.connector
import random



mydb=mysql.connector.connect(
      host="3.16.54.143",
      user="root",
      password="12345678",
      database="Capstone3000"
)


mydatabase = mydb.cursor()


global w

browser = webdriver.Chrome(executable_path='/Users/ShiqiWang/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.6/chromedriver')
#这个取决于你自己浏览器的内核，如果报错说明你电脑里没有driver，你需要去下载，然后配置

browser.get('https://myzou.missouri.edu/psp/csprdc/?cmd=login&languageCd=ENG')


username = browser.find_element_by_id("userid")
password = browser.find_element_by_id("pwd")

username.send_keys("swz45")
password.send_keys("Dota2009")

browser.find_element_by_name("Submit").click()


browser.get('https://myzou.missouri.edu/psc/csprdc/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.CLASS_SEARCH.GBL?Page=SSR_CLSRCH_ENTRY&Action=U&ExactKeys=Y&TargetFrameName=None&&')

subject = Select(browser.find_element_by_id("SSR_CLSRCH_WRK_SUBJECT_SRCH$0"))
career  = Select(browser.find_element_by_id("SSR_CLSRCH_WRK_ACAD_CAREER$2"))

print ("The number of majors:" ,len(subject.options));

print ("The number of available careeris :", len(career.options));

def subjectforloop():
    for y in range(0, len(subject.options)):
      if subject.options[y].text == "Physics":
         return y
         break
def careerforloop():
    for z in range(0, len(career.options)):
      if career.options[z].text == "Undergraduate":
         return z
         break

h = subjectforloop()
k = careerforloop()
print(h)
print(k)

#print(career.options[5].text);
       


subject.options[h].click()
#这个是课程的选项，从1到不知道多少
career.options[k].click()
#这个是难度的选项，4还是5好像是undergraduate

browser.find_element_by_name("CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH").click()


#这里要停3秒，不一定三秒，但是要等跳转
time.sleep(5)
browser.find_element_by_name("#ICSave").click()
time.sleep(20)

coursenumber = []; 
coursesection = [];
coursedate = [];
courseroom = [];
courseteacher = [];
courseduration = [];
coursename = [];
coursecredit = [];
courseGPA = [];
classname = [];
xuefen = 0
#coursecredit.append(xuefen)

#let me try using the pointer to solve this question.
#/parent::div/parent::div
#does not work

#name = browser.find_element_by_xpath('//a[@id="MTG_CLASS_NBR$7"]//ancestor::table[@class="PABACKGROUNDINVISIBLEWBO"]/tbody/tr/td[@class="PAGROUPBOXLABELLEVEL1"]')
#print(name.text)
#print(coursetag)
#parent2 = parent1.find_element_by_xpath(".//parent::div")
#print(coursetag)
classname = browser.find_elements_by_class_name('PAGROUPBOXLABELLEVEL1')
#print(classname.text)




#def findclassnameonindex1(i):
#    math1 = browser.find_element_by_xpath('//a[@id="MTG_CLASS_NBR$'+str(i)+'"]//ancestor::table[@class="PABACKGROUNDINVISIBLEWBO"]/tbody/tr/td[@class="PAGROUPBOXLABELLEVEL1"]')
#    return math1

#def findclassnameonindex2(j):
#    math2 = browser.find_element_by_xpath('//a[@id="MTG_CLASS_NBR$'+str(j)+'"]//ancestor::table[@class="PABACKGROUNDINVISIBLEWBO"]/tbody/tr/td[@class="PAGROUPBOXLABELLEVEL1"]')
#    return math2




def findingsession():
    w=0
    for k in range (0, 900):
        try:
           browser.find_element_by_id('MTG_CLASS_NBR$'+str(k)).is_displayed() 
        except:
           break
        else:
           w=w+1
    return w





v=findingsession()
print(v)




                   


for j in range (0,v):
    #o = j+1
    name1=browser.find_element_by_xpath('//a[@id="MTG_CLASS_NBR$'+str(j)+'"]//ancestor::table[@class="PABACKGROUNDINVISIBLEWBO"]/tbody/tr/td[@class="PAGROUPBOXLABELLEVEL1"]')
    #print(name1.text)
    coursename.append(name1)
    #classname1=findclassnameonindex1(v)
    #classname2=findclassnameonindex2(v+1)
    #if classname1==clasname2:
    #   coursecredit.append(xuefen)
    #else:
    #   xuefen = random.randint(2,5)
    #   coursecredit.append(xuefen)
    
   
    if coursename.count(name1) == 1:
       xuefen = random.randint(1,5)
       coursecredit.append(xuefen)
       number = browser.find_element_by_id('MTG_CLASS_NBR$'+str(j))
       section = browser.find_element_by_id('MTG_CLASSNAME$'+str(j))
       date = browser.find_element_by_id('MTG_DAYTIME$'+str(j))
       room = browser.find_element_by_id('MTG_ROOM$'+str(j))
       gpa=round(random.uniform(2.5, 4.0),1)
       try:
        browser.find_element_by_id('UM_SB389$span$'+str(j)).is_displayed()
       except:
        teacher = browser.find_element_by_id('UM_SB389$'+str(j))
       else:
        teacher = browser.find_element_by_id('UM_SB389$span$'+str(j))
      
       Duration = browser.find_element_by_id('MTG_TOPIC$'+str(j))
       coursenumber.append(number)
       coursesection.append(section)
       coursedate.append(date)
       courseroom.append(room)
       courseteacher.append(teacher)
       courseduration.append(Duration)
       courseGPA.append(gpa)
       classname.append(name1)
    #print(coursename[j].text, coursenumber[j].text, coursesection[j].text, courseroom[j].text, coursedate[j].text, courseteacher[j].text, courseduration[j].text, coursecredit[j],courseGPA[j])


for course in range (0, 21):
    var=(coursenumber[course].text, coursesection[course].text, coursedate[course].text, courseduration[course].text, courseteacher[course].text,courseroom[course].text, classname[course].text, courseGPA[course], coursecredit[course]) 
    sql = "INSERT INTO Course(courseID,section, days, coursetime, instructor, room, CourseName, GPA, Credit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mydatabase.execute(sql, var)
    mydb.commit()
    print(mydatabase.rowcount, "record inserted")
    #print(classname[y].text)
    #coursename.append(classname)
    
    


       
#coursename.append(classname[0])
#print(classname[1].text)
#for y in range (0, 28):
    #sql = "INSERT INTO Course(courseName) VALUES (%s)"
    #mydatabase.execute(sql, var)
    #mydb.commit()
    #print(mydatabase.rowcount, "record inserted")
    #print(classname[y].text)
    #coursename.append(classname)
   
    




 

    







