from fastapi import APIRouter, Depends, Request, HTTPException, status
from database.connection import get_session
from models.users import User
from models.musics import Music
from models.charts import Chart
from models.records import Record
from services.auths import get_current_user

chart_router = APIRouter(
    tags=["Chart"],
)

@chart_router.get("/stats")
async def get_charts(session=Depends(get_session), current_user: dict = Depends(get_current_user)) -> dict:
    # 모든 음악 조회
    music_list = session.query(Music).all()
    result = []
    
    for music in music_list:
        music_data = {
            "music_id": music.music_id,
            "title": music.title,
            "composer": music.composer,
            "charts": []
        }
        
        # 해당 음악의 차트 조회
        charts = session.query(Chart).filter(Chart.music_id == music.music_id).all()
        for chart in charts:
            # 해당 차트의 레코드 조회
            records = session.query(Record).filter(
                Record.music_id == music.music_id,
                Record.difficulty == chart.difficulty
            ).all()

            if records:
                # 평균 점수 계산
                avg_score = session.query(func.avg(Record.high_score)).filter(
                    Record.music_id == music.music_id,
                    Record.difficulty == chart.difficulty
                ).scalar() or 0

                # clear_status와 full_combo_status 비율 계산
                clear_count = sum(1 for record in records if record.clear_status)
                full_combo_count = sum(1 for record in records if record.full_combo_status)

                clear_rate = (clear_count / len(records)) * 100
                full_combo_rate = (full_combo_count / len(records)) * 100
            else:
                avg_score = 0
                clear_rate = 0
                full_combo_rate = 0

            # 차트 데이터 추가
            chart_data = {
                "difficulty": chart.difficulty,
                "level": chart.level,
                "avg_score": avg_score,
                "clear_rate": clear_rate,
                "full_combo_rate": full_combo_rate
            }
            music_data["charts"].append(chart_data)

        result.append(music_data)

    return {"data": result}

@chart_router.get("/ranking")
async def get_ranking(music_id: int, difficulty: int, session=Depends(get_session)) -> dict:
    # 해당 음악과 난이도에 대한 기록 조회
    records = session.query(Record).filter(
        Record.music_id == music_id,
        Record.difficulty == difficulty
    ).order_by(
        Record.high_score.desc(),  # high_score 내림차순 정렬
        Record.score_updated_date.asc()  # 동점일 경우 score_updated_date 오름차순 정렬
    ).limit(10).all()

    # 결과를 리스트 형태로 변환
    result = []
    for record in records:
        result.append({
            "user_id": record.user_id,
            "name": record.name,
            "high_score": record.high_score,
            "score_updated_date": record.score_updated_date.strftime("%Y-%m-%d %H:%M:%S")
        })

    # 결과를 dict 형태로 반환
    return {"data": result}