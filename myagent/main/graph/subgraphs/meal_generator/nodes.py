
from .meal_state import MealPlanningSubgraph
import time
import random
from myagent.main.services.llm_api import generate_meal_suggestion


async def generate_breakfast(state):
    print("[START] Generating Breakfast...")
    bf_response = await generate_meal_suggestion("breakfast",[],500)
    print(f"breakfast response {bf_response}")
    #state["meals"] = {"breakfast": "Oatmeal with Fruits", "calories": 350}
    print("[DONE] Breakfast Generated")
    return {"meals": [{"breakfast": bf_response}]}

async def generate_lunch(state):
    print("[START] Generating Lunch...")
    lunch_response = await generate_meal_suggestion("lunch",[],500)
    print(f"lunch response {lunch_response}")
    #state["mealsLunch = {"lunch": "Grilled Chicken Salad", "calories": 500}
    print("[DONE] Lunch Generated")
    return {"meals": [{"lunch": lunch_response}]}

async def generate_dinner(state):
    print("[START] Generating Dinner...")
    dinner_response = await generate_meal_suggestion("dinner",[],500)
    print(f"dinner response {dinner_response}")
   # state["meals"] = {"dinner": "Stir-Fried Vegetables with Tofu", "calories": 450}
    print("[DONE] Dinner Generated")
    return {"meals": [{"dinner": dinner_response}]}




def calculate_target_calories(user_profile):
    """
    Dynamically calculates daily calorie target based on user profile.
    """
    weight = user_profile["weight"]  # kg
    height = user_profile["height"]  # cm
    #age = user_profile["age"]  # years
    age = 34
    gender = "female"
    activity_level = "light"
    #gender = user_profile["gender"].lower()  # "male" or "female"
    #activity_level = user_profile["activity_level"].lower()  # "sedentary", "light", "moderate", "active", "super"
    goal = user_profile["goal"].lower()  # "weight_loss", "muscle_gain", "maintenance"

    # ✅ Convert weight from pounds to kg if necessary
    if weight > 100:  # Assuming weight in pounds if it's too high
        weight = weight * 0.453592  # Convert to kg

    # ✅ Convert height from inches to cm if necessary
    if height < 100:  # Assuming height in inches
        height = height * 2.54  # Convert to cm

    # ✅ Calculate BMR
    if gender == "female":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:  # Male
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

    # ✅ Apply Activity Level Multiplier
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "super": 1.9
    }
    tdee = bmr * activity_multipliers.get(activity_level, 1.2)  # Default to "sedentary" if not provided

    # ✅ Adjust for Goal
    if goal == "weight_loss":
        target_calories = tdee - 500  # 500 kcal deficit
    elif goal == "muscle_gain":
        target_calories = tdee + 500  # 500 kcal surplus
    else:
        target_calories = tdee  # Maintenance

    return int(target_calories)


async def calorie_adjustment(state):
    print("inside calorie_adjustment \n")
    #print(f"here are meals from subgraph {state["meals"]}")
    # user_profile = state["user_profile"]
    
    # """Adjusts meal portions to match the dynamically calculated daily calorie target."""
    # user_profile = state["user_profile"]

    # # ✅ Calculate target calories dynamically
    # target_calories = calculate_target_calories(user_profile)
    # print(f"target calorie {target_calories} \n")
    # state["user_profile"]["daily_calorie_target"] = target_calories  # Store it in state for reference

    # # ✅ Sum current meal calories
    # meals = state["meals"]
    # total_calories = sum(meal[list(meal.keys())[0]].calories for meal in meals)

    # if total_calories == target_calories:
    #     print(f"✅ Calories are balanced: {total_calories} kcal")
    #     return state  # No adjustment needed

    # # ✅ Adjust proportionally
    # difference = target_calories - total_calories
    # print(f"⚖️ Adjusting calories: Target {target_calories} kcal, Current {total_calories} kcal")

    # for meal in meals:
    #     meal_type = list(meal.keys())[0]
    #     meal_data = meal[meal_type]

    #     # Scale portion sizes to match target calories
    #     if abs(difference) > 50:
    #         adjustment_factor = target_calories / total_calories
    #         meal_data.calories = int(meal_data.calories * adjustment_factor)
    #         print(f"🔄 Adjusted {meal_type} to {meal_data.calories} kcal")
    # state["meals"] = []
    # state["meals"] = meals
    return state