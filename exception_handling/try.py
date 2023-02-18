try:
    filename = open("path", "r")
    filename.write("hello")
except IOError:
    print("can not write to closed file")

    import pickle

    from diaryApplication.diary import diary

my_diary = diary()

if __name__ == '__main__':

        try:
            with open("Joshpick.pkl", 'rb') as file:
                my_diary = pickle.load(file)
                print(my_diary.get_pages_in_diary())

        except:
            print("you are high")
            print(my_diary.get_pages_in_diary())

        my_diary.create_entry("Progress so far", "Let us see "
                                                 "the progress of "
                                                 "what we have done so far")
        print(my_diary.get_pages_in_diary())
        print(my_diary.find_entry(1))

        exit(1)

        with open("Joshpick.pkl", 'wb') as file:
            pickle.dump(my_diary, file)


