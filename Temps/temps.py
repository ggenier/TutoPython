# -*-coding:Latin-1 -*
import time
import datetime

debut = time.time()
time.sleep(1)
fin = time.time()

print("Heure de debut {}".format(debut))
print("Heure de fin {}".format(fin))

if debut < fin:
    print("debut avant fin")

print("Temps d'écart {}".format(fin-debut))

date_heure = time.localtime()
print(date_heure)
print("Nous sommes le {} {} {}, il est {}:{}:{}".format(date_heure.tm_mday, date_heure.tm_mon, date_heure.tm_year, date_heure.tm_hour, date_heure.tm_min, date_heure.tm_sec))

print("\nheure debut +50")
date_heure = time.localtime(debut+50)
print(date_heure)
print("Nous sommes le {} {} {}, il est {}:{}:{}".format(date_heure.tm_mday, date_heure.tm_mon, date_heure.tm_year, date_heure.tm_hour, date_heure.tm_min, date_heure.tm_sec))

print("\nFormattage heure avec strftime")
print(time.strftime("%A %d %B %Y %H:%M:%S semaine %U"))

print("\nJuste une date")
date=datetime.date.today()
print(date)

print("\nJuste une heure")
heure=datetime.time(12, 11, 45)
print(heure)

print("\nDate et heure")
dateHeure=datetime.datetime.now()
print(dateHeure)