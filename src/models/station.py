from typing import List

from pydantic import BaseModel, field_validator, FieldValidationInfo

from .icao import Icao


class Station(BaseModel):
    name: str
    icao: Icao
    op_hours: List[int]

    @field_validator("name")
    @classmethod
    def check_name_is_alphanumeric(cls, v: str, info: FieldValidationInfo) -> str:
        if isinstance(v, str):
            is_alnum = v.lower().replace(" ", "").isalnum()
            assert is_alnum, f"{info.field_name} must be alphanumeric"
        return v.title()

    @field_validator("name")
    @classmethod
    def check_name_have_spaces(cls, v: str, info: FieldValidationInfo) -> str:
        if " " not in v:
            raise ValueError(f"{info.field_name} must contain spaces")
        return v.title()

    @field_validator("op_hours")
    @classmethod
    def check_valid_hours(cls, v: List[int], info: FieldValidationInfo) -> str:
        if isinstance(v, list):
            for hour in v:
                assert (
                    hour >= 0 and hour < 24
                ), f"{info.field_name} must have valid hours"
        return v
