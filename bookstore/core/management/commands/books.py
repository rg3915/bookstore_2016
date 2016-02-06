import random
import string
import requests
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from optparse import make_option
from core.models import Book


class Command(BaseCommand):
    help = """Faz o crawler numa api de livros e retorna os dados.
    Uso: python manage.py books
    ou: python manage.py books -b 20"""
    option_list = BaseCommand.option_list + (
        make_option('--books', '-b',
                    dest='books',
                    default=10,
                    help='Define a quantidade de livros a ser inserido.'),
    )

    def print_red(self, name):
        """imprime em vermelho"""
        print("\033[91m {}\033[00m".format(name))

    def get_html(self):
        """
        Le os dados na api http://extracts.panmacmillan.com/getextracts de forma aleatoria
        e escolhe um livro buscando por 3 letras
        """
        # Escolhe tres letras aleatoriamente
        letters = ''.join(random.choice(string.ascii_lowercase)
                          for _ in range(3))
        # define a url
        # url = 'http://extracts.panmacmillan.com/getextracts?authorcontains={letters}'.format(letters=letters)
        url = 'http://extracts.panmacmillan.com/getextracts?authorcontains=exu'
        # print(letters)
        return requests.get(url).json()

    def get_book(self):
        """ Retorna um dicionário do livro """
        book = self.get_html()
        j = 1  # contador
        # Faz a validação de Extracts. Se o resultado for vazio, então busca outro
        # livro.
        while len(book) == 0 and j < 100:
            book = self.get_html()
            print('Tentando %d vezes\n' % j)
            j += 1
        return book

    def handle(self, books, **options):
        if books is not None:
            books = int(books)

        # busca os livros n vezes, a partir da variavel "books"
        for i in range(2):
            b = self.get_book()
            print(b['Extracts'])
