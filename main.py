d = int(input("День: ")) # ввод числа дня
m = int(input('Месяц: ')) # ввод месяца
if m<1 or m>12: #проверка на правильность месяца 
    print("ошибка месяца")
elif d<1 or d>31: #проверка на правильность дня
    print("неправильный день")
else:
   if(m == 1 and d >= 1 and d <=31) or ( m == 2 and d <=31) or (m == 3 and d <=28): # условие при котором будет зима
       s = "Зима"
   elif(m == 3 and d >= 1 and d <=31) or ( m == 4 and d <= 30) or (m == 5 and d <=30): # условие при котором будет весна
       s = "Весна"
   elif (m == 6 and d >= 1 and d <=30) or (m == 7 and d <=31) or (m == 8 and d <= 31):# условие при котором будет лето
       s = "Лето"
   elif (m == 9 and d >= 1 and d <=30) or (m == 10 and d <= 31) or (m == 11 and d <=30):
       s = "Осень"
   print(f"дата {d}.{m} относится к {s}") #вывод если все правильно 
    
