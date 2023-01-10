class 차:
    def __init__(self, 바퀴, 가격): #객체 생성시 자동호출되는 메서드
        self.바퀴=바퀴  #self가 가리키는 객체공간에 
        #바퀴라는 변수를 만들고 메서드에서 넘겨준 바퀴값을 바인딩
        self.가격=가격

    def 정보(self):
        print(self.바퀴)
        print(self.가격)

car=차(2,1000)
print(car.바퀴)
print(car.가격)

class 자전차(차):
    def __init__(self,바퀴,가격,구동계):
        super().__init__(바퀴,가격) #부모클래스에서 넘겨받기
        #차.__init__(self,바퀴,가격)#차클래스에 생성자를 호출
        self.구동계=구동계

    def 정보(self):
        super().정보()  #부모클래스에서 가져오기
        print("구동계: ",self.구동계)  #메소드 오버라이드

bicycle=자전차(2,100,"시마노")
print(bicycle.구동계)

class 자동차(차):
    def __init__(self,바퀴,가격):
        super().__init__(바퀴,가격)
    
car=자동차(4,1000)
car.정보()

bicycle=자전차(2,100,"시마노")
bicycle.정보() 

class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")

나 = 자식()
나.호출()

#289
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

#291
f = open("C:\\Users\\User\\Desktop\\매수종목1.txt",mode="wt",\
    encoding="utf-8")

f.write("00005930\n")
f.write("00005220\n")
f.write("00005930")
f.close()

#292
a = open("C:\\Users\\User\\Desktop\\매수종목2.txt",mode="wt",\
    encoding="utf-8")

a.write("0059330 삼성전자\n")
a.write("005380 현대차\n")
a.write("035420 NAVER")
a.close()

#293
import csv
file = open("C:\\Users\\User\\Desktop\\매수종목2.csv",mode\
    ="wt", encoding="cp949",newline='')
writer=csv.writer(file)
writer.writerow([["종목명","종목코드","PER"]])
writer.writerow([["삼성전자","005930","15.59"]])
writer.writerow([["NAVER","035420","55.82"]])
file.close()

#294
f = open("C:\\Users\\User\\Desktop\\매수종목1.txt", \
    encoding="utf-8")
lines=f.readlines()
codes=[]
for line in lines:
    a = line.strip()
    codes.append(a)
print(lines)
f.close()

#295
a = open("C:\\Users\\User\\Desktop\\매수종목2.txt",\
    encoding="utf-8")
lines=a.readlines()
data={}
for line in lines:
    line=line.strip()
    k,v=line.split()
    print(k,v)
    data[k]=v

print(data)
a.close()
