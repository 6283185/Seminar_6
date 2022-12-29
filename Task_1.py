# 1. Напишите программу вычисления арифметического
#  выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок,
#  меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

# a = [int(i) for i in input().split()]
str = '10+200*3'

lst = []
temp = ''
for i in range(len(str)):
    if str[i].isdigit():
        temp += str[i]
    else:
        lst.append(int(temp))
        lst.append(str[i])
        temp = ''
else:
    lst.append(int(temp))
print(lst) 

while '*' in lst or '/' in lst:
    mult = -1
    if '*' in lst:
        mult = lst.index('*')
    div = -1
    if '/' in lst:
        div = lst.index('/')
    
    if ((mult < div) and (mult != -1) and (div != -1)) or ((mult != -1) and (div == -1)):
        res = lst[mult - 1] * lst[mult + 1]
        lst = lst[:mult - 1] + [res] + lst[mult + 2:]
        
    elif (mult > div) and (div != -1) and (mult != -1) or (mult == -1 and div != -1):
        res = lst[div - 1] / lst[div + 1]
        lst = lst[:div - 1] + [res] + lst[div + 2:]
        
while '+' in lst or '-' in lst:
    addition = -1
    if '+' in lst:
        addition = lst.index('+')
    diff = -1
    if '-' in lst:
        div = lst.index('-')
    
    if ((addition < diff) and (addition != -1) and (diff != -1)) or ((addition != -1) and (diff == -1)):
        res = lst[addition - 1] + lst[addition + 1]
        lst = lst[:addition - 1] + [res] + lst[addition + 2:]
        
    elif (addition > diff) and (diff != -1) and (addition != -1) or (addition == -1 and diff != -1):
        res = lst[diff - 1] - lst[diff + 1]
        lst = lst[:diff - 1] + [res] + lst[diff + 2:]

print(lst)