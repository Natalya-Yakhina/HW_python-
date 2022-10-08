# import view
# import imp
# import exp
# import logger

# def run():
#      temp = view.choice()
#      if temp == 1:
#           print ('Новый сотрудник')
#           entry = imp.record() # Запись в справочник
#           logger.log_to_file(entry)
#           run()
#      if temp == 2:
#           print ('\n Поиск сотрудника\n' )
#           entry = exp.search() # Поиск в справочнике
#           logger.reading_file(entry)
#           run()
#      if temp == 3:
#           print ('n=== ВСЕ СОТРУДНИКИ ===\n')
#           logger.read_all_file()  
#           run()
#      if temp == 4:
#           print('\n Работа завершена \n')

from view import (get_employee, get_changes, get_id, get_first_name, get_last_name,
                    get_phone_number, get_position, get_salary, get_salary_range, show_menu, 
                    show_search_menu, show_update_menu, no_employee_error, show_employee_info)
from model import (read_csv, read_json, write_csv, write_json, find_employee_by_id,
                    find_employee_by_last_name, find_employee_by_phone_number, 
                    find_employees_by_salary_range, update_employee, add_employee, del_employee, 
                    find_employee, find_employee_by_position)

def run_work():
     employees = read_csv()
     employee = {}
     while True:
          choice = show_menu()
          if choice == 1: # find employee
               employee = find_employee (employees)
               if employee is None:
                    no_employee_error ()
               else:
                    show_employee_info(employee)
          elif choice == 2: # select employees by position
               position = input("Введите название позиции:")
               emp_by_position = find_employee_by_position (employees, position)
               if not emp_by_position:
                    no_employee_error ()
               else:
                    for emp in emp_by_position:
                         show_employee_info(emp)
          elif choice == 3: # select employees by salary range
               emp_by_salary = find_employees_by_salary_range (employees)
               if not emp_by_salary:
                    no_employee_error ()
               else:
                    for emp in emp_by_salary:
                         show_employee_info(emp)
          elif choice == 4: # add employee
               add_employee (employees)
          elif choice == 5 # remove emplouee
               fired_employee = get_employee ()
               del_employee (employees, fired_employee) 
          elif choice == 6: # apdate employee data
               employee = find_employee (employees)
               update_employee (employees, employee)
          elif choice == 7: # export data to json
               write_json(employees)
          elif choice == 8: # export data to csv
               write_csv(employees)
          # elif choice == 9:
          #      m.exp_xlsx()
          #   print('Database exported to xlsx')
          # else:
          #   quit()
