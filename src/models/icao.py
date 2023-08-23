from pydantic import BaseModel, field_validator, FieldValidationInfo

class Icao(BaseModel):
    code: str
    
    @field_validator("code")
    @classmethod
    def check_is_alphanumeric(cls, v: str, info: FieldValidationInfo) -> str:
        if isinstance(v, str):
            is_alnum = v.lower().isalnum()
            assert is_alnum, f"{info.field_name} must be alphanumeric"
        return v