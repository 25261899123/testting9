"""Дан список стран и городов каждой страны. Затем даны названия городов. Для
каждого города укажите, в какой стране он находится."""

# cities = {'Bishkek':'Kyrgyzstan','Almata':'Kazakstan','London':'United Kingdom'}


# cities['Russia'] = 'Moscow'
# cities['Ukraine'] = 'Kiev'
# cities['USA'] = 'Washington'
# print(cities)


# print('В каком городе вы живете?')
# country = input()


# if country in cities:

#     print('этот город страны', cities[country])

strany = [{ 'kyrgyz' : ["talas", "bishkek"]}, {'kaz' : ["almaty", "pavlodar"]}, {'USA' : ["washington", "brooklyn"]}]
for strana in strany:
    for city in strana:
        print()
    