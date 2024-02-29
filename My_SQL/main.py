from My_SQL.services.hr_db_services import HR_services


# data = HR_services.get_all("my_table")
#
# for r in data:
#     print(r)
#
# HR_services.insert_one_my_table("ganesh", 38)
#
# HR_services.update_age("s", 22)

HR_services.pro_call("sp_dept")