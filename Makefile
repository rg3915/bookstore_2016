install:
	pip install -r requirements.txt

migrate:
	./manage.py makemigrations
	./manage.py migrate

createuser:
	./manage.py createsuperuser --username='admin' --email=''

backup:
	./manage.py dumpdata core --format=json --indent=2 > fixtures.json

load:
	./manage.py loaddata fixtures.json

run:
	./manage.py runserver

shell_customer:
	./manage.py shell < fixtures/shell_customer.py

shell_seller:
	./manage.py shell < fixtures/shell_seller.py

shell_pf:
	./manage.py shell < fixtures/shell_pf.py

shell_pj:
	./manage.py shell < fixtures/shell_pj.py

shell_ordered:
	./manage.py shell < fixtures/shell_ordered.py

shell_sale:
	./manage.py shell < fixtures/shell_sale.py

shell_book:
	./manage.py shell < fixtures/shell_book_.py

shell_store:
	./manage.py shell < fixtures/shell_store.py

initial: install migrate createuser load

fixtures: shell_store shell_book