class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def print_person(self):
        print("Name:", self.__name)
        print("Address:", self.__address)
        print("Phone Number:", self.__phone)


class Customer(Person):
    def __init__(self, name, address, phone, cust_num, mail):
        Person.__init__(self, name, address, phone)

        self.__customer_number = cust_num
        self.__boolean_data_attribute = mail

    def print_person(self):
        Person.print_person(self)
        print("Customer Number:", self.__customer_number)
        print("Mailing List y/n:", self.__boolean_data_attribute)
