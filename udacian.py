class Udacian():
    """
    This class provides the structure to view Udacity member information

    Attributes:
    name (str): Udacian member name
    city (str): City where member lives
    enrollment (str):  Courses the member enrolled in
    nanodegree (str): The name of the nanodegree course
    status (str): The status of the member
    """

    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status

    # Display the udacian information
    def print_udacian(self):
        value = "Udacity Member Information:\nName: "
        value += self.name + "\nCity: " + self.city
        value += "\nEnrollment: " + self.enrollment
        value += "\nNanodegree: " + self.nanodegree
        value += "\nStatus: " + self.status
        value += "\n---------------------------------"
        return value
