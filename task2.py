"""Дан список, состоящая ровно из двух строк. Переставьте эти слова местами. Результат запишите
в список и выведите получившийся список."""
Spisok = [1, 2, 3],[5, 6, 7]
Dlinna = len(Spisok)
half = Dlinna /2
half_ = int(half)
half2 = (Spisok[half_:])
half1 = (Spisok[:half_])
print ([half2] + [half1])