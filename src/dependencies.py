
def type_of_exercise(weight: float, height: float, ageInput: float, selection: str):
    if selection == "sedentary":
        return float((13.397*(weight)+ 4.799*(height) - 5.677*(ageInput) + 88.362)* 1.2)
    elif selection == "light":
        return float((13.397*(weight)+ 4.799*(height) - 5.677*(ageInput) + 88.362)*1.35)
    elif selection == "moderate:":
        return float((13.397*(weight)+ 4.799*(height) - 5.677*(ageInput) + 88.362)*1.55)
    elif selection == "heavy":
        return float((13.397*(weight)+ 4.799*(height) - 5.677*(ageInput) + 88.362)*1.7)
    elif selection == "very":
        return float((13.397*(weight)+ 4.799*(height) - 5.677*(ageInput) + 88.362)*1.9)

def bmi(weight: float, height: float):
    return ((weight/(height**2))*10000) 

def bmi_2(weight: float, height: float):
    if bmi(weight, height) < 18.5:
        return("You are Underweight")
    elif bmi(weight, height) < 24.9:
        return("You have a normal body mass index")
    elif bmi(weight, height) < 29.9:
        return("You are Overweight")
    elif bmi(weight, height) > 29.91:
        return("You are Obese")
