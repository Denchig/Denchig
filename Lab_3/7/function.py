def transport(distance, time):
    if distance <= 100:
        if time <= 60:
            return "Please, choose a car"
        else:
            return "Please, choose a bus"
    else:
        if time <= 120:
           return "Please, choose an aircraft"
        else:
            return "Please, choose a train"  
        