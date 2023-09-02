from typing import List

from pydantic import BaseModel

DAYS_PER_MONTH: List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

MONTH_NAMES: List[str] = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "setiembre",
    "octubre",
    "noviembre",
    "diciembre",
]


def days_per_month_as_str(max_days: int) -> List[str]:
    return [f"{day}" for day in range(1, max_days + 1)]


def days_per_month_as_int(max_days: int) -> List[int]:
    return [day for day in range(1, max_days + 1)]


class Month(BaseModel):
    index: int
    name: str
    days_as_str: List[str]
    days_as_int: List[int]


MONTHS: List[Month] = [
    Month(
        index=i + 1,
        name=MONTH_NAMES[i],
        days_as_str=days_per_month_as_str(DAYS_PER_MONTH[i]),
        days_as_int=days_per_month_as_int(DAYS_PER_MONTH[i]),
    )
    for i in range(12)
]
