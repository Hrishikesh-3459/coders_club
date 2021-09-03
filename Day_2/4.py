# Write a program which accepts coefficients of a quadratic equations from the user and displays the roots (both real and complex roots depending upon the discriminant)
a = int(input("Enter the first root: "))
b = int(input("Enter the second root: "))
c = int(input("Enter the third root: "))

dis = (b * b) - (4 * a * c)
sqr = abs(dis) ** (1/2)

if dis > 0: 
    print("Roots are real and distinct") 
    print((-b + sqr)/(2 * a)) 
    print((-b - sqr)/(2 * a)) 

elif dis == 0: 
    print(" Roots are real and repeated") 
    print(-b / (2 * a)) 

else:
    print("Roots are complex") 
    print(- b / (2 * a), " + i", sqr) 
    print(- b / (2 * a), " - i", sqr) 