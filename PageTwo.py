class PageTwo:

    general_start_row = 0
    kitchen_start_row = 0
    living_room_start_row = 0
    restroom_start_row = 0

    def __init__(self, title, year=0, expenditure=0, appendix=0, quantity=0, age=0, years_curve=0, written_down_to=0,
                 owners_work=0, number_of_hours=0, cost=0):
        self.title = title
        self.year = year
        self.expenditure = expenditure
        self.appendix = appendix
        self.quantity = quantity
        self.age = age
        self.years_curve = years_curve
        self.written_down_to = written_down_to
        self.owners_work = owners_work
        self.number_of_hours = number_of_hours
        self.cost = cost
