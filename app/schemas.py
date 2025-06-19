from pydantic import BaseModel, HttpUrl

class URLRequest(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    short_code: str
    original_url: HttpUrl

    class Config:
        orm_mode = True