from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from models.users import User
from models.charts import Chart


class Record(SQLModel, table=True):
    record_id: int = Field(primary_key=True, index=True)
    user_id: str = Field(..., foreign_key="user.user_id")
    chart_id: str = Field(..., foreign_key="chart.chart_id")
    high_score: int = Field(index=True, default=0)
    clear_status: bool = Field(default=False)
    full_combo_status: bool = Field(default=False)
    all_arts_status: bool = Field(default=False)
    judgement: int = Field(..., index=True)
    play_count: int = Field(index=True, default=1)
    score_updated_date: datetime = Field(index=True)

    user: "User" = Relationship()

    class Config:
        schema_extra = {
            "example": {
                "user_id": "1",
                "chart_id": "0_1",
                "high_score": 4567890,
                "clear_status": False,
                "full_combo_status": False,
                "all_arts_status": False,
                "judgement": 0,
                "play_count": 3
            }
        }

    def __repr__(self):
        return (f"<Record(record_id={self.record_id}, user_id={self.user_id}, "
                f"chart_id={self.chart_id}, high_score={self.high_score}, "
                f"clear_status={self.clear_status}, full_combo_status={self.full_combo_status}, "
                f"all_arts_status={self.all_arts_status}, judgement={self.judgement}, "
                f"play_count={self.play_count}, score_updated_date={self.score_updated_date})>")
