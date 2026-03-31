name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))
gender = input("Enter your gender(M/F/O): ")
activity = input("Entre your activity(sedentary/moderate/active/athlete): ")

if activity=="sedentary":
    protein = 1.0 * weight
    carbs = 3 * weight
    fats = 0.6 * weight
    calories = 28 * weight

elif activity=="moderate":
    protein = 1.3 * weight
    carbs = 4 * weight
    fats = 0.8 * weight
    calories = 30 * weight

elif activity=="active":
    protein = 1.6 * weight
    carbs = 5 * weight
    fats = 1.0 * weight
    calories = 33 * weight  

elif activity=="athlete":
    protein = 2.0 * weight
    carbs = 6.5 * weight
    fats = 1.2 * weight
    calories = 38 * weight

if gender=="M":
    vitamins = {"Iron": "8 mg", "Calcium": "1000 mg", "Vitamin C": "90 mg", "Vitamin D": "600 IU"}
elif gender=="F":
      vitamins = {"Iron": "18 mg", "Calcium": "1200 mg", "Vitamin C": "75 mg", "Vitamin D": "600 IU"}
else :
    vitamins = {"Iron": "10 mg", "Calcium": "1000 mg", "Vitamin C": "85 mg", "Vitamin D": "600 IU"}

bmi = round(weight / (height ** 2),2)
ideal_weight = round(22 * (height ** 2),2)
difference = round(weight - ideal_weight, 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

water_intake = (weight*0.033)

if 14 <= age <= 17:
    sleep = "8–10 hours"
elif 18 <= age <= 25:
    sleep = "7–9 hours"
else:  
    sleep = "7–8 hours"    

print("\n-------------------- DAILY NUTRITION & HEALTH REPORT --------------------")

print(f"\nHello {name},\n")
print("Welcome to AI Health Assistant System")
print("I have analyzed your data and generated your personalized health report.\n")

print(f"\nBMI:", {bmi,(category)})
print(f"Ideal Weight is: {ideal_weight}kg") 
print(f"weight Difference: {difference}kg")
print(f"Protein Needed: {protein}g/day")
print(f"Carbohydrates Needed: {carbs}g/day")
print(f"Fats Needed: {fats}g/day")
print(f"Calories Required: {calories}Kcal/day")
print(f"Water Intake: {water_intake}L/day")
print(f"Sleep Needed: {sleep}")

print("\n-------**********Vitamins & Mineral Recommendation-************-----------")
for vitamin in vitamins:
    print(vitamin,":",vitamins[vitamin])


print("\n==================================")
print("AI PERSONAL HEALTH ANALYSIS")
print("====================================")

score = 100
if category != "Normal":
    score -= 20
if activity =="sedentary":
    score -=5

print(f"AI Health Score: {score}/100\n")  

if category == "Underweight":
    print("AI weight gain plan")
    print("1. Increase calorie intake by 300-500 kcal/day")
    print("2. Eat protein rich foods (milk,eggs,paneer,nuts)")
    print("3. Eat 5-6 meals per day")
    print("4. Strength training (push-ups,squats)")

    extra = abs(difference)

    if extra <= 5:
        print("level: Mild Underweight")
    elif extra <=10:
        print("level:Moderate underweight")
    else:
        print("level:high underweight")    

    gain_target = round(extra*7700/7 , 0)      
    print(f"\nDaily calorie surplus target:{gain_target}kcal")  

elif category == "Overweight":
    print("AI weight loss  plan")
    print("1. Reduce sugar and junk food")
    print("2. Drink more water")
    print("3. Do regular cardio excercises")

    extra =abs(difference)

    if extra <= 5:
        print("level :Mild overweight = walking + yoga")
    elif extra <= 10:
        print("level:moderate overweight = cycling = skipping")  
    else:
        print("level: high overweight = jogging + cardio training")   

    burn_target = round(extra*7700/7,0)      
    print(f"\ndaily calorie burn target:{burn-target}kcal")   

else:
    print("AI MAINTENANCE PLAN") 
    print("1. maintain balanced diet")
    print("2. regular exercise")   
    print("3. stay hydrated")
    print("4. good sleep routine")

print("\nAI HEALTH INSIGHT")    

if bmi>30:
    print("Risk: High chance of lifestyle diseases")
elif bmi< 18.5:
    print("Risk: weak immunity & low energy")    
else:
    print("Risk: Health range")    

print("\n-------------------------END OF AI ANALYSIS------------------------")

print(f"\nTake care,{name}")
print("Thankyou for using AI Health Assistance")
("====================***********************************==================")
