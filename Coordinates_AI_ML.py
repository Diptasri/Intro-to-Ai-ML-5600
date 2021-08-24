

# inputs
a = float (input ("Enter a value: "))
b = float (input ("Enter b value: "))

if a>b :
    # Internal
    Px = ((a*a) + (b*b))/ (a+b)
    Py = ((a*a) + (2*a*b) - (b*b)) / (a+b)

    # External
    Qx = ((a*a) - (2*a*b) - (b*b)) / (a-b)
    Qy = ((a*a) + (b*b))/ (a-b)

    internal_coordinates = (Px, Py)
    external_coordinates = (Qx, Qy)

    # Output
    print (internal_coordinates)
    print (external_coordinates)

else :
    print ("a value must be greater than b ")