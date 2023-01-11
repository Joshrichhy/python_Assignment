from practice.Class_declaration import Human

if __name__ == '__main__':
    name = input("Enter Name: ")
    Age = int(input("Enter Age: "))
    person = Human(name, Age)
    print("My name is", person.get_name(), "age is ", person.get_age())