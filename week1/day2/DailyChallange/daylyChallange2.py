import datetime
birth_date = input("Enter your birth date DD/MM/YYYY: ")
b_day=birth_date.split("/")
b_day.reverse()
b_day=int("".join(b_day))
#print(b_day)
today = datetime.date.today()
date_as_int = int(today.strftime("%Y%m%d"))
#print(date_as_int)     
age = int((date_as_int - b_day) // 10000)
if age % 10==0:
    candles=10
    print('       ' + ('i'*candles))
else:
    candles=age%10
    _total=10-candles
    _left=_total//2
    _right=_total-_left
    total='       ' + ('_'*_left) + ('i'*candles) + ('_'*_right)
    print(total)
print("""      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
""")