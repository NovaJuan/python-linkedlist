# Project Description:
# Linked List in python using recursivity (almost)
# This is the main file where all is executed
import controllers as ctrls

# Prep to start, load data if required
ctrls.setup()


def main():
    print("""
        \nChoose one option:
        (1) To add a new friend:
        (2) To see the list of your friends:
        (3) To get one friend:
        (4) To remove a friend:
        (5) Exit
    """)
    opt = input('\nOption = ')

    ctrls.clear_terminal()
    if opt == '1':
        ctrls.add_user()
    elif opt == '2':
        ctrls.list_all_users()
        pass
    elif opt == '3':
        ctrls.list_all_users()
        ctrls.get_one_user()
    elif opt == '4':
        ctrls.list_all_users()
        ctrls.remove_user()
    elif opt == '5':
        print('\n Bye!')
        return
    else:
        print('\nThat option doesn\'t exists.')

    return main()


# Start the CLI loop
main()
