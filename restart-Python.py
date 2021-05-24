# print("신씨가 소리질렀다. \"도둑이야\".")
# print("naver", "kakao", "samsung", sep="/")
# print("first", end="/");print("second")
# print(5/3)

# 시가총액 = 298000000000000
# 현재가 = 5000
# PER = 15.79
# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))

# s = "hello"
# t = "python"
# print(s, t)
# print(s+"!", t)

# num_str = "720"
# num_int = int(num_str)
# print(num_int+1, type(num_int))

# letters = 'python'
# print(letters[0], letters[2])

# license_plate = "24가 2210"
# print(license_plate[-4:])

# string = "홀짝홀짝홀짝"
# print(string[0::2])

# string = "PYTHON"
# print(string[::-1])

# phone_number = "010-1111-2222"
# print(phone_number.replace("-", " "))
# print(phone_number.replace("-", ""))

# url = "http://sharebook.kr"
# print(url[-2::])

# url_split = url.split('.')
# print(url_split[1])

# lang = 'python'
# lang[0] = 'P'
# print(lang)

# string = 'abcd'
# string.replace('b', 'B')
# print(string)

# string = 'abcdfe2a354a32a'
# string = string.replace('a', 'A')
# print(string)

# print("-" * 80)

# t1 = 'python'
# t2 = 'java'
# t3 = t1 + ' ' + t2 + ' '
# print(t3 * 4)

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

# 상장주식수 = "5,969,782,550"
# a = int(상장주식수.replace(",", ""))
# print(a)

# 분기 = "2020/03(E) (IFRS연결)"

# data = "   삼성전자    "
# data1 = data.strip()
# print(data1)

# a = "hello"
# a = a.capitalize()
# print(a)

# file_name = "보고서.xlsx"
# isTrue = file_name.endswith("xlsx")
# print(isTrue)

# list = ["닥터 스트레인지", "스플릿", "럭키"]
# list.append("베트맨")
# list.insert(1, "슈퍼맨")

# del list[3]
# del list[2]
# del list[2]
# print(list)

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2

# nums = [1, 2, 3, 4, 5, 6, 7]

# print(max(nums))
# print(min(nums))
# print(sum(nums))

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# nums = [1, 2, 3, 4, 5]
# average = sum(nums) / len(nums)
# print(average)

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[0::2])
# print(nums[1::2])
# print(nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver']
# del interest[1]
# print(interest)

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("\n".join(interest))

# string = "삼성전자/LG전자/Naver"
# array = string.split("/")
# print(array)

# data = [2, 4, 3, 1, 5, 10, 9]
# # data.sort()
# # print(data)
# data2 = sorted(data)
# print(data2)

# my_variable = ()
# print(type(my_variable))

# movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
# print(movie_rank)

# my_tuple = (1,)
# print(type (my_tuple))

# data = tuple(range(2, 100, 2))
# print(data)

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, _ = scores
# print(valid_score)

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# # _, _, *valid_score = scores
# _, *valid_score, _ = scores
# print(valid_score)

# icd = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# print(icd)

# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# ice["죠쓰바"] = 1200
# ice["월드콘"] = 1500
# print(ice)
# print(ice["메로나"])

# inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
# print(inventory)

# inventory = {"메로나": [300, 20], 
#              "비비빅": [400, 3], 
#              "죠스바": [250, 100]}
# inventory["월드콘"] = [500, 7]
# print(inventory)
# print(inventory["메로나"][1], "원")

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice = list(icecream.keys())
# price = list(icecream.values())
# sumPrice = sum(icecream.values())
# print(ice)
# print(price)
# print(sumPrice)

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)
# print(icecream)

# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys, vals))
# print(result)

# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# result = dict(zip(date, close_price))
# print(result)

# print(type(True))
# user = input("입력:")
# print(user * 2)

# user = input("")
# if int(user) % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# amount = input("입력값 : ")
# if int(amount) + 20 > 255 :
#     print(255)
# else:
#     print(int(amount) + 20)

# amount = input("입력값 : ")
# num = int(amount) - 20
# if num <= 0 :
#     print(0)
# elif num > 255:
#     print(255)
# else:
#     print(num)

# time = input("현재 시간: ")
# if time[-2:] == "00":
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다")

# fruit = ["사과", "포도", "홍시"]
# f = input("좋아하는 과일은? ")
# if fruit[0] == f:
#     print("사과")
# elif fruit[1] == f:
#     print("포도")
# elif fruit[2] == f:
#     print("홍시")
# else:
#     print("없습니다.")

# fruit = ["사과", "포도", "홍시"]
# f = input("좋아하는 과일은? ")
# if f in fruit:
#     print("정답입니다")
# else:
#     print("없습니다.")

# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# i = input("투자 종목은 :")
# if i in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("좋아하는 과일은?")
# if user in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# user = input("문자: ")
# if user.islower():
#     print(user.upper())
# elif user.isupper():
#     print(user.lower())

# user = input("score : ")
# user = int(user)
# if 81 <= user <= 100:
#     print("grade is A")
# if 61 <= user <= 80:
#     print("grade is B")
# if 41 <= user <= 60:
#     print("grade is C")
# if 21 <= user <= 40:
#     print("grade is D")
# if 0 <= user <= 20:
#     print("grade is E")

# user = input("입력 : ")
# user2 = user.split(" ")
# won = int(user2[0])
# currency = user2[1]
# if currency == "달러":
#     print(won * 1167, "원")
# elif currency == "엔":
#     print(won * 1.096, "원")
# elif currency == "유로":
#     print(won * 1268, "원")
# elif currency == "위안":
#     print(won * 171, "원")

