from typing import Protocol, OrderedDict
import collections

from django.db.models import QuerySet

from API import models


class CategoryRepositoriesInterface(Protocol):
    model: models.Category

    def get_list(self) -> QuerySet[models.Category]: ...

    @staticmethod
    def get_products(category_id: int) -> QuerySet[models.Product]: ...

    def create(self, data: OrderedDict) -> models.Category: ...


class CategoryRepositories:
    model: models.Category = models.Category

    def get_list(self) -> QuerySet[models.Category]:
        return self.model.objects.all()

    @staticmethod
    def get_products(category_id: int) -> QuerySet[models.Product]:
        repos = ProductRepositories()
        return repos.get_list(collections.OrderedDict({'category_id': category_id}))

    def create(self, data: OrderedDict) -> models.Category:
        return self.model.objects.create(**data)


class ProductRepositoriesInterface(Protocol):
    model: models.Product

    def get_list(self) -> QuerySet[models.Product]: ...

    def create(self, data: OrderedDict) -> models.Product: ...


class ProductRepositories:
    model: models.Product = models.Product

    def get_list(self, filters: OrderedDict = None) -> QuerySet[models.Product]:
        if filters is None:
            filters = {}

        return self.model.objects.filter(**filters).all()

    def create(self, data: OrderedDict) -> models.Product:
        return self.model.objects.create(**data)
