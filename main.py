# print("### TEST SCRIPT" * 5)


def h():
    def help(x):
        return x % 2 == 0
    
    lst = [i**2 for i in range(10)]
    # return lst
    lst = filter(help, lst)
    # print(list(lst))

    print(list(lst)[::2])


# h()
def q2():
    z = 0
    for i in range(1, 10):
        if (i + 1 // 2) % 7 == 0:
            break
        else:
            z += int(i % 2 == 0)
            print(z)

    else:
        print("End")

# q2()
# print(7 % 7)
for num in range(5, 9):
    # print(num)
    for i in range(2, num):
       if num%i == 1:
          print(num, i, num%i)
          break


sample = [5,4,12,7,15,9]
reverse = sample[::-1]

print(reverse)

# {
#     "role_name": "Administrator",
#     "modules": 
#         [
#             {
#             "module_name": "ReportManager",
#             "can_view": "False",
#             "can_add": "False",
#             "can_edit": "False",
#             "can_delete": "False",
#             "can_print": "False",
#             "can_deactivate": "False",
#             "can_import": "False",
#             "can_export": "False"
#             },
#             {
#             "module_name": "ContentManager",
#             "can_view": "True",
#             "can_add": "True",
#             "can_edit": "True",
#             "can_delete": "True",
#             "can_print": "True",
#             "can_deactivate": "True",
#             "can_import": "True",
#             "can_export": "True"
#             },
#             {
#             "module_name": "UserProfileManager",
#             "can_view": "True",
#             "can_add": "True",
#             "can_edit": "True",
#             "can_delete": "True",
#             "can_print": "True",
#             "can_deactivate":"True",
#             "can_import":"True",
#             "can_export":"True"
#         },
#         {
#             "module_name":"UserRoleManager",
#             "can_view": "True",
#             "can_add": "True",
#             "can_edit": "True",
#             "can_delete": "True",
#             "can_print": "True",
#             "can_deactivate": "True",
#             "can_import": "True",
#             "can_export": "True"
#         },
#         {
#             "module_name": "AircraftTemplateManager",
#             "can_view": "True",
#             "can_add": "True",
#             "can_edit": "True",
#             "can_delete": "True",
#             "can_print": "True",
#             "can_deactivate": "True",
#             "can_import": "True",
#             "can_export": "True"
#         },
#         {
#             "module_name": "DataSettings",
#             "can_view": "True",
#             "can_add": "True",
#             "can_edit": "True",
#             "can_delete": "True",
#             "can_print": "True",
#             "can_deactivate": "True",
#             "can_import": "True",
#             "can_export": "True"
#         },
#         {
#             "module_name": "OccurrenceReport",
#             "can_view": "True",
#             "can_add": "True",
#             "can_edit": "True",
#             "can_delete": "True",
#             "can_print": "True",
#             "can_deactivate": "True",
#             "can_import": "True",
#             "can_export": "True"
#         }
#     ]
# }

