import matplotlib.pyplot as plt
# inputs
a = float (input ("Enter a value: "))
b = float (input ("Enter b value: "))

ax = a + b
ay = a - b

bx = a - b
by = a + b

# Internal division section formula
Px = ((a * a) + (b * b)) / (a + b)
Py = ((a * a) + (2 * a * b) - (b * b)) / (a + b)

# External division section formula
Qx = ((a * a) - (2 * a * b) - (b * b)) / (a - b)
Qy = ((a * a) + (b * b)) / (a - b)

plt.figure(1)
plt.scatter([ax, bx, Px], [ay, by, Py], color= 'r')
plt.text(ax, ay + 0.5, '({},{})'.format(ax, ay))
plt.text(bx, by + 0.5, '({},{})'.format(bx, by))
plt.text(Px, Py + 0.5, '({},{})'.format(Px, Py))
plt.plot([ax, bx, Px], [ay, by, Py])
plt.title("Internal Division Section")
plt.xlabel("X- Axis")
plt.ylabel("Y- Axis")
plt.grid(True)
plt.show()

plt.figure(2)
plt.scatter([ax, bx, Qx], [ay, by, Qy], color= 'r')
plt.text(ax, ay + 0.5, '({},{})'.format(ax, ay))
plt.text(bx, by + 0.5, '({},{})'.format(bx, by))
plt.text(Qx, Qy + 0.5, '({},{})'.format(Qx, Qy))
plt.plot([ax, bx, Qx], [ay, by, Qy])
plt.title("External Division Section")
plt.xlabel("X- Axis")
plt.ylabel("Y- Axis")
plt.grid(True)
plt.show()




# Final coordinates
internal_coordinates = (Px, Py)
external_coordinates = (Qx, Qy)

# Printing outputs
print ("(Px, Py) = " + str (internal_coordinates))
print ("(Qx, Qy) = " + str (external_coordinates))
