from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class StudentSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., gt=0, lt=4.0)

    class Config:
        schema_extra = {
            "example":{
                "name": "Hemant Rakesh",
                "email": "hemantrak05@gmail.com",
                "course_of_study": "MSc. Computer Science",
                "year": 2,
                "gpa": 3.0
            }

        }

class UpdateStudentModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }