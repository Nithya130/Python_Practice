#In order to convert the slash - dates to dash - dates, we have created a utility function toDashDate within Dates.
#It is a static method because it doesn't need to access any properties of Dates itself and only requires the parameters.


class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromuser = "15/12/2017"
dateWithDash = Dates.toDashDate(dateFromuser)

if (date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")
