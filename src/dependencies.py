
def type_of_exercise(weight: str, height: str, ageInput: str, selection: str):
    if selection == "sedentary":
        return float((13.397*(float(weight))+ 4.799*(float(height)) - 5.677*(float(ageInput)) + 88.362)* 1.2)
    elif selection == "light":
        return float((13.397*(float(weight))+ 4.799*(float(height)) - 5.677*(float(ageInput)) + 88.362)*1.35)
    elif selection == "moderate:":
        return float((13.397*(float(weight))+ 4.799*(float(height)) - 5.677*(float(ageInput)) + 88.362)*1.55)
    elif selection == "heavy":
        return float((13.397*(float(weight))+ 4.799*(float(height)) - 5.677*(float(ageInput)) + 88.362)*1.7)
    elif selection == "very":
        return float((13.397*(float(weight))+ 4.799*(float(height)) - 5.677*(float(ageInput)) + 88.362)*1.9)

def bmi(weight: str, height: str):
    return ((float(weight)/(float(height)**2))*10000) 

def bmi_2(weight: str, height: str):
    if bmi(float(float(weight)), float(float(height))) < 18.5:
        return("You are Underfloat(weight)")
    elif bmi(float(weight), float(height)) < 24.9:
        return("You have a normal body mass index")
    elif bmi(float(weight), float(height)) < 29.9:
        return("You are Overfloat(weight)")
    elif bmi(float(weight), float(height)) > 29.91:
        return("You are Obese")

