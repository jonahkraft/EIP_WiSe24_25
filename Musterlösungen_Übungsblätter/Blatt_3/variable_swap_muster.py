# Aufgabe 1:

# erst bekommt x den Wert von y zugewiesen und dann y den Wert von x. Da aber x zuvor den Wert von y zugewiesen bekommen
# hat, wird y der eigene Wert zugewiesen.


# Aufgabe 2:

x = 5
y = 15

h = x
x = y
y = h

print(f'x={x}, y={y}')
