
from typing import List, Annotated
from typing_extensions import TypedDict
import operator


class MealPlanningSubgraph(TypedDict):
    meals : Annotated[List[str], operator.add]
    