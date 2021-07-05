import datetime
from collections import defaultdict

class DataBase:


    def __init__(self,filename):
        self.filename = filename
        self.file = None
        self.punches = None
        self.load()

    def add_user(self, name):
        if name.strip() not in self.punches:
            self.punches[name.strip()] = DataBase.get_date()
            self.save()
            return 1
        else:
            print("User Already in DataBase")
            return -1

    def get_user(self,name):
        if name in self.punches:
            return self.punches[name]
        else:
            return -1

    def append_punch(self, name):
        if name.strip() in self.punches:
            self.punches[name.strip()].append(DataBase.get_date()+"#")
            print(DataBase.get_date())
            print(self.punches[name.strip()])
            print(len(self.punches[name.strip()]))
            #Method that saves only the last 60 punches or the last month
            if(len(self.punches[name.strip()]) >59):
                self.punches[name.strip()].pop(0)
            self.save()
            return 1
        else:
            print("User not in DataBase")
            return -1

    def load(self):
        self.file = open(self.filename, "r")
        self.punches = defaultdict(list)

        for line in self.file:
            string = line.strip()+"#"
            name, time = string.split(";")
            tempList = time.split("#")
            for item in tempList:
                if item != "":
                    print("Here " + str(item))
                    self.punches[name].append(item+"#")
                else:
                    print("Garbage")
        self.file.close()

    def save(self):
        with open(self.filename, "w") as f:
            for punch in self.punches:
                string = ''.join(self.punches[punch]) + "\n"
                f.write(punch + ";" + string)

    def print_cont(self):
        for line in self.punches:
            print(self.punches[line])

    @staticmethod
    def get_date():
        return str(datetime.datetime.now())[:-7]