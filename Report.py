from PageTwo import PageTwo

class Report:
    def __init__(self, report):
        self.report = report

    def get_stylesheet_1(self):
        stylesheet_one = self.report.get_sheet_by_name('Side 1')
        return stylesheet_one

    def get_stylesheet_2(self):
        stylesheet_two = self.report.get_sheet_by_name('Side2.1')
        return stylesheet_two

    def get_stylesheet_3(self):
        stylesheet_3 = self.report.get_sheet_by_name('Side 3 - Vedligehold')
        return stylesheet_3

    def get_rownumbers_for_page_two(self):
        sheet = self.report.get_sheet_by_name('Side2.1')

        for i in range(1, 100):
            row_value = str(sheet['B' + str(i)].value)
            if 'Generelt' in row_value:
                PageTwo.general_start_row = i
            if 'Køkken' in row_value:
                PageTwo.kitchen_start_row = i
            if 'Badeværelse' in row_value:
                PageTwo.restroom_start_row = i
            if 'Stue og værelser' in row_value:
                PageTwo.living_room_start_row = i

