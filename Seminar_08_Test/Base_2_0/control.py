import model as m
import menu


def start():
    students = m.read_csv()
    stud = {}
    while True:
        choice = menu.show_menu()
        if choice == 2:
            stud = m.find_stud(students)
            if not stud:
                print('There is no such student')
            else:
                print(stud)
        elif choice == 1:
            m.show_base()
        elif choice == 4:
            stud = m.stud_by_grant(students)
            print(stud)
        elif choice == 5:
            stud = m.add_stud(students)
            m.show_base()
        elif choice == 6:
            stud = m.del_stud(students)
            m.show_base()
        elif choice == 7:
            stud = m.upd_stud(students)
            m.show_base()
        elif choice == 8:
            m.exp_json()
            print('Database exported to json')
        elif choice == 9:
            m.exp_xlsx()
            print('Database exported to xlsx')
        else:
            quit()