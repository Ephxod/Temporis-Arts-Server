from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):  
    user_id: str = Field(..., primary_key=True, index=True) 
    name: str = Field(..., index=True)

    class Config:
        schema_extra = {
            "example": {
                "user_id": "sampleid123",
                "name": "samplename"
            }
        }

    def __repr__(self):
        return f"<User(user_id={self.user_id}, name={self.name})>"


