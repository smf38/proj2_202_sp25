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
    country: Optional[str]
    year: Optional[int]
    electricity_and_heat_co2_emissions: Optional[float]
    electricity_and_heat_co2_emissions_per_capita: Optional[float]
    energy_co2_emissions: Optional[float]
    energy_co2_emissions_per_capita: Optional[float]
    total_co2_emissions_excluding_lucf: Optional[float]
    total_co2_emissions_excluding_lucf_per_capita: Optional[float]

@dataclass(frozen=True)
class Node:
    value: Row
    next: Node|None
# ...

# Then your functions.

#takes the values from a list of strings containing the fields of a row object, and transforms
#them into a row, turns "" into None type
def parse_row(fields: list[str]) -> Row:

    #helper: turns a string into an int or None
    def to_int(x: str) -> Optional[int]:
        return None if x == "" else int(x)
    #helper: turns a string into a float or none
    def to_float(x: str) -> Optional[float]:
        return None if x == "" else float(x)

    country = str(fields[0])
    year =  to_int(fields[1])
    electricity_and_heat_co2_emissions = to_float(fields[2])
    electricity_and_heat_co2_emissions_per_capita = to_float(fields[3])
    energy_co2_emissions = to_float(fields[4])
    energy_co2_emissions_per_capita = to_float(fields[5])
    total_co2_emissions_excluding_lucf =  to_float(fields[6])
    total_co2_emissions_excluding_lucf_per_capita = to_float(fields[7])
    return Row(country,
                year,
                electricity_and_heat_co2_emissions,
                electricity_and_heat_co2_emissions_per_capita,
                energy_co2_emissions,
                energy_co2_emissions_per_capita,
                total_co2_emissions_excluding_lucf,
                total_co2_emissions_excluding_lucf_per_capita)

#takes a csv file and extracts it into a linked list of Row objects
#using multiple helper functions
def read_csv_lines(filename: str) -> Optional[Node]:
    with open(filename, mode='r', newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
    correct_header: list[str] = ['country',
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
    #helper: zips up the rows into a linked list
    def create_linked_list(idx:int) -> Optional[Node]:
        if idx == len(rows):
            return None
        current = parse_row(rows[idx])
        return Node(current, create_linked_list(idx+1))

    return create_linked_list(1)

#lists the length of a linked list recursively and returns it as an integer
def listlen(data: Optional[Node]) -> int:
    if data is None:
        return 0
    else:
        return 1 + listlen(data.next)

#filters a linked list according to a given field, comparison, and value, and returns
#a linked list that satisfies all the filter requirements
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

    row: Row = data.value
    rest: Optional[Node] = filter_rows(data.next, field_name, comparison, value)
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
