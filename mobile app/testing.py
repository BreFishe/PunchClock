from database import DataBase
from collections import defaultdict
import datetime
#
db = DataBase("punches.txt")
# db.add_user("Max")
# db.append_punch("Max")
# db.add_user("Brennen")
#db.append_punch("Brennen")
# db.add_user("Lisa")
# db.append_punch("Lisa")
#
# data_dict = defaultdict(list)
print(db.get_user("Brennen"))

# data_dict = {"Brennen" : ["1,2", "3,4"],"Max" : [1,2],}
# print(data_dict["Brennen"][0])
# data_dict["Brennen"].append("5,6")
# print(data_dict["Brennen"][2])
# print(*data_dict["Brennen"])
# print(str(datetime.datetime.now()).split(" ")[0])