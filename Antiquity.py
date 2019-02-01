from datetime import date
from math import floor
loop=True
while loop:
    userDate = input("Insira a data que pertende avaliar; 0 - Sair\n")
    if userDate == '0':
        loop = False
    else:
        userDate = userDate.split('-')
        today = date.today()

        for i in range(len(userDate)):
            userDate[i] = int(userDate[i])

        try:
            initialDate = date(userDate[2], userDate[1], userDate[0])
            
        except:
            print("A data introduzida não é válida")

        print("A antiguidade desta pessoa é:\n")

        days = today - initialDate
        days = days.days
        years = floor(days/365)
        days -= years*365
        month = floor(days/30)
        days -= month*30

        print(str(years), 'Anos ', str(month), 'Meses ', str(days), 'Dias\n')


