name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))
gender = input("Enter your gender (M/F/O): ").upper()
activity = input("Enter your activity (sedentary/moderate/active/athlete): ").lower()

# Activity-based calculations
if activity == "sedentary":
    protein = 1.0 * weight
    carbs = 3 * weight
    fats = 0.6 * weight
    calories = 28 * weight

elif activity == "moderate":
    protein = 1.3 * weight
    carbs = 4 * weight
    fats = 0.8 * weight
    calories = 30 * weight

elif activity == "active":
    protein = 1.6 * weight
    carbs = 5 * weight
    fats = 1.0 * weight
    calories = 33 * weight  

elif activity == "athlete":
    protein = 2.0 * weight
    carbs = 6.5 * weight
    fats = 1.2 * weight
    calories = 38 * weight

else:
    print("Invalid activity level!")
    exit()

# Vitamins
if gender == "M":
    vitamins = {"Iron": "8 mg", "Calcium": "1000 mg", "Vitamin C": "90 mg", "Vitamin D": "600 IU"}
elif gender == "F":
    vitamins = {"Iron": "18 mg", "Calcium": "1200 mg", "Vitamin C": "75 mg", "Vitamin D": "600 IU"}
else:
    vitamins = {"Iron": "10 mg", "Calcium": "1000 mg", "Vitamin C": "85 mg", "Vitamin D": "600 IU"}

# BMI Calculation
bmi = round(weight / (height ** 2), 2)
ideal_weight = round(22 * (height ** 2), 2)
difference = round(weight - ideal_weight, 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print("\n-------------------- DAILY NUTRITION & HEALTH REPORT --------------------")

print(f"\nHello {name},\n")
print("Welcome to AI Health Assistant System")
print("I have analyzed your data and generated your personalized health report.\n")

print(f"BMI: {bmi} ({category})")
print(f"Ideal Weight: {ideal_weight} kg")
print(f"Weight Difference: {difference} kg")
print(f"Protein Needed: {protein} g/day")
print(f"Carbohydrates Needed: {carbs} g/day")
print(f"Fats Needed: {fats} g/day")
print(f"Calories Required: {calories} kcal/day")

water_intake = round(weight * 0.033, 2)
print(f"Water Intake: {water_intake} L/day")

if 14 <= age <= 17:
    sleep = "8–10 hours"
elif 18 <= age <= 25:
    sleep = "7–9 hours"
else:
    sleep = "7–8 hours"

print(f"Sleep Needed: {sleep}")

print("\nVitamins & Minerals:")
for v in vitamins:
    print(v, ":", vitamins[v])

print("\n===================================")
print("AI PERSONAL HEALTH ANALYSIS")
print("===================================\n")

# Health Score
score = 100
if category != "Normal":
    score -= 20
if activity == "sedentary":
    score -= 15
if age < 18:
    score -= 5

print(f"AI Health Score: {score}/100\n")

if category == "Underweight":
    print("AI WEIGHT GAIN PLAN")
    print("1. Increase calorie intake by 300–500 kcal/day")
    print("2. Eat protein-rich foods (milk, eggs, paneer, nuts)")    
    print("3. Eat 5–6 meals per day")
    print("4. Strength training (push-ups, squats)")

    extra = abs(difference)

    if extra <= 5:
        print("Level: Mild Underweight")
    elif extra <= 10:
        print("Level: Moderate Underweight")
    else:
        print("Level: High Underweight")

    gain_target = round(extra * 7700 / 7, 0)
    print(f"\nDaily Calorie Surplus Target: {gain_target} kcal")

elif category == "Overweight":
    print("AI WEIGHT LOSS PLAN")
    print("1. Reduce sugar and junk food")
    print("2. Drink more water")
    print("3. Do regular cardio exercises")

    extra = abs(difference)

    if extra <= 5:
        print("Level: Mild Overweight → Walking + Yoga")
    elif extra <= 10:
        print("Level: Moderate Overweight → Cycling + Skipping")
    else:
        print("Level: High Overweight → Jogging + Cardio Training")

    burn_target = round(extra * 7700 / 7, 0)
    print(f"\nDaily Calorie Burn Target: {burn_target} kcal")

else:
    print("AI MAINTENANCE PLAN")
    print("1. Maintain balanced diet")
    print("2. Regular exercise")
    print("3. Stay hydrated")
    print("4. Good sleep routine")

print("\nAI HEALTH INSIGHT")

if bmi > 30:
    print("Risk: High chance of lifestyle diseases")
elif bmi < 18.5:
    print("Risk: Weak immunity & low energy")
else:
    print("Risk: Healthy range")

print("\n----------------------- END OF AI ANALYSIS ------------------------")

print("\nThank you for using AI Health Assistant")
print("\n=================***********************************==================")
