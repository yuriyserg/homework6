my_dict = {'Yura': 1985, 'Ira': 1995, 'Inokenty': 1874}
print(my_dict)
print(my_dict['Yura'])
print(my_dict.get('Prohor'))
my_dict.update({'Potap': 1901, 'Stephan': 2023})
a = my_dict.pop('Inokenty')
print(a)
print(my_dict)
my_set = {1, 2, 3, 'String', True, 3, 1}
my_set.add(7)
my_set.add(False)
my_set.remove(2)
print(my_set)