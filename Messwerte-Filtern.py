""" Name: Messwerte filtern
### Version: 1.0.0
### Autor: Alexander Holzenkamp
### Datum: 10.09.2024
### Änderungen:
### Messwerte mit append hinzugefügt,
### Liste sortiert und Werte gelöscht,
### Mittelwert gebildet und gerundet,
### Programm auf funktion geprüft
"""

#Liste mit Messwerten in Celcius
messwerte = []
messwerte.append (15.2)
messwerte.append (13.5)
messwerte.append (13.6)
messwerte.append (14.7)
messwerte.append (16.9)
messwerte.append (14.8)
messwerte.append (17.8)
messwerte.append (14.9)
messwerte.append (16.4)
messwerte.append (15.0)

#Liste sortieren und Messwerte löschen
messwerte.sort()
kleinster_wert = min(messwerte)
groesster_wert = max(messwerte)

messwerte.remove(kleinster_wert)
messwerte.remove(groesster_wert)

#Mittelwert bilden und zahlen runden
mittelwert = sum(messwerte) /len(messwerte)
mittelwert= round(mittelwert)
print("Der Temperatur beträgt", mittelwert ,"Grad Celcius +- 0,3")

