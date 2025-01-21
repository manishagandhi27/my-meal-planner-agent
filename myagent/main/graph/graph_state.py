from typing import TypedDict
from typing import List, Annotated
from typing_extensions import TypedDict
import operator

class MealPlannerState(TypedDict):
    user_profile: dict
    user_preference : str
    formatted_meal: str
    meals: Annotated[List[str], operator.add]
    feedback: str
    trigger: str
    
