import unittest
from typing import Optional, Union
from proj2 import (
    Row,
    Node,
    read_csv_lines,
    listlen,
    filter_rows,
    parse_row
)

class TestStudent(unittest.TestCase):

    def test_parse_row(self):
        row = parse_row(["USA", "2000", "10", "1", "20", "2", "30", "3"])
        self.assertEqual(row.country, "USA")
        self.assertEqual(row.year, 2000)

    def test_parse_row_spaces(self):
        row = parse_row(["USA", " ", " ", " ", " ", " ", "", ""])
        self.assertIsNone(row.year)
        self.assertIsNone(row.energy_co2_emissions)

    def test_listlen(self):
        data = read_csv_lines("test_data.csv")
        self.assertEqual(listlen(data), 10)

    def test_filter_country(self):
        data = read_csv_lines("test_data.csv")
        result = filter_rows(data, "country", "equal", "USA")
        self.assertEqual(listlen(result), 3)

    def test_filter_year(self):
        data = read_csv_lines("test_data.csv")
        result = filter_rows(data, "year", "greater_than", 2000)
        self.assertEqual(listlen(result), 7)

    def test_read_csv(self):
        data = read_csv_lines("test_data.csv")
        self.assertIsNotNone(data)

if __name__ == "__main__":
    unittest.main()
