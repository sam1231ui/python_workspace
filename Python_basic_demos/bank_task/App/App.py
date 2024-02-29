from SilverCard import SilverCard
from GoldCard import GoldCard


# inner menu of app
def inner_menu(client):
    while True:
        print("1)View \n2)Withdraw \n3)Deposit \n4)Increase Limit \n5)Exit")
        choice = input("Please enter your choice\n")
        match choice:
            case '1':
                client.show()
            case '2':
                print(client.withdraw(int(input("Enter Amount to be withdraw \n"))))
            case '3':
                print(client.deposit(int(input("Enter Amount to be deposited \n"))))
            case '4':
                print(client.increase_limit())
            case '5':
                break


# app main menu
def app():
    while True:
        choice = input("Menu\n 1)Silver-Card\n 2)Gold-Card\n 3)Exit\n")
        match choice:
            case '1':
                inner_menu(SilverCard())
            case '2':
                inner_menu(GoldCard())
            case '3':
                break


# call to app function
app()
