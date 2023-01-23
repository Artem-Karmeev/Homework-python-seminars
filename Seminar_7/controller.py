from view import input_num_menu, input_contact
from model import dp
from view import po
import view
def my_menu():

    while True:
        user_nam = input_num_menu()

        if user_nam == 1:
            phone_book = dp.get()
            po.show_contacts(phone_book)

        elif user_nam == 2:
            dp.open()
            po.open_print()

        elif user_nam == 3:
            dp.save()
            po.save_print()

        elif user_nam == 4:
            li = input_contact()
            dp.update(li)

        elif user_nam == 5:
            str_search = view.inpyt_search()
            li = dp.search_index(str_search)
            po.show_i_contacts(li)
            index = view.del_item(li)
            res_li = input_contact()
            dp.change(res_li, index)

        elif user_nam == 6: 
            str_search = view.inpyt_search()
            li = dp.search_index(str_search)
            po.show_i_contacts(li)
            index = view.del_item(li)
            dp.delete(index)

        elif user_nam == 7:
            str_search = view.inpyt_search()
            li = dp.search(str_search)
            po.show_contacts(li)

        else:
            res = dp.check_changes()
            if res:
                break
            else:
                user_res = view.making_changes()
                if user_res:
                    dp.save()
                    po.save_print()
                    break
                else:
                    break

