
class Udacian():

    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status
    
    def print_udacian(self):
        print("Udacity Member Information:\n",
         "Name: ", self.name,
         "\nCity: ", self.city,
         "\nEnrollment: ", self.enrollment,
         "\nNanodegree: ", self.nanodegree,
         "\nStatus: ", self.status)

zinab = Udacian("Zainab", "Jeddah", ["Full-Stack", "Font-End"],
 "Full-Stack", "Active")

print(zinab.name)
