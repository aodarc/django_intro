
migrations:
	@docker exec -it -w /django_intro django_intro_api python src/manage.py makemigrations

migrate:
	@docker exec -it -w /django_intro django_intro_api python src/manage.py migrate

app:
	@mkdir -p src/apps/$(name)
	@docker exec -it -w /django_intro django_intro_api python src/manage.py startapp $(name) src/apps/$(name)

test_env:
	@cat ./docker/envs/env_example > ./docker/envs/.env-local

test_user:
	@docker exec -it -w /django_intro django_intro_api python src/manage.py createsuperuser