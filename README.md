# FastAPI + SQLModel + Alembic


# Docker Compose Commands executed in this lab

```sh
docker-compose exec -it db psql --username=postgres --dbname=foo
docker-compose exec web alembic init -t async migrations
docker-compose exec web alembic revision --autogenerate -m "init"
docker-compose exec web alembic upgrade head
docker-compose exec web alembic revision --autogenerate -m "add year"
docker-compose exec web alembic upgrade head
```
