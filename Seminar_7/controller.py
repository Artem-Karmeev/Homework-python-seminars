from view import input_num_menu, input_contact
from model import dp
from view import dp_po
import view
def my_menu():

    while True:
        user_nam = input_num_menu()

        if user_nam == 1:
            phone_book = dp.get()
            dp_po.show_contacts(phone_book)
        elif user_nam == 2:
            dp.open()
            dp_po.open_print()
        elif user_nam == 3:
            dp.save()
            dp_po.save_print()
        elif user_nam == 4:
            li = input_contact()
            dp.update(li)
        # elif user_nam == 5:
        #     pass
        # elif user_nam == 6:
        #     pass
        elif user_nam == 7:
            str_search = view.inpyt_search()
            dp.search(str_search)


        elif user_nam == 8:
            print('Пока-пока!')
            break
