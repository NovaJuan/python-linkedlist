# Here we create the logic to handle all the list functionality

import csv
import platform
import sys
import os
from linkedlist import LinkedList
from data_type import User

users = LinkedList(User)


def clear_terminal():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Darwin' or system == 'Linux':
        os.system('clear')


def load_data():
    "Load data (if exists) from csv set put into the Linked list"
    try:
        with open('scraper/people.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.insert(name=row['Name'], age=row['Age'])
    except FileNotFoundError:
        pass


def setup():
    clear_terminal()
    print('\nWelcome to this Linked list test.')
    print('You can create and manage your list of friends here.')

    set_placeholder = input(
        '\nWant to add some placeholder friends? Y or N: ')

    if set_placeholder == 'Y' or set_placeholder == 'y':
        print('\nSetting up data...')
        load_data()


def add_user():
    name = input('\nFriend\'s name: ')
    age = input('Friend\'s age: ')
    users.append(name=name, age=age)
    print(f'\n{name} was added to your list.')


def list_all_users():
    print('\nYour list of friends')
    if len(users) == 0:
        return print('No friends in your list.')

    row = ''
    for i in range(len(users)):
        row = row + ('%3d.%-12s ' % (i + 1, users[i].name))
        if (i + 1) % 3 == 0:
            row = row + '\n'

    print(row)


def get_one_user():
    if len(users) == 0:
        return
    try:
        index = int(input('\nEnter the index: '))
        user = users[index - 1]

        print(f'\nYour friend is called {user.name},')
        print(f'and is {user.age} years old.')
    except (IndexError, ValueError):
        print('\nThat index is not in the list.')


def remove_user():
    if len(users) == 0:
        return
    try:
        index = int(input('\nEnter the index: '))
        user = users[index - 1]
        users.remove(index - 1)

        print(f'\n{user.name} was removed.')
    except (IndexError, ValueError):
        print('\nThat index is not in the list.')
