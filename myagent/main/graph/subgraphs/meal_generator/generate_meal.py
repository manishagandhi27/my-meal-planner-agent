from langgraph.graph import StateGraph, END
from .nodes import (
    generate_breakfast, generate_dinner, generate_lunch
)
from main.graph.subgraphs.meal_generator.nodes import calorie_adjustment
import logging
from .meal_state import MealPlanningSubgraph



def get_meal_subgraph():
    try:
        graph_builder = StateGraph(MealPlanningSubgraph)
        graph_builder.add_node("generateBreakfast", generate_breakfast)
        graph_builder.add_node("generateLunch",generate_lunch)
        graph_builder.add_node("generateDinner", generate_dinner)
        graph_builder.add_node("adjustCalories", calorie_adjustment)
        graph_builder.set_entry_point("generateBreakfast")
        graph_builder.set_entry_point("generateLunch")
        graph_builder.set_entry_point("generateDinner")
        graph_builder.add_edge("generateBreakfast", "adjustCalories")
        graph_builder.add_edge("generateLunch", "adjustCalories")
        graph_builder.add_edge("generateDinner", "adjustCalories")
        return graph_builder.compile()
    except Exception as e:
        logging.error(f"Exception during subgraph creation {e}")
        

