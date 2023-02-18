import pickle

from diaryApplication.diary import diary

my_new_diary = diary()


def create_entry_in():
    title = input("Enter your Entry title")
    body = input("What are you writing today?")

    my_new_diary.create_entry(title, body)
    print("Entry created successfully")
    go_to_main_menu()


def view_entry_in():
    idNumber = int(input("Enter your id Number"))
    print("Hi, here is your entry")
    print(my_new_diary.find_entry(idNumber))
    go_to_main_menu()


def edit_entry():
    print("not available")
    go_to_main_menu()


def count_entry():
    numberOfEntries = my_new_diary.get_pages_in_diary()
    print("You have", numberOfEntries, "numbers of entries in your diary")
    go_to_main_menu()


def delete_entry_in():
    idNumber = int(input("Enter Your entry id you want to delete"))
    my_new_diary.delete_entry(idNumber)
    print("Entry deleted successfully")
    go_to_main_menu()


def view_all_entry_in_diary():
    my_new_diary.view_diary()
    go_to_main_menu()


def over_write_entry_in():
    go_to_main_menu()


def exit_application():
    save_file()


def save_file():
    print("Thank you for using our application ")
    with open("entries.pkl", 'wb') as diary_of_file:
        pickle.dump(my_new_diary, diary_of_file)
        diary_of_file.close()


def go_to_main_menu():
    mainMenu = int(input("""
                    ===================================
                    THIS IS MY DIARY
                    1 -> Create Entry
                    2 -> View Entry
                    3 -> Edit Entry
                    4 -> Count Entry
                    5 -> Delete Entry
                    6 -> View All Entries
                    7 -> overWrite Entry 
                    8 -> Exit"
                     ===================================
                    """))

    match mainMenu:
        case 1:
            create_entry_in()

        case 2:
            view_entry_in()

        case 3:
            edit_entry()

        case 4:
            count_entry()

        case 5:
            delete_entry_in()

        case 6:
            view_all_entry_in_diary()

        case 7:
            over_write_entry_in()

        case 8:
            exit_application()

        case other:
            go_to_main_menu()


if __name__ == '__main__':
    try:
        with open("entries.pkl", 'rb') as diary_file:

            my_new_diary = pickle.load(diary_file)
    except:
        print("Reloading...")

    go_to_main_menu()
