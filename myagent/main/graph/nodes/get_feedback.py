from  main.graph.graph_state import MealPlannerState
from langgraph.types import interrupt, Command


async def get_feedback(state):
    print("inside get_feedback \n")
    feedback = interrupt("Do you accept this output or want to regenerate? (Type 'accept' or 'regenerate')")
    return {"feedback": feedback}
    