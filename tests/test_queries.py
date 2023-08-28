import pytest
import numpy as np

import src.queries as queries


@pytest.fixture
def data():
    return queries.read_metars_csv(filepath="./tests/mocks/data/metars.csv")


def test_by_year_unique(data):
    df = queries.by_year(data, 2009)
    result = df["year"].unique()
    expected = np.array([2009])

    assert np.array_equal(result, expected)


def test_by_year_range(data):
    df = queries.by_year(data, 2005, end=2020)
    result = df["year"].unique()
    expected = np.array([2005, 2009, 2014, 2018])

    assert np.array_equal(result, expected)


def test_by_month_unique(data):
    df = queries.by_month(data, 1)
    result = df["month"].unique()
    expected = np.array([1])

    assert np.array_equal(result, expected)


def test_by_month_range(data):
    df = queries.by_month(data, 1, end=9)
    result = df["month"].unique()
    expected = np.array([1, 8])

    assert np.array_equal(result, expected)
