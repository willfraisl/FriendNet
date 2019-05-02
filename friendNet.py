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
import copy

def best_friend_group(graph, group_size):
    poss_groups = generate_groups(graph, group_size)
    valid_groups = []
    for group in poss_groups:
        if is_valid_group(graph, group):
            valid_groups.append(group)

    best_group = []
    best_score = 0
    for group in valid_groups:
        curr_score = 0
        for i, user in enumerate(group):
            for friend in group[:i] + group[i+1:]:
                for other_friend, score in graph[user]:
                    if friend == other_friend:
                        curr_score += score
        if curr_score > best_score:
            best_score = curr_score
            best_group = group

    return best_group      
    
def is_valid_group(graph, group):
    for i, user in enumerate(group):
        for other_friend in group[:i] + group[i+1:]:
            # needs to look at first element of tuples
            if other_friend not in graph[user]:
                return False
    return True


def pay_to_win(graph):
    name = ''
    while True:
        print('Please enter your name:')
        name = input('> ')
        #name = 'Emma'
        if user_exists(graph, name):
            print(f"You have chosen {name}")
            break
        print("This user does not exist! Try again!")

    rating_avg = {}
    for user in graph:
        # Verify that this order is right... you want the name to be the requester
        if get_connection(graph, user, name) != 0 and get_connection(graph, user, name) != 0:     
            sum_values = 0
            num = 0
            for names in graph[user]:
                sum_values += names[1]
                num += 1
            rating_avg[user] = sum_values/num

    requester_eval = {}
    differences = {}
    for person in rating_avg:
        # person is now the key name
        requester_eval[person] = get_connection(graph, person, name)
        temp_diff = rating_avg[person] - requester_eval[person]
        if temp_diff >= 0:
            differences[person] = temp_diff

    max_diff_key = max(differences.keys(), key=(lambda k: differences[k]))
    #print(max_diff_key)
    print(f"The biggest difference between you and how {max_diff_key} rates you is {differences[max_diff_key]}")
    print("Right now we have great deal you may want to consider! For each point you are differently rated, you can pay $1 to change that!")
    print("Enter how much you want to bump up your rating (0 for none, you can't go more than you are at a deficit):")
    inp = 0
    while True:
        try:
            inp = int(input('> '))
            break
        except ValueError:
            print("The input was either invalid or too high. Try again!")
    print(graph[max_diff_key])
    print(f"Ok! You increased your friendship by {inp}")


def best_friend_chain(graph, name1, name2):
    result = dijkstra(graph, name1, name2)
    if result == []:
        print('No path to connect these people.')
    else:
        print('The best friend chain is', ', '.join(result))


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

    for i, line in enumerate(data_list):
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
        print('3) Pay to increase your status')
        print('4) Quit')
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
        elif inp == '3':
            pay_to_win(graph)
        else:
            break


def dijkstra(graph, source, destination):
    inf = float("inf")
    Q = set()
    dist = {}
    prev = {}
    for vertex in graph.keys():
        dist[vertex] = inf
        prev[vertex] = None
        Q.add(vertex)
    dist[source] = 0

    while len(Q) > 0:
        smallest = inf
        smallest_node = Q
        for node in Q:
            print(node, dist[node], smallest)
            if dist[node] <= smallest:
                smallest = dist[node]
                smallest_node = node
        u = smallest_node

        Q.remove(u)

        for v, weight in graph[u]:
            alt = dist[u] + 10 - weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    u = destination
    path = []
    if(prev[u] != None or u == source):
        while(u):
            path.insert(0, u)
            u = prev[u]
    return path


def getCostMatrix(graph, IDDict):
    inf = float("inf")
    matrix = [[]]*len(IDDict)
    print(matrix)
    for item in graph.keys():
        print(item, getID(item, IDDict))
        matrix[getID(item, IDDict)] = ([inf]*len(IDDict))
        for value in graph.get(item):
            print(value, getID(value[0], IDDict))
            matrix[getID(item, IDDict)][getID(value[0], IDDict)] = 10-value[1]
    return matrix


def createIDDict(graph):
    IDDict = {}
    for i, key in enumerate(graph.keys()):
        IDDict.update({key: i})
    return IDDict


def getID(name, IDDict):
    return IDDict.get(name)


def generate_groups(graph, group_size):
    users = graph.keys()

    groups = []
    return groups

   
def generate_groups_helper(graph,groupSize):
    users = list(graph.keys())
    group = list(range(3))
    return generate_groups(users,groupSize,0,group,0,[])

def generate_groups(users,groupSize,groupIndex,data,userIndex,groupsList): 
    # add filled group to the list 
    if(groupIndex == groupSize): 
        groupsList.append(copy.deepcopy(data))
        return groupsList
  
    # don't exceed group size
    if(userIndex >= len(users)): 
        return groupsList
  
    # add current person to group and recurse  
    data[groupIndex] = users[userIndex]
    generate_groups(users, groupSize, groupIndex + 1, data, userIndex + 1,groupsList) 
      
    # move to next person and recurse
    generate_groups(users, groupSize, groupIndex, data, userIndex + 1,groupsList)

    return groupsList

def main():
    graph = read_friends("friendNet.txt")
    #print_dictionary(graph)
    #best_friend_chain(graph, 'Coe', 'Tony')
    #menu_interface(graph)
    print(generate_groups_helper(graph,3))


if __name__ == '__main__':
    main()
