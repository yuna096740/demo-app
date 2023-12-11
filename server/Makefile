up:
	docker compose up -d

# DBのマイグレーションを実行
migrate:
	cd app/database/migrations && poetry run alembic upgrade head

# appコンテナ内の操作用

# 現状これらのコマンドは使えない。
# 手順
# 1. docker compose exec app bash 
# 2. poetry shell
# 3. cd app/database/migrations
# 4. poetry run alembic revision -m "hogefuga"
# 要調査。 癖が強い。。。

new-migration:
	docker compose exec app bash -c "cd app/database/migrations && poetry run alembic revision -m "${NAME}""

app-migrate:
	docker compose exec app bash -c "cd app/database/migrations && poetry run alembic upgrade head"

app-drop:
	docker compose exec app bash -c "cd app/database/migrations && poetry run alembic downgrade base"
