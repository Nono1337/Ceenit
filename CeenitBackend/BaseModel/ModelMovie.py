from pydantic import BaseModel

class CreateReview(BaseModel):
    userId: str = ""
    content: str

class MovieRating(BaseModel):
    userID:str = ""
    rating: int