waypoints = []
import numpy as np

while True:
    info = eval(input("Enter Info: "))
    x = info[0]
    y = info[1]
    waypoints = info[2]
    v = info[3]
    yaw = info[4]
    
    k = 0.5
                
                
    slope = (float(waypoints[-1][1])-float(waypoints[0][1])) / (float(waypoints[-1][0])-float(waypoints[0][0]))
    print("Slope = ", slope)
    a = -slope
    print("a = ", a)
    b=1
    print("b = ", b)
    c = slope * float(waypoints[0][0]) - float(waypoints[0][1])
    print("c = ", c)

    e = abs(a*x + b*y + c) / np.sqrt(a**2 + b**2)
    print("e = ", e)


    cross_track_error = np.arctan((k*e) / v)
    print("Cross Track Error = ", cross_track_error)
        
    heading_error = np.arctan2(y-float(waypoints[0][1]), x-float(waypoints[0][0])) - yaw
    print("Heading Error = ", heading_error)

    # Change the steer output with the lateral controller. 
    steer_angle  = cross_track_error + heading_error
    print("Steer Angle = ", steer_angle)
    if abs(steer_angle) < 1.22:
        steer_output = steer_angle
    elif steer_angle >= 1.22:
        steer_output = 1.22
    elif steer_angle <= -1.22:
        steer_output = -1.22
        
    print("Steer Output = ", steer_output)