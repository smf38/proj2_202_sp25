from __future__ import annotations
import sys
import csv
from typing import *
from dataclasses import dataclass
import unittest
import math
sys.setrecursionlimit(10_000)
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
def read_csv_lines(filename: str) -> Optional[Node]:
    def parse_row(fields: list[str]) -> Row:
        country = str(fields[0])
        year =  int(fields[1])
        electricity_and_heat_co2_emissions = float(fields[2])
        electricity_and_heat_co2_emissions_per_capita = float(fields[3])
        energy_co2_emissions = float(fields[4])
        energy_co2_emissions_per_capita = float(fields[5])
        total_co2_emissions_excluding_lucf =  float(fields[6])
        total_co2_emissions_excluding_lucf_per_capita = float(fields[7])
        return Row(country,
                    year,
                    electricity_and_heat_co2_emissions,
                    electricity_and_heat_co2_emissions_per_capita,
                    energy_co2_emissions,
                    energy_co2_emissions_per_capita,
                    total_co2_emissions_excluding_lucf,
                    total_co2_emissions_excluding_lucf_per_capita)
    with open(filename, mode='r', newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
    correct_header = ['country',
                    'year',
                    'electricity_and_heat_co2_emissions',
                    'electricity_and_heat_co2_emissions_per_capita',
                    'energy_co2_emissions',
                    'energy_co2_emissions_per_capita',
                    'total_co2_emissions_excluding_lucf',
                    'total_co2_emissions_excluding_lucf_per_capita']
    if len(rows) == 0:
        return None
    if rows[0] != correct_header:
        return None

    def create_linked_list(idx:int) -> Optional[Node]:
        if idx == len(rows):
            return None
        current = parse_row(rows[idx])
        return Node(current, create_linked_list(idx+1))

    return create_linked_list(1)

def list_len(data: Optional[Node]) -> int:
    if data is None:
        return 0
    else:
        return 1 + list_len(data.next)

def filter_rows(
    data: Optional[Node],
    field_name: str,
    comparison: str,
    value: Union[str, float, int]
) -> Optional[Node]:
    if data is None:
        return None
    if field_name == "country" and comparison != "equal":
        return None

    row = data.value
    rest = filter_rows(data.next, field_name, comparison, value)
    field_value = getattr(row, field_name)
    if field_value is None:
        return rest

    if field_name == "country" and comparison == "equal":
        if field_value == value:
            return Node(data.value, rest)
        else:
            return rest


    if comparison == "equal":
        if field_value == value:
            return Node(data.value, rest)
        else:
            return rest
    elif comparison == "less_than":
        if field_value < value:
            return Node(data.value, rest)
        else:
            return rest
    elif comparison == "greater_than":
        if field_value > value:
            return Node(data.value, rest)
        else:
            return rest
    else:
        raise Exception(f"Unknown comparison {comparison}")
# ...
