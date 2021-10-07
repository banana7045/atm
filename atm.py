class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 60")

    def withdrawl(self,amount):
        new_amount = 60 - amount
        print("you've successfully wihdrawn "+str(amount) +". You now have "+ str(new_amount))


def main():
    Card_number = input("Enter a card number: ")
    pin_number  = input("Enter a pin number: ")

    new_user =  Atm(Card_number ,pin_number)

    print("Pick an option below: ")
    print(" 1.) balance   2.) withdraw")
    task = int(input("Input the number your choice has here: "))

    if (task == 1):
        new_user.check_balance()
    elif (task == 2):
        amount = int(input("enter the amount: "))
        new_user.withdrawl(amount)
    else:
     print(" (WIP) ")


if __name__ == "__main__":
    main()