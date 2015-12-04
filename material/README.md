***************************
Dominando o shell do Django
***************************

```python
# from project.app.models import class
# from bookstore.bookstore.models import Customer, Seller, PF, PJ, Ordered, Sale, Author, Publisher, Book, Store
from bookstore.core.models import Customer
import datetime
d = datetime.datetime(1999, 12, 31, 23, 59, 59, 123456).isoformat(" ")
customer = Customer(gender='M',treatment='sr',first_name='John',last_name='Smith',birthday=d,email='js@example.com')
customer.save()
customers = Customer.objects.all()
data_atual = datetime.datetime.now()
Customer.objects.create(gender='M',first_name='Alef',last_name='Lopez',birthday=data_atual,email='al@example.com')

Customer.objects.filter(id=1).delete()
c = Customer.objects.get(pk=1)
c.delete()
Customer.objects.all().delete()

customers = Customer.objects.all()[0]
customers.email
customers.birthday

customers = Customer.objects.all()
for i in customers: print(i.email, i.birthday, i.active)

Customer.objects.filter(birthday__year=2015)
Customer.objects.filter(birthday__year=2015).count()

Customer.objects.filter(birthday__year=2015).update(active=False)

# from vendas_project.vendas.models import Customer
customers = Customer.objects.all()
customers = Customer.objects.all().values()
for i in customers: print(i)
customers = Customer.objects.all().values('first_name','last_name','birthday')
[x for x in Customer().__dict__.keys() if not x.startswith('_')]


from bookstore.core.models import Book


from myproject.core.models import Person
p = Person.objects.search_person('James')
p
p.count()
```



Vendo o SQL equivalente de uma consulta do Django
=================================================

Se no Django fazemos uma consulta do tipo

```python
from bookstore.core.models import Book
consulta = Book.objects.all()
```

para ver o equivalente em SQl basta digitar

```python
print(consulta.query)
```

Eis o SQL equivalente:

```sql
SELECT "core_book"."id", "core_book"."name", "core_book"."price" FROM "core_book" ORDER BY "core_book"."name" ASC
```

http://blog.roseman.org.uk/2010/05/10/django-aggregation-and-simple-group/

http://henriquebastos.net/agregacoes-condicionais-com-django-aggregate-if/

Aggregate
=========

Aggregate
---------

Annotate
--------

### Anotações

null

Se True, o Django irá gravar valores vazios como NULL no banco de dados. O padrão é False.

Use o null=True apenas para campos que não sejam texto, como inteiros, booleanos e datas.

blank

Se True, o campo pode ser vazio. o padrão é False.

Note que isso é diferente de null. null é puramente relacionado ao banco de dados, e blank é relacionado com validação. Se um campo tem blank=True, a validação na administração do Django irá permitir a entrada de um valor vazio. Se um campo tem blank=False, o campo será obrigatório.


https://django-portuguese.readthedocs.org/en/1.0/ref/models/fields.html