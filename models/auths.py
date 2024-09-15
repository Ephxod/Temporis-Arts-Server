from pydantic import BaseModel, Field
import base64

class Auth(BaseModel):
    user_id: str = Field(...)
    user_ticket: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_id": "sampleid123",
                "user_ticket": str(base64.b64encode(b"sampleticket"))
            }
        }