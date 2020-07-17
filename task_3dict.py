"""Дан словарь, состоящий из элементов типа: слово-синоним. Все слова в словаре
различны. Выведите синоним для последнего слова."""
dict_= {"asman": "nebo","jer":"zemlya","kola":"pepsi"}
new = (dict_.popitem())
dict_.values()
print(dict_)
print(new)