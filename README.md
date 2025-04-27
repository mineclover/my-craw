uv venv
uv sync

# FastAPI 앱 실행 방법

1. 의존성 설치:

```
pip install fastapi uvicorn sqlalchemy
```

2. 앱 실행:

```
uvicorn app.main:app --reload
```

3. Swagger UI:

- 브라우저에서 http://localhost:8000/docs 접속

---

## 기능 설명

- 모든 요청은 sqlite DB(`app.db`)에 method, url, timestamp가 기록됩니다.
- DB 파일은 프로젝트 루트에 생성됩니다.
- SQLAlchemy를 사용하여 모델 및 세션을 관리합니다.
