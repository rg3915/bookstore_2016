null

Se True, o Django irá gravar valores vazios como NULL no banco de dados. O padrão é False.

Use o null=True apenas para campos que não sejam texto, como inteiros, booleanos e datas.

blank

Se True, o campo pode ser vazio. o padrão é False.

Note que isso é diferente de null. null é puramente relacionado ao banco de dados, e blank é relacionado com validação. Se um campo tem blank=True, a validação na administração do Django irá permitir a entrada de um valor vazio. Se um campo tem blank=False, o campo será obrigatório.


https://django-portuguese.readthedocs.org/en/1.0/ref/models/fields.html