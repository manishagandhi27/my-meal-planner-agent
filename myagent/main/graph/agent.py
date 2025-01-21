
from langgraph.graph import StateGraph, END
import logging
from main.graph.nodes.gather_inputs import validate_inputs
from myagent.main.graph.subgraphs.meal_generator.generate_meal import get_meal_subgraph
from langgraph.checkpoint.sqlite import SqliteSaver
from main.services.db.init_db import get_db_connection
import sqlite3

from myagent.main.graph.nodes.get_feedback import  get_feedback
from myagent.main.graph.nodes.meal_orchestrator import meal_orchestrator
from myagent.main.graph.nodes.notify_user import notify_user
from myagent.main.graph.graph_state import MealPlannerState

meal_generation_graph = get_meal_subgraph()
#checkpointer = SqliteSaver(get_db_connection())

def feedback_router(state):
    """
    Determines next route based on feedback state
    Returns: 
    - 'meal_agent' if feedback requires regeneration
    - END if feedback is satisfactory
    """
    if state.get('feedback') == "regenerate":
        return 'generateMealPlan'
    return END



try :
    graph_builder = StateGraph(MealPlannerState)
    #Nodes
    graph_builder.add_node("gatherInputs", validate_inputs)
    #subgraph as node
    graph_builder.add_node("generateMealPlan", meal_generation_graph)   
    graph_builder.add_node("orchestrateMeals", meal_orchestrator)
    graph_builder.add_node("sendUserNotification",notify_user)
    graph_builder.add_node("get_feedback", get_feedback)
    #Edges
    graph_builder.add_edge("gatherInputs", "generateMealPlan")
    graph_builder.add_edge("generateMealPlan", "orchestrateMeals")
    graph_builder.add_edge("orchestrateMeals", "sendUserNotification")
    graph_builder.add_edge("sendUserNotification", "get_feedback")
    graph_builder.add_conditional_edges(
        "get_feedback",
        feedback_router,
        {
          'generateMealPlan': 'generateMealPlan',
           END: END
        }
    )
    graph_builder.set_entry_point("gatherInputs")
    graph = graph_builder.compile()
except Exception as e:
    logging.error(f"exception in node egdes {e}")
