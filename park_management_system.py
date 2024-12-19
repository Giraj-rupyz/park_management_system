

class park_management():
    visitors = []
    discount_for_men = 0
    discount_for_women = 0
    discount_for_children = 0
    price_for_adults = 0
    price_for_teenagers = 0
    price_for_children = 0
    amount_collected = 0

    # function to set discount

    def set_discount(self, discount_for_men, discount_for_women, discount_for_children):
        self.discount_for_men = discount_for_men
        self.discount_for_women = discount_for_women
        self.discount_for_children = discount_for_children

    # function to set price
    def set_price(self, price_for_adults, price_for_teenagers, price_for_children):
        self.price_for_adults = price_for_adults
        self.price_for_teenagers = price_for_teenagers
        self.price_for_children = price_for_children

    # function for booking

    def book_ticket(self, name, age, phone, gender):
        visitors_map = {"name": name, "age": age, "phone": phone, "gender": gender}
        price_before_discount = 0
        price_after_discount = 0

        # calculating prices after discount as per age and gender
        if age > 20 and gender == "male":
            price_before_discount = self.price_for_adults
            price_after_discount = price_before_discount-((self.discount_for_men/100)*price_before_discount)
        elif age > 20 and gender == "female":
            price_before_discount = self.price_for_adults
            price_after_discount = price_before_discount-((self.discount_for_women/100)*price_before_discount)
        else:
            if age > 10 and age <= 20:
                price_before_discount = self.price_for_teenagers
                price_after_discount = price_before_discount-((self.discount_for_children/100)*price_before_discount)
            else:
                price_before_discount = self.price_for_children
                price_after_discount = price_before_discount-((self.discount_for_children/100)*price_before_discount)

        print(f"Price to be paid {price_after_discount}")
        print()
        print("******Processing payment*******")
        print()
        print("Payment Successful! Welcome to the park ")
        print()
        print()
        print()
        self.visitors.append(visitors_map)

    # function to display prices

    def display_prices(self):
        print(f"price for people below 10 years: {self.price_for_children}")
        print(f"Price for people between 10 to 20 years: {self.price_for_teenagers}")
        print(f"Price for people above 20 years: {self.price_for_adults}")
        print()
        print()
        print()

    # function to display discounts
    def display_discounts(self):
        print(f"There is a discount of {self.discount_for_men}% for all mens")
        print(f"There is a discount of {self.discount_for_women}% for all women")
        print(f"There is a discount of {self.discount_for_children}% for all children below 20")
        print()
        print()
        print()

    # function to see number of visitors
    def visitors_count(self):
        print(f"Total visitors in the park: {len(self.visitors)}")
        print()
        print()
        print()


def main():
    # admin control
    park_system = park_management()
    park_system.set_discount(10, 30, 50)
    park_system.set_price(500, 300, 100)

    # user panel

    while True:
        print("1. booking", end="      ")
        print("2. view prices", end="       ")
        print("3. view offers", end="       ")
        print("4. see number of visitors", end="        ")
        print("5. exit")
        user_choice = int(input("Enter your choice "))
        print()
        print()
        print()

        if user_choice == 1:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            if age < 0:
                print()
                print("Enter valid age")
                print()
                print("Enter your details again")
                print()
                print()
                print()
                continue

            phone = input("Enter your phone number: ")
            if len(phone) != 10:
                print()
                print("Enter a valid phone number")
                print()
                print("Enter your details again")
                print()
                print()
                print()
                continue
            gender = input("Enter your gender (male/female): ")
            if gender == 'male' or gender == 'female':
                print()
                park_system.book_ticket(name, age, phone, gender.lower())

            else:
                print()
                print("Please enter your gender in the given format only")
                print()
                print("Enter your details again")
                print()
                print()
                print()
                continue

        elif user_choice == 2:
            park_system.display_prices()

        elif user_choice == 3:
            park_system.display_discounts()

        elif user_choice == 4:
            park_system.visitors_count()

        elif user_choice == 5:
            break


if __name__ == "__main__":
    main()
