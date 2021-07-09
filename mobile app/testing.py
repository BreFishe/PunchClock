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

#Code I may need later
# class P(Popup):
#     username = ""
#
#     def assignName(self):
#         username = self.username.text
#         print(username)
#         MainWindow.setName(self,username)
#
#
#     @property
#     def getUsername(self):
#         return self.username
#
#     pass
#
# <P>:
#     username: usernameInput
#     title: ""
#     size_hint: None, None
#     size: 400, 400
#     FloatLayout:
#         Label:
#             text: "Please enter your UserName"
#             size_hint: .6, .1
#             pos_hint: {"x":.2,"top":.8}
#
#         TextInput:
#             id: usernameInput
#             font_size: 30
#             multiline: False
#             pos_hint: {"x": 0.1, "top":0.7}
#             size_hint: 0.8, 0.4
#
#         Button:
#             text: "Submit"
#             size_hint: .6, .2
#             pos_hint: {"x":.2,"top":.25}
#             on_release:
#                 root.assignName()
#                 root.dismiss()
# ScrollView:
#             do_scroll_y: False
#             do_scroll_y: True
#             pos_hint: {"x": .5, "top": 1}
#
#             Label:
#                 size_hint_y: None
#                 height: self.texture_size[1]
#                 text_size: self.width, None
#                 padding: 10, 10
#                 font_size: 24
#                 text: 'really some amazing text\n' * 100
