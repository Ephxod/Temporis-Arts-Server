from fastapi import APIRouter, Depends
from sqlalchemy import func
from database.connection import get_session
from models.musics import Music
from models.charts import Chart
from models.records import Record
from models.users import User
from models.responses.charts import ChartResponse, MusicResponse, ChartsStatsResponse, UserHighScoreResponse, RankingResponse
from services.auths import get_current_user

chart_router = APIRouter(
    tags=["Chart"],
)

@chart_router.get("/stats", response_model=ChartsStatsResponse)
async def get_charts(session=Depends(get_session), current_user: dict = Depends(get_current_user)) -> ChartsStatsResponse:
    music_list = session.query(Music).all()
    result = []
    
    for music in music_list:
        music_data = MusicResponse(
            music_id=music.music_id,
            title=music.title,
            composer=music.composer,
            charts=[]
        )
        
        charts = session.query(Chart).filter(Chart.music_id == music.music_id).all()
        for chart in charts:
            # judgement 값에 따라 grouping하여 평균 점수 계산
            for judgement in [0, 1]:
                records = session.query(Record).filter(
                    Record.chart_id == chart.chart_id,
                    Record.judgement == judgement  
                ).all()

                if records:
                    avg_score = session.query(func.avg(Record.high_score)).filter(
                    Record.chart_id == chart.chart_id,
                    Record.judgement == judgement  
                    ).scalar() or 0

                    clear_count = sum(1 for record in records if record.clear_status)
                    full_combo_count = sum(1 for record in records if record.full_combo_status)

                    clear_rate = (clear_count / len(records)) * 100
                    full_combo_rate = (full_combo_count / len(records)) * 100
                else:
                    avg_score = 0
                    clear_rate = 0
                    full_combo_rate = 0

                chart_data = ChartResponse(
                    chart_id=chart.chart_id,  
                    difficulty=chart.difficulty,
                    level=chart.level,
                    avg_score=avg_score,
                    clear_rate=clear_rate,
                    full_combo_rate=full_combo_rate,
                    judgement=judgement 
                )
                music_data.charts.append(chart_data)

        result.append(music_data)

    return ChartsStatsResponse(data=result)

@chart_router.get("/ranking", response_model=RankingResponse)
async def get_ranking(chart_id: str, session = Depends(get_session)) -> RankingResponse:
    result = {
        "easy": [],
        "hard": []
    }

    for judgement in [0, 1]:  # 0은 easy, 1은 hard
        records = session.query(Record).join(User).filter(
            Record.chart_id == chart_id,
            Record.judgement == judgement  
        ).order_by(
            Record.high_score.desc(),
            Record.score_updated_date.asc()
        ).limit(10).all()

        for record in records:
            user_score = UserHighScoreResponse(
                user_id=record.user_id,
                name=record.user.name,
                high_score=record.high_score,
                score_updated_date=record.score_updated_date
            )
            if judgement == 0:
                result["easy"].append(user_score)
            else:
                result["hard"].append(user_score)

    return RankingResponse(easy=result["easy"], hard=result["hard"])