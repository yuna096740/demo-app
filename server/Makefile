up:
	docker compose up -d

# DBのマイグレーションを実行
migrate:
	cd app/database/migrations && poetry run alembic upgrade head

# appコンテナ内の操作用
new-migration:
	docker compose exec app bash -c "cd app/database/migrations && poetry run alembic revision -m "${NAME}""

app-migrate:
	docker compose exec app bash -c "cd app/database/migrations && poetry run alembic upgrade head"

app-drop:
	docker compose exec app bash -c "cd app/database/migrations && poetry run alembic downgrade base"
