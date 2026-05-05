import csv
import math
from dataclasses import dataclass
from typing import *
#testing pycharm commits

# Put your data definitions first!
from dataclasses import dataclass
@dataclass(frozen=True)
class Row:
    country: str
    year: int
    electricity_and_heat_co2_emissions: float
    electricity_and_heat_co2_emissions_per_capita: float
    energy_co2_emissions: float
    energy_co2_emissions_per_capita: float
    total_co2_emissions_excluding_lucf: float
    total_co2_emissions_excluding_lucf_per_capita: float

@dataclass(frozen=True)
class Node:
    value: Row
    next: Node|None
# ...

# Then your functions.

# ...
