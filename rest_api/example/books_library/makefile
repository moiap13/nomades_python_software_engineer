run_server:
	FLASK_APP=app:server flask run --reload

run_tests:
	python -m unittest discover -s tests

run_coverage:
	python -m coverage run -m unittest discover -s tests
	python -m coverage report -m

run_coverages:
	python -m coverage run ./tests/users/users_mapper_test.py
	python -m coverage run ./tests/users/users_service_test.py
	python -m coverage combine
	python -m coverage report -m

create_requirements:
	pip list --format=freeze > requirements.txt