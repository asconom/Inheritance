import PersonClass as pc

general_person = pc.Person("Adam", "1410 S 10th st", "123-456-7890")

customer_person = pc.Customer("Aidan", "1410 S 10th st", "214-799-3743", 123, True)

general_person.print_person()
customer_person.print_person()
