#10. World Series Champions

file = open('WorldSeriesWinners.txt', 'r')
list = []
for string in file:
    list.append(string.rstrip())
file.close
list.insert(1, 'the World Series was not played')
list.insert(91, 'the World Series was not played')
y = int(1903)
nested_list = []
list_2 = []
years = []
n = input('enter a team: ')
for item in list:
    nested_list = [y, item]
    y += 1
    list_2.append(nested_list)
    if item == n:
        print('*', nested_list)
        years.append(nested_list[0])
    else:
        print(' ', nested_list)
print(f'{"=" * 40}')
print(f'{n} win the World Series {len(years)} times. In {years}')