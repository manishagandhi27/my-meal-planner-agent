from  main.graph.graph_state import MealPlannerState
from main.services.user_profile_db import get_user_profile




def validate_inputs(state:MealPlannerState):
    print("in validate node \n ")
    user_profile =  get_user_profile()
    print(f"user profile found  {user_profile} \n")
    state["user_profile"] = user_profile
    return state