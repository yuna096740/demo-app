build:
	docker compose build

up:
	docker compose up -d

setup:
	@if [ -e .env ] ; then \
   		echo ".env already exists"; \
   	else \
		cp .env.example .env; \
	fi

	@make build
	@make up

# DBのマイグレーションを実行
# migrate:
# 	cd app/database && poetry run alembic upgrade head

# appコンテナ内の操作用

# 現状以下の make コマンドは使えない。
# 手順
# 0. (demo-app-server-py3.11) root@9477ce5d687f:/app/app/database# 
#     poetry run alembic init migrations
# 1. docker compose exec app bash 
# 2. poetry shell
# 3. cd app/database
# 4. poetry run alembic revision -m "hogefuga"
# 要調査。 癖が強い。。。

new-migration:
	docker compose exec app bash -c "cd app/database && poetry run alembic revision -m "${NAME}""

app-migrate: # ○
	docker compose exec app bash -c "cd app/database && poetry run alembic upgrade head"

app-drop:
	docker compose exec app bash -c "cd app/database && poetry run alembic downgrade base"
