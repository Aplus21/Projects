import mouse, time

events = mouse.record() 
#Records everything that the mouse do until the right click is pressed

#Set time 0 for the first time
t0 = time.time()

#a will change it value when left click is executed
a = False

while ( not a):
    t1 = time.time()
    if (t1-t0) >= 60.0:
        mouse.play(events[:-1])
        t0 = t1
    a= mouse.is_pressed("left")

print("Finish")
