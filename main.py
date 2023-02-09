"""
Author: Aleh Hubarevich
Date:9/2/2023


Project Assignment:
The WorldSeriesWinners.txt contains a chronological list of the World Series winning teams from 1903 through 2009. 
(The first line in the file is the name of the team that won in 1903, and the last line is the name of the team 
that won in 2009. Note the World Series was not played in 1904 or 1994.)
Write a program that lets the user enter the name of a team, then displays the number of times that team has won 
the World Series in the time period from 1903 through 2009.
"""

#main function
def main():
    #Declare Variables
    team = input('enter a team: ')
    year = int(1903)
  
    #Initialize "lists"
    list = []
    list_2 = []
    nested_list = []
    years = []

    #Try and Except
    try:
        file = open('WorldSeriesWinners.txt', 'r')
        for string in file:
            list.append(string.rstrip())
        file.close
        list.insert(1, 'the World Series was not played')
        list.insert(91, 'the World Series was not played')
        for item in list:
            nested_list = [year, item]
            year += 1
            list_2.append(nested_list)
            if item == team:
                print('*', nested_list)
                years.append(nested_list[0])
            else:
                print(' ', nested_list)
        print(f'{"=" * 40}')
        print(f'{team} win the World Series {len(years)} times. In {years}')
    
    #Handdle File not Found Error
    except FileNotFoundError:
        print("File does not exist")
main()