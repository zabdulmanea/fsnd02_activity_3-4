class Udacian():
    """
    This class provides the structure to view Udacity member information

    Attributes:
    name (str): Udacian member name
    city (str): City where member lives
    enrollment (object):  List of the courses the member enrolled in
    nanodegree (str): The name of the nanodegree course
    status (str): The status of the member
    """

    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status

    def print_udacian(self):
        print("Udacity Member Information:", "\nName: ", self.name, "\nCity: ",
              self.city, "\nEnrollment: ",
              (", ".join([str(i) for i in self.enrollment])), "\nNanodegree: ",
              self.nanodegree, "\nStatus: ", self.status)


zinab = Udacian("Zainab", "Jeddah", ["Full-Stack", "Font-End"], "Full-Stack",
                "Active")

print(zinab.print_udacian())