# 환율 = {"달러": 1167, 
#         "엔": 1.096, 
#         "유로": 1268, 
#         "위안": 171}
# user = input("입력: ")
# num, currency = user.split()
# print(float(num) * 환율[currency], "원")

# number1 = input("number1 : ")
# number2 = input("number2 : ")
# number3 = input("number3 : ")
# numlist = [number1, number2, number3]
# print(max(numlist))

# user = input("번호: ")
# num = user[0:3]
# 통신사 = {"011": "SKT", "016": "KT", "019": "LGU", "010": "알수없음"}
# com = 통신사[num]
# print(f"당신은 {com} 사용자입니다.")

# user = input("번호 : ")
# num = int(user[2:3:])
# if 0 <= num and num <= 2:
#     print("강북구")
# elif 3 <= num and num <= 5:
#     print("도봉구")
# elif 6 <= num and num <= 9:
#     print("노원구")

# user = input("번호 :")
# num = user.split("-")[1]
# if 0 <= int(num[1:3]) <= 8:
#     print("서울")
# else:
#     print("x")

# user = input("번호 : ")
# num1 = user.split("-")[0]
# num2 = user.split("-")[1]
# print(num1)
# print(num2)
# result = int(num1[0]) * 2 + int(num1[1]) * 3 + int(num1[2]) * 4 + \
#     int(num1[3]) * 5 + int(num1[4]) * 6 + int(num1[5]) * 7 + \
#     int(num2[0]) * 8 + int(num2[1]) * 9 + int(num2[2]) * 2 + \
#     int(num2[3]) * 3 + int(num2[4]) * 4 + int(num2[5]) * 5
# print(result)
# result2 = 11 - (result % 11)
# print(result2)
# print(num2[-1])
# if result2 == int(num2[-1]):
#     print("유효")
# else:
#     print("x")

# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])

# if (시가+변동폭) > 최고가:
#     print("상승장")
# else:
#     print("하락장")

# 리스트 = ["A", "b", "c", "D"]
# for 변수 in 리스트:
#     if 변수.isupper():
#         print(변수)

# for i in list(range(2002, 2050, 4)):
#     print(i)

# for i in range(100):
#     print(99 - i)

# for num in range(10):
#     print(num / 10)

# for i in range(1, 10):
#     print(3, "x", i, " = ", 3 * i)
# for i in range(1, 10):
#     print(3, "x", i, " = ", 3 * i)

# for i in range(1, 10):
#     if i % 2 != 0:
#         print(3, "x", i, " = ", 3 * i)

# sum = 0
# for i in range(1, 11):
#     if i % 2 != 0:
#         sum += i
# print(sum)

# gob = 1
# for i in range(1, 11):
#     gob *= i
# print(gob)

# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(i, price_list[i])

# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list) - 1):
#     print(my_list[i], my_list[i+1])

# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list) - 2):
#     print(my_list[i], my_list[i+1], my_list[i+2])

# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list) - 1):
#     print(my_list[-i-1], my_list[-i-2])

# stock = {"시가": [100, 200, 300], "종가": [80, 210, 330]}

# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)):
#     print(apart[i][0], "호")
#     print(apart[i][1], "호")

# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart[::-1]:
#     for col in row[::-1]:
#         print(col, "호")

# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for i in data:
#     sub = []
#     for col in i:
#         sub.append(col * 1.00014)
#     result.append(sub)
# print(result)

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#     if row[3] > 150:
#         print(row[3])

# def print_coin():
#     print("비트코인")

# for i in range(100):
#     print_coin()

# def print_with_smile(str):
#     print(str + ":D")

# print_with_smile("ss")

# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}

# def print_value_by_key(my_dict, key):
#     print(my_dict[key])
# print_value_by_key(my_dict, "10/26")

# def print_5xn(line, n):
#     chunk_num = int(len(line) / n)
#     for x in range(chunk_num + 1):
#         print(line[x * n: x * n + n])
# print_5xn("아이엠어보이유알어", 3)

# def calc_monthly_salary(salary):
#     month = int(salary / 12)
#     return month
# print(calc_monthly_salary(100000000))

# def make_url(string) :
#     url = "www." + string + ".com"
#     return url
# print(make_url("naver"))

# def pickup_even(items):
#     result = []
#     for item in items:
#         if item % 2 == 0:
#             result.append(item)
#     return result

# re = pickup_even([3, 4, 5, 6, 7, 8])

# print(re)

# def convert_int(str):
#     return int(str.replace(",", ""))

# print(convert_int("1,234,567"))

# now = datetime.datetime.now()
# print(now, type(now))

# for day in range(5, 0, -1):
#     delta = datetime.timedelta(days=day)
#     date = now - delta
#     print(date)
# import datetime
# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))
# import time
# import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self):
#         print(self.name)
#         print(self.age)
#         print(self.sex)
# areum = Human("아름", 25, "여자")
# areum.who()

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def __del__(self):
#         print("나의 죽음을 알리지마라")

#     def who(self):
#         print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("아름", 25, "여자")
# del(areum)

# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#     def set_name(self, name):
#         self.name = name
# stock = Stock(None, None)
# stock.set_name("삼성전자")
# print(stock.name)

# import random

# class Account:

#     account_count = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_number = num1 + '-' + num2 + '-' + num3

#         Account.account_count += 1
    
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
# kim = Account("김민수", 100)
# print(kim.name)
# print(kim.balance)
# print(kim.bank)
# print(kim.account_number)
# print(Account.account_count)
# kim.get_account_num()

# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
# class 자전차(차):
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
    
# bicycle = 자전차(2, 100)
# print(bicycle.가격)

class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")


나 = 자식()
나.호출()
