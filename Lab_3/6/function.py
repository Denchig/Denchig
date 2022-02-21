def weather(temp, nature):
    if temp <= 10:
        if nature == "wind":
            return "Please, put on a coat"
        else:
            return "Please, put on a jacket"
    else:
        if nature == "wind":
           return "Please, put on a hoodie"
        else:
            return "Please, put on a T-shirt"  
        