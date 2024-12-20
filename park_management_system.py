

class ParkManagement():
    """This class manages bookings, display prices, tickets and offers for user and sets price and discount for admin.
    """
    _visitors = []
    _discount_for_men = 0
    _discount_for_women = 0
    _discount_for_children = 0
    _price_for_adults = 0
    _price_for_teenagers = 0
    _price_for_children = 0
    _amount_collected = 0
    _id = 0

    # function to set discount

    def _set_discount(self, _discount_for_men, _discount_for_women, _discount_for_children):
        """This function is for admin. It is use to set discount.

        Args:
            _discount_for_men (int): _This argument is used to set discount for men_
            _discount_for_women (int): _This argument is used to set discount for women_
            _discount_for_children (int): _This argument is used to set discount for children_
        """
        self._discount_for_men = _discount_for_men
        self._discount_for_women = _discount_for_women
        self._discount_for_children = _discount_for_children

    # function to set price
    def _set_price(self, _price_for_adults, _price_for_teenagers, _price_for_children):
        """This function is for admin. It is use to set prices according to age.

        Args:
            _price_for_adults (_type_): sets price for adults.
            _price_for_teenagers (_type_): _sets price for teenagers
            _price_for_children (_type_): sets price for children
        """
        self._price_for_adults = _price_for_adults
        self._price_for_teenagers = _price_for_teenagers
        self._price_for_children = _price_for_children

    def book_ticket(self, name, age, phone, gender):
        """This function is used to book tickets and calculates price based on the user's data)

        Args:
            name (str): name of the user
            age (int): age of the user
            phone (str): user's contact number
            gender (str): gender of the user (male/female)
        """
        visitors_map = {"name": name, "age": age, "phone": phone, "gender": gender}
        price_before_discount = 0
        price_after_discount = 0

        # calculating prices after discount as per age and gender
        if age > 20 and gender == "male":
            price_before_discount = self._price_for_adults
            price_after_discount = price_before_discount-((self._discount_for_men/100)*price_before_discount)
        elif age > 20 and gender == "female":
            price_before_discount = self._price_for_adults
            price_after_discount = price_before_discount-((self._discount_for_women/100)*price_before_discount)
        else:
            if age > 10 and age <= 20:
                price_before_discount = self._price_for_teenagers
                price_after_discount = price_before_discount-((self._discount_for_children/100)*price_before_discount)
            else:
                price_before_discount = self._price_for_children
                price_after_discount = price_before_discount-((self._discount_for_children/100)*price_before_discount)

        print(f"Price to be paid {price_after_discount} \n")
        user_payment_choice = input("Do you want to pay (yes/no): ")
        print()
        if user_payment_choice == 'yes':
            print("****** Processing payment ******\n")
            print("Payment Successful! Welcome to the park\n\n\n")
            self._id += 1
            visitors_map['id'] = self._id
            self._visitors.append(visitors_map)
        elif user_payment_choice == 'no':
            print("we will be glad to have you on board next time!\n\n\n")

    # function to display prices

    def display_prices(self):
        """This function is used to display prices for users.
        """
        print(f"price for people below 10 years: {self._price_for_children}")
        print(f"Price for people between 10 to 20 years: {self._price_for_teenagers}")
        print(f"Price for people above 20 years: {self._price_for_adults}\n\n\n")
        # print()
        # print()
        # print()

    # function to display discounts
    def display_discounts(self):
        """This function is used to display discounts for users.
        """
        print(f"There is a discount of {self._discount_for_men}% for all mens")
        print(f"There is a discount of {self._discount_for_women}% for all women")
        print(f"There is a discount of {self._discount_for_children}% for all children below 20 \n\n\n")
        # print()
        # print()
        # print()

    # function to see number of visitors
    def visitors_count(self):
        """This function is used to show number of visitors in the park.
        """
        print(f"Total visitors in the park: {len(self._visitors)} \n\n\n")
        # print()
        # print()
        # print()

    def view_ticket_by_id(self, id):
        """This function is used to view details of the visitor by id.

        Args:
            id (int): ID of the visitor.
        """
        if id > 0:
            for visitor in self._visitors:
                if visitor['id'] == id:
                    print(f"Name: {visitor['name']}")
                    print(f"Age: {visitor['age']}")
                    print(f"Gender: {visitor['gender']}")
                    print(f"Phone: {visitor['phone']}\n\n\n")
                    break
        else:
            print("Enter a valid id\n\n\n")


def main():
    # admin control
    park_system = ParkManagement()
    park_system._set_discount(10, 30, 50)
    park_system._set_price(500, 300, 100)

    # user panel

    while True:
        print("1. booking\t\t", end="")
        print("2. view prices\t\t", end="")
        print("3. view offers\t\t", end="")
        print("4. see number of visitors\t\t", end="")
        print("5. view ticket")
        print("6. exit")
        user_choice = int(input("Enter your choice "))
        print("\n\n\n")
        # print()
        # print()

        if user_choice == 1:
            name = input("Enter your name: ")
            age = int(input("Enter your age:"))
            if age < 0:
                print()
                print("Enter valid age \n")
                # print()
                print("Enter your details again \n\n\n")
                # print()
                # print()
                # print()
                continue

            phone = input("Enter your phone number: ")
            if len(phone) != 10:
                print()
                print("Enter a valid phone number\n")
                # print()
                print("Enter your details again \n\n\n")
                # print()
                # print()
                # print()
                continue
            gender = input("Enter your gender (male/female):")
            if gender == 'male' or gender == 'female':
                print()
                park_system.book_ticket(name, age, phone, gender.lower())

            else:
                print()
                print("Please enter your gender in the given format only \n")
                # print()
                print("Enter your details again \n\n\n")
                # print()
                # print()
                # print()
                continue

        elif user_choice == 2:
            park_system.display_prices()

        elif user_choice == 3:
            park_system.display_discounts()

        elif user_choice == 4:
            park_system.visitors_count()

        elif user_choice == 5:
            id = int(input("Enter your id: "))
            print('\n')
            park_system.view_ticket_by_id(id)


if __name__ == "__main__":
    main()
