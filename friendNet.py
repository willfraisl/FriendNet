# Final Project for Design and Analysis of Computer Algorithms
# Will Fraisl
# Erik Fox
# Emma Delucchi

'''
Dijkstra’s Shortest Path First algorithm is likely the algorithm that we will need to use, 
and we may need to transform the data into a matrix to use this algorithm and flip the 
values so that 0 is best friend and 10 is worst friend when doing the calculation.

Killer feature #1: Microtransactions
If you want to increase your friendship with someone, we will prompt you to enter 
a sum of money. That money will bump you up on someone’s list by a certain amount. 

Killer feature #2: Find the best group of friends
Enter a size of group, we will find the closest group of friends of this size. 
Everyone in the group has to be friends with each other. 

'''

import csv


def user_exists(graph, user):
    if user in graph:
        return True
    else:
        return False


def get_connection(graph, user1, user2):
    for friend in graph[user1]:
        if friend[0] == user2:
            return friend[1]
    return 0


def print_dictionary(dictionary):
    for key in dictionary.keys():
        print(key, ":", dictionary.get(key))


def read_friends(file_name):
    graph = {}
    with open(file_name) as f:
        data_list = f.readlines()

    for line in data_list:
        temp = line.split()
        friend_list = graph.get(temp[0], [])
        friend_list.append((temp[1], int(temp[2])))
        graph.update({temp[0]: friend_list})
    return graph


def menu_interface(graph):
    while(True):
        print('\nWhat do you want to do?')
        print('1) Check if user exists')
        print('2) Check connection between users')
        print('3) Quit')
        inp = input('> ')
        if inp == '1':
            user = input('What user? ')
            if user_exists(graph, user):
                print(user, 'does exist.')
            else:
                print(user, 'does not exist.')
        elif inp == '2':
            names = input('What users (separated by spaces)? ')
            names = names.split(' ')
            weight = get_connection(graph, names[0], names[1])
            print('The connection from',
                  names[0], 'to', names[1], 'has weight', weight)
        else:
            break


def main():
    graph = read_friends("friendNet.txt")
    print_dictionary(graph)
    menu_interface(graph)


if __name__ == '__main__':
    main()
