from collections import Counter
raodenoba = int(input()) #რაოდენობის განმსაზღვრელი ცვლადი
l = [] 
for i in range(raodenoba):  #ციკლი დატრიალდება იმდენჯერ, რამდენიც იქნება ცვლადი  raodenoba - ის მნიშვბელობა მეორე ხაზზე.
    l.append(input()) # l - List ში ამატებს append ის მეშვეობით.
c = Counter(l) # ითვლის შეტანილ მონაცემებს (მაგალითად თუ ჩვენ ორჯერ შევიტანთ abcd - ს  Counter - ს ექნება შემდეგი ფორმატი -- Counter({'abcd':2}))
print(len(c)) # გამოაქვს პირველ ხაზზე და ითვლის თუ რამდენი ელემენტია Counter - ის Dictionary - ში
for i in c.values(): 
    print(i, end = ' ') # გამოგვაქვს მეორე ხაზზე საბოლოო მნიშვნელობები 
