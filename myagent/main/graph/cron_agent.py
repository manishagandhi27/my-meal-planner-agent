from typing import TypedDict
import uuid
import hashlib
import httpx
from langgraph_sdk import get_client
from langgraph.graph import StateGraph, START, END
from myagent.main.graph.graph_state import MealPlannerState
import logging

# Initialize LangGraph client
client = get_client(url="http://localhost:8000")

# Define the input structure for the cron job
class MealPlannerInput(TypedDict):
    user_email: str  # Email where the meal plan will be sent
    trigger: str


def cron_setup(state: MealPlannerState):
    # Initialize the state required by your main graph
    return {
        "user_profile": {},
        "user_preference": {},
        "formatted_meal": "",
        "meals": [],
        "feedback": ""
    }
    
    
async def generate_meal_plan(state: MealPlannerInput, config):
    """Generates a meal plan and stores it in a thread for tracking."""
    user_email = state["user_profile"]["email"]
    # Create a unique thread ID for tracking
    thread_id = str(uuid.UUID(hex=hashlib.md5(user_email.encode("UTF-8")).hexdigest()))

    try:
        thread_info = await client.threads.get(thread_id)
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            # Create a new thread for meal planning if it doesn't exist
            thread_info = await client.threads.create(thread_id=thread_id)
        else:
            raise e
    logging.info(f"thread_id {thread_id}")
    # Store the generated meal plan inside the thread
    await client.threads.update(thread_id, metadata={"meal_plan": state["formatted_meal"]})
    initial_state = {
            "user_profile": {},
            "user_preference": {},
            "formatted_meal": "",
            "meals": [],
            "feedback": "",
            "user_email": "youremail@gmail.com",  
            "trigger": "manual" 
        }
    await client.runs.create(
            thread_id,
            "main", #main graph id from langgraph.json
            input=initial_state,
            multitask_strategy="rollback",
        )
    





# state["user_email"] = "a.g.com"


# Define the LangGraph StateGraph
graph = StateGraph(MealPlannerInput)
graph.add_node("generate_meal_plan", generate_meal_plan)
graph.add_edge(START, "generate_meal_plan")
graph.add_edge("generate_meal_plan", END)

# Compile the graph
graph = graph.compile()
