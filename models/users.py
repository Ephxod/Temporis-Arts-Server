from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):  # SQLModel을 상속받고 table=True를 설정
    user_id: str = Field(..., primary_key=True, index=True)  # PK 설정
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


