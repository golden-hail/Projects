def calculate_final_speed(initial_speed, inclinations):
    cur_speed = initial_speed
    for seg in inclinations:
        if seg < 0:  
            seg = abs(seg)
            cur_speed = cur_speed + seg
        elif seg > 0:
            cur_speed = cur_speed - seg
        else:
            continue
        
        if cur_speed <= 0:
            return 0
        
    return cur_speed

print(calculate_final_speed(60, [0, 30, 0, -45, 0]))

