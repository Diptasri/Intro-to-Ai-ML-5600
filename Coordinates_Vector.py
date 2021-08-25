
# inputs
a = float (input ("Enter a value: "))
b = float (input ("Enter b value: "))

# Internal division section formula
Px = ((a * a) + (b * b)) / (a + b)
Py = ((a * a) + (2 * a * b) - (b * b)) / (a + b)

# External division section formula
Qx = ((a * a) - (2 * a * b) - (b * b)) / (a - b)
Qy = ((a * a) + (b * b)) / (a - b)

# Final coordinates
internal_coordinates = (Px, Py)
external_coordinates = (Qx, Qy)

# Printing outputs
print ("(Px, Py) = " + str (internal_coordinates))
print ("(Qx, Qy) = " + str (external_coordinates))
