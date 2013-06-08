for x in range(1000):
    for y in range(1000):
        for z in range(1000):
            if x + y + z == 1000 and x < y < z  and x**2 + y**2 == z**2:
                print x,y,z
                print x*y*z
