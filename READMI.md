1. Для запуска проекта используем команду
    uvicorn app.main:app --reload

2. Для миграции проекта используем команду
    alembic init migrations
    alembic revision --autogenerate -m "comment"
    alembic upgrade head

    -Откатить миграцию на одну назад
    alembic downgrade -1