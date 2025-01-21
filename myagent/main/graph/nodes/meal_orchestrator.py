
from  main.graph.graph_state import MealPlannerState


async def meal_orchestrator(state):
    print("inside meal_orchestrator \n")
    """Formats the meal plan to prevent duplication before sending it as a notification."""

    # ✅ Ensure meals are processed only once
    meals = state.get("meals", [])
    
    seen_meals = set()  # Track unique meals to prevent duplicates
    formatted_message = "🍽️ Your Meal Plan for Today:\n"

    for meal in meals:
        meal_type = list(meal.keys())[0]
        meal_data = meal[meal_type]

        # ✅ Avoid duplicate meal entries
        if meal_data.meal_name not in seen_meals:
            formatted_message += f"🔹 {meal_type.capitalize()}: {meal_data.meal_name}\n"
            seen_meals.add(meal_data.meal_name)  # Track this meal

    formatted_message += "\nReply with 'Regenerate' to receive alternatives."

    # ✅ Store formatted message in state before sending notification
    state["formatted_meal"] = formatted_message
    print(f"here are meals from meal_orchestrator {state["meals"]}")
    return state