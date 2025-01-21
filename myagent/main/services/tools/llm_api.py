
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.pydantic_v1 import BaseModel

# Load API key from .env file
load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o"

os.environ["BROWSER"] = "/usr/bin/google-chrome"

model = ChatOpenAI(model=OPENAI_MODEL)

class MealResponse(BaseModel):
    meal_name: str
    ingredients_with_accurate_measurements: list[str]
    recipe_short_summary: str
    calories: int

#add profile or preference here or load from DB.
SYSTEM_MESSAGE = """
You are an AI nutritionist planning meals for a user. 
User Profile:
- vegetarian (not vegan), no eggs or meat.
- Prefers Indian & Asian cuisine. tofu based recipes
- Follows a low-carb, high-protein, calorie-deficit diet.
- No alcohol consumption.
- Drinks: Green tea, Coffee, Macha
- Open to exploring low-carb, high-protein meal options.

Meal Preferences:
- **Breakfast:** 
- **Lunch:**
- **Dinner:** 
- **Desserts:** 
- **New Experiments:** 

Your task: **Suggest a meal that fits the user's dietary needs, preferred cuisine, and available ingredients and variety in meals.**
"""


structured_llm = model.with_structured_output(MealResponse)

async def generate_meal_suggestion(meal_type, pantry_items, calorie_target):
    """
    Calls the LLM to generate a meal suggestion based on meal type, available ingredients, and calorie goals.
    """
    # User query (dynamic part)
    user_query = HumanMessage(
        content=f"""
        Generate a {meal_type} meal using these ingredients: {', '.join(pantry_items)}.
        Ensure it aligns with a low-carb, high-protein, calorie-deficit diet.
        The meal should not exceed {calorie_target} calories.

        Return a JSON object with:
        - "meal_name": (string)
        - "ingredients_with_accurate_measurements": (list of strings)
        - "recipe_short_summary": (string)
        - "calories": (integer)
        """
    )

    # Combine system + user messages
    messages = [SYSTEM_MESSAGE, user_query]

    response = await structured_llm.ainvoke(messages)
    print(f"model response {response} \n")
    return response