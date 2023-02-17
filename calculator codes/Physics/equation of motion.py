# 1: s = v * t

# 2: Vf = Vi + a*t

# 3: s = Vi*t + (1/2)a*t^2

# 4: 2*a*s = Vf^2 - Vi^2


nv = int(input("Please enter the number of values which are given in the numerical problem: "))

#For two variable values
#CASE 1

if nv == 2:
    s = float(input("Please enter the value of distance(if value is not given write 0) : "))
    v = float(input("Please enter the value of speed(if value of speed is not gien write 0) :"))
    t = float(input("please enter the value of time(if time is not given write 0) :"))
    if s == 0:
        d = v * t
        print("distance covered by object is ",+d," m")
    if v == 0:
        v1 = s / t
        print("speed of the object is ",+v1," m/s")
    if t == 0:
        t1 = s / v
        print("Time is ",+t1," s")



#For 3 or more than 3 variables

elif nv >= 3:
    #FIVE VARIABLES

    s1 = float(input("Please enter the value of distance(if not given please write 0) : "))
    vi = float(input("please enter the value of initial speed(if not given please write 0) :"))
    t2 = float(input("please enter the value of time(if not gien please enter 0): "))
    a = float(input("please enter the value of acceleration(if not given please enter 0): "))
    vf = float(input("please enter the value of final speed(if not given please enter 0): "))
    #VARIABLE TO DETERMINE {DISTANCE = 0, TIME = 1, FINAL SPEED =2, ACCELERATION = 3, INITIAL SPEED = 4}
    vtd = int(input("please enter the value to determine: "))
    
    # if distance is to be determined
    #CASE 2

    if vtd == 0:
        if s1 == 0 and vf == 0 and vi !=0 and t2 !=0 and a !=0:
            d1 = vi * t2 + 0.5 * a * t2**2
            print("Distance covered by object is ",+d1," m")
        if s1 ==0 and t2 == 0 and a !=0 and vf !=0 and vi !=0:
             d2 =  (1 / (2* a)) * (vf**2 - vi**2)
             print("Distance covered by object is ",+d2," m")
             

    #if final speed is to be determined
    #CASE 3

    
    if vtd == 2:
        if s1 ==0 and vi != 0 and t2 != 0 and a != 0 and vf == 0:
           vf1 = vi + a * t2
           print("Final speed of object is ",+vf1," m/s")
        if t2 == 0 and vi !=0 and a != 0 and s1 !=0:
           vf2 = (2 * a * s1 + vi**2)**0.5
           print("Final speed of object is ",+vf2," m/s")

    #if time to be determined
    #CASE 4
    if vtd == 1:
        if t2 == 0 and s1 == 0 and a !=0 and vf != 0 and vi != 0:
            t3 = (vf - vi) / a
            print("Time required is ",+t3," s")
        if t2 == 0 and vf == 0 and a != 0 and vi != 0 and s1 != 0:
            t4 = (-2 * vi + (4 * vi**2 +8 * a * s1)**0.5) / 2 * a
            t5 = (-2 * vi - (4 * vi**2 +8 * a * s1)**0.5) / 2 * a
            print("Time required is ",+t4," or ",+t5," s")

    #if acceleration to be determined
    #CASE 5

    if vtd == 3:
        if s1 == 0 and a == 0 and vf != 0 and t2 != 0 and vi != 0:
            a1 = (vf - vi) / t2
            print("Acceleration of object is ",+a1," m/s^2")
        if a == 0 and vf == 0 and s1 != 0 and vi != 0 and t2 != 0:
            a2 = (2 * (s1 - vi * t2)) / t2**2
            print("Acceleration of object is ",+a2," m/s^2")
        if a == 0 and t2 == 0 and vi != 0 and vf != 0 and s1 != 0:
            a3 = (1 /(2 * s1)) * (vf**2 - vi**2)
            print("Acceleration of object is ",+a3," m/s^2")
    
    #if initial speed to be determined
    #CASE 6

    if vtd == 4:
        if s1 == 0 and vi == 0 and t2 != 0 and vf != 0 and a != 0:
            vi1 = vf - a * t2
            print("Initial speed of object is ",+vi1," m/s")
        if vi == 0 and vf == 0 and t2 != 0 and s1 != 0 and a != 0:
            vi2 = (1/t2) * (s1 - 0.5 * a * t2**2)
            print("Initial speed of object is ",+vi2," m/s")
        if vi == 0 and t2 == 0 and vf != 0 and a != 0 and s1 != 0:
            vi3 = (vf**2 - 2 * a * s1)**0.5
            print("Initial speed of object is ",+vi3," m/s")
    else:
        print("PLEASE ENTER A VALID CHOICE BETWEEN 2-4")
