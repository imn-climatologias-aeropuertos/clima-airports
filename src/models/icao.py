from pydantic import BaseModel, field_validator, FieldValidationInfo

class Icao(BaseModel):
    code: str
    
    @field_validator("code")
    @classmethod
    def check_is_alphanumeric(cls, v: str, info: FieldValidationInfo) -> str:
        if isinstance(v, str):
            is_alnum = v.lower().isalnum()
            assert is_alnum, f"{info.field_name} must be alphanumeric"
        return v.upper()
    
    @field_validator("code")
    @classmethod
    def check_is_four_length(cls, v: str, info: FieldValidationInfo) -> str:
        if isinstance(v, str):
            length = len(v)
            assert length == 4, f"{info.field_name} must have 4 characters length"
        return v.upper()