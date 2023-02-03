from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from API import models, repositories


class CategoryServicesInterface(Protocol):
    repos: repositories.CategoryRepositoriesInterface

    def get_list(self) -> QuerySet[models.Category]: ...

    def create(self, data: OrderedDict) -> models.Category: ...


class CategoryServices:
    repos: repositories.CategoryRepositoriesInterface = repositories.CategoryRepositories()

    def get_categories(self) -> QuerySet[models.Category]:
        return self.repos.get_list()

    def get_category_products(self, category_id: int) -> QuerySet[models.Product]:
        return self.repos.get_products(category_id)

    def create_category(self, data: OrderedDict) -> models.Category:
        return self.repos.create(data)


class ProductServicesInterface(Protocol):
    repos: repositories.ProductRepositoriesInterface

    def get_list(self) -> QuerySet[models.Product]: ...

    def create(self, data: OrderedDict) -> models.Product: ...


class ProductServices:
    repos: repositories.ProductRepositoriesInterface = repositories.ProductRepositories()

    def get_products(self) -> QuerySet[models.Product]:
        return self.repos.get_list()

    def create_product(self, data: OrderedDict) -> models.Product:
        return self.repos.create(data)
