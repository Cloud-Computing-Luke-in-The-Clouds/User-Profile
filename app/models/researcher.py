from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Interest_Field(BaseModel):
    interest_name: Optional[str] = None


class UserProfile(BaseModel):
    user_id: Optional[str] = None
    email_address: Optional[str] = None
    name: Optional[str] = None
    password: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    interest_list: Optional[list[Interest_Field]] = None
    points: Optional[int]


class Config:
    json_schema_extra = {
        "example": {
            "user_id": "123",
            "email_address": "testuser@columbia.edu",
            "name": "John Doe",
            "password": "XXXXXXXX",
            "age": 18,
            "sex": "Male",
            "interest_list": [
                {
                    "interest_name": "Cloud Computing"
                }
            ],
            "points": 2
        }
    }
