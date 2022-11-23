valls = {'I': 1, 'V': 5,'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
d = list(input())
res = []
for i in d:
    for key, value in enumerate(valls):
        if i == key:
            print('t')
        else:
            print('r')
#print(res)



#for i in s:
 #   i =
##ПРОДОЛЖИТЬ ЧЕРЕЗ КЛЮЧ-ЗНАЧЕНИЕ ДЛЯ САМИХ РИМСКИХ ЦИФР

