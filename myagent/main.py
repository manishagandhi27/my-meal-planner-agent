
from main.graph.graph_state import MealPlannerState
from main.graph.subgraphs.meal_generator import graph
import asyncio


# Done so this can run in parallel
async def call_reflection(state: MealPlannerState):
    
    result = await graph.ainvoke(initial_state)
    return result


if __name__ == "__main__":
    initial_state = {
        "user_profile" :{},
        "user_preference": "",
    "formatted_meal": "",
    "meals":[]
      
    }

    result = asyncio.run(call_reflection(initial_state))
  