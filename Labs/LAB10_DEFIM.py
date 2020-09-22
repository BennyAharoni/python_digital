from time import sleep


#choise 2 menu
def search_ip():
    print("search_ip")


def add_ip():
    print("add_ip")


def delete_ip():
    print("delete_ip")


def print_ip():
    print("print_ip")


#choice 3 menu
def search_url():
    print("search_url")


def add_url():
    print("add_url")


def delete_url():
    print("delete_url")


def update_ip_of_url():
    print("update_ip_of_url")


def print_dict():
    print("print_dict")


def menu():
    while(True):
        choice1 = input("Menu:\n----------------\na. IP System\nb. DNS System\n")
        if choice1 == "a":
            choice2 = input("\nMenu IP System:\n----------------\n1. Search for IP address from a list\n"
                            "2. Add IP address to a list\n"
                            "3. pDelete IP address to a list\n"
                            "4. Print all the IPs to the screen\n")
            if choice2 == "1":
                search_ip()
            elif choice2 == "2":
                add_ip()
            elif choice2 == "3":
                delete_ip()
            elif choice2 == "4":
                print_ip()
        elif choice1 == "b":
            choice3 = input("\nMenu DNS System:\n----------------\n1. Search for URL from a dictionary\n"
                            "2. Add URL + IP address to a dictionary\n"
                            "3. Delete URL from a dictionary\n"
                            "4. Update the IP address of specific URL\n"
                            "5. Print all the URL:IP to the screen\n")
            if choice3 == "1":
                search_url()
            elif choice3 == "2":
                add_url()
            elif choice3 == "3":
                delete_url()
            elif choice3 == "4":
                update_ip_of_url()
            elif choice3 == "5":
                print_dict()
        else:
            print("Enter a or b only!!")
            continue
        exit = input("Do you want to exit? y/n: ")
        if exit == "y":
            print("Bye bye!!")
            break
        else:
            continue

