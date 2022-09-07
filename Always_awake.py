import mouse, time

events = mouse.record()


t0 = time.time()
i = 0
a = False
while ( not a):
    t1 = time.time()
    if (t1-t0) >= 60.0:
        mouse.play(events[:-1])
        t0 = t1
    a= mouse.is_pressed("left")

print("Finish")
