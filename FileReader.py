from Kitchen import Kitchen
from PageOne import PageOne
from GeneralInfo import GeneralInfo
from PageTwo import PageTwo
from General import General
from Hall import Hall
from pprint import pprint
from Content import Content
from Room import Room
import re
from Toilet import Toilet


class FileReader:
    def __init__(self, file):
        self.file = file

    def getDataFromPageOne(self):
        lines = self.file.readlines()
        page_one = PageOne()
        inspection_people_bool = False
        comments_bool = False

        for index, line in enumerate(lines):
            line = line.replace("\n", "")
            if 'Lejlighedens adresse' in line:
                page_one.address = self.formatLine(line)

            if 'Andelshaver, sælger' in line:
                page_one.owner = self.formatLine(line)

            if 'Dato:' in line:
                page_one.date = self.formatLine(line)

            if 'Sag nr' in line:
                page_one.id = self.formatLine(line)

            if "Besigtiget" in line:
                page_one.inspection_date = self.formatLine(line)

            if "Til stede ved besigtigelsen" in line:
                inspection_people_index = index  # Sætter index til indexet for "Til stede ved besigtigelsen"-elementet
                inspection_people_bool = True  # Bruges til at bestemme at loopet nu er forbi "Til stede ved besigtigelsen"-elementet

            # Tjekker loopet er forbi "Til stede ved besigtigelsen"-elementet
            # Hvis det er det tilføjes de næste elementer i listen til people_at_inspection i Page1 objektet indtil at elementet indeholder "---"
            # Når elementet indeholder "---" er der ikke flere personer at tilføje
            if inspection_people_bool and inspection_people_index != index:
                if line != "---":
                    if line and line != " ":
                        page_one.people_at_inspection.append(line)
                else:
                    inspection_people_bool = False

            if "Lejlighedens vedligeholdelsesstand" in line:
                page_one.maintance_condition = self.formatLine(line)

            if "Vedligeholdelse giver tillæg/fradrag" in line and "JA" in line.upper():
                page_one.appendix = True

            if "Tidligere opgørelse" in line:
                page_one.last_report = self.formatLine(line)

            if "Andelshaveres opgørelse" in line:
                page_one.owners_report = self.formatLine(line)

            if "Overtaget" in line:
                page_one.apartment_takeover = self.formatLine(line)

            if "Ombygning:" in line and "JA" in line.upper():
                page_one.reconstruction = True

            if "Byggesag / anmeldelse til kommunen" in line:
                page_one.construction_project = self.formatGeneralInfoLine(line)

            if "VVS-installationsgodkendelse" in line:
                page_one.VVS_approval = self.formatGeneralInfoLine(line)

            if "Gasinstallationsgodkendelse" in line:
                page_one.gas_approval = self.formatGeneralInfoLine(line)

            if "El-installationsgodkendelse" in line:
                page_one.electricity_approval = self.formatGeneralInfoLine(line)

            if "Afløbsinstallationsgodkendelse" in line:
                page_one.drain_approval = self.formatGeneralInfoLine(line)

            # Hvis elementet er Bemærkninger skal de næste elementer tilføjes til comments listen i Page1 objektet
            # Indtil at der stødes på "Sendt til:"-elementet
            if line == "Bemærkninger:":
                comments_bool = True
                comments_index = index

            if comments_bool and comments_index != index:
                if line != "Side 2 - Forbedringer/løsøre:" and "Sendt til:" not in line:
                    if line:
                        page_one.comments.append(line)
                else:
                    page_one.comments.pop()
                    comments_bool = False
        return page_one


    # Optimer denne metode (de sidste if sætninger)
    def getDataFromPageTwo(self):
        lines = self.file.readlines()
        general = []
        kitchen = []
        restroom = []
        living_room = []
        side_2_reached = False
        temp = []
        type = 0
        for index, line in enumerate(lines):

            if "Side 2 - Forbedringer/løsøre":
                side_2_reached = True

            if side_2_reached:
                if "Side 3 - Tilstand, vedligeholdelse" in line:
                    break

                if "Generelt:" in line:
                    type = 1

                if "Køkken:" in line:
                    type = 2

                if "Badeværelse" in line or "Toilet:" in line:
                    type = 3

                if "Værelse" in line:
                    type = 4

                if type == 1 and line != '\n' and line != '\xa0\n' and line != ' ':
                    if 'Generelt:' not in line and '----\n' not in line:
                        line = line.replace('\n', '')
                        if temp.__len__() in (2, 9, 10) and line != '0':
                            line = self.format_line_for_page_two_obj(line)
                        if line == '0':
                            line = ''
                        temp.append(line)
                        if temp.__len__() == 11:
                            general = self.addPageTwoObjToList(temp, general)
                            temp.clear()

                if type == 2 and line != '\n' and line != '\xa0\n' and line != ' ':
                    if 'Køkken:' not in line and '----\n' not in line:
                        line = line.replace('\n', '')
                        if temp.__len__() in (2, 9, 10) and line != '0':
                            line = self.format_line_for_page_two_obj(line)
                        if line == '0':
                            line = ''
                        temp.append(line)
                        if temp.__len__() == 11:
                            kitchen = self.addPageTwoObjToList(temp, kitchen)
                            temp.clear()

                if type == 3 and line != '\n' and line != '\xa0\n':
                    if 'Toilet:' not in line and 'Badeværelse:' not in line and '----\n' not in line:
                        line = line.replace('\n', '')
                        if temp.__len__() in (2, 9, 10) and str(line) != '0':
                            line = self.format_line_for_page_two_obj(line)
                        if line == '0':
                            line = ''
                        temp.append(line)

                        if temp.__len__() == 11:
                            restroom = self.addPageTwoObjToList(temp, restroom)
                            temp.clear()

                if type == 4 and line != '\n' and line != '\xa0\n' and line != ' ':
                    if 'Værelse:' not in line and '----\n' not in line:
                        line = str(line.replace('\n', ''))
                        if temp.__len__() in (2, 9, 10) and str(line) != '0':
                            line = self.format_line_for_page_two_obj(line)
                        if line == '0':
                            line = ''
                        temp.append(line)
                        if temp.__len__() == 11:
                            living_room = self.addPageTwoObjToList(temp, living_room)
                            temp.clear()

        list_of_lists = [general, kitchen, restroom, living_room]

        return list_of_lists

    def getDataFromPageThree(self):
        lines = self.file.readlines()
        reached_side_three = False
        general_bool = True
        hall_bool = False
        kitchen_bool = False
        toilet_bool = False
        living_room_bool = False
        room_1_bool = False
        room_2_bool = False
        general_data = General()
        hall_data = Hall()
        kitchen_data = Kitchen()
        toilet_data = Toilet()
        living_room_data = Room()
        room_1_data = Room()
        room_2_data = Room()
        for index, line in enumerate(lines):
            if "Side 3 - Tilstand, vedligeholdelse" in line:
                reached_side_three = True

            if reached_side_three:
                if general_bool:
                    if "Eltavle" in line:
                        general_data.eltavle = self.create_content(line)

                    if "HFI" in line:
                        general_data.hfi = self.create_content(line)

                    if "Stik, afbrydere og udtag" in line:
                        general_data.stik = self.create_content(line)

                    if "vinduer og ruder" in line.lower():
                        general_data.vinduer = self.create_content(line)

                    if "Vedligeholdelse:" in line:
                        general_data.vedligeholdse = self.create_content(line)

                    if "Rydning" in line:
                        general_data.rydning = self.create_content(line)

                    if "Rengøring" in line:
                        general_data.rengøring = self.create_content(line)
                        general_bool = False
                        hall_bool = True

                if hall_bool:
                    if "Loft" in line:
                        hall_data.loft = self.create_content(line)
                    if "Vægge" in line:
                        hall_data.vægge = self.create_content(line)
                    if "Gulv" in line:
                        hall_data.gulv = self.create_content(line)
                    if "Træværk" in line:
                        hall_data.træværk = self.create_content(line)
                        hall_bool = False
                        kitchen_bool = True

                if kitchen_bool:
                    if "Loft" in line:
                        kitchen_data.Loft = self.create_content(line)
                    if "Vægge" in line:
                        kitchen_data.Vægge = self.create_content(line)
                    if "Gulv" in line:
                        kitchen_data.Gulv = self.create_content(line)
                    if "Træværk" in line:
                        kitchen_data.Træværk = self.create_content(line)
                    if "Skabe" in line:
                        kitchen_data.Skabe = self.create_content(line)
                    if 'Bordplader' in line:
                        kitchen_data.Bordplader = self.create_content(line)
                    if 'Vægfliser' in line:
                        kitchen_data.Vægfliser = self.create_content(line)
                    if 'Afløbsinstallation' in line:
                        kitchen_data.Afløbsinstallation = self.create_content(line)
                    if 'Vandinstallation' in line:
                        kitchen_data.Vandinstallation = self.create_content(line)
                    if 'Gasinstallation' in line:
                        kitchen_data.Gasinstallation = self.create_content(line)
                    if 'Hårde hvidevarer' in line:
                        kitchen_data.Hvidevarer = self.create_content(line)
                        kitchen_bool = False
                        toilet_bool = True

                if toilet_bool:
                    if "Loft" in line:
                        toilet_data.Loft = self.create_content(line)
                    if "Vægge" in line:
                        toilet_data.Vægge = self.create_content(line)
                    if "Gulv" in line:
                        toilet_data.Gulv = self.create_content(line)
                    if "Træværk" in line:
                        toilet_data.Træværk = self.create_content(line)
                    if "WC" in line:
                        toilet_data.WC = self.create_content(line)
                    if "Håndvask" in line:
                        toilet_data.Håndvask = self.create_content(line)
                    if "Bruseinstallation" in line:
                        toilet_data.Bruseinstallation = self.create_content(line)
                    if "Vandinstallation" in line:
                        toilet_data.Vandinstallation = self.create_content(line)
                    if "Afløbsinstallation" in line:
                        toilet_data.Afløbsinstallation = self.create_content(line)
                    if "Ventilation" in line:
                        toilet_data.Ventilation = self.create_content(line)
                        toilet_bool = False
                        room_1_bool = True

                if room_1_bool:
                    if "Værelse" in line:
                        room_1_data.title = line.replace('\n', '')
                    if "Loft" in line:
                        room_1_data.loft = self.create_content(line)
                    if "Vægge" in line:
                        room_1_data.vægge = self.create_content(line)
                    if "Gulv" in line:
                        room_1_data.gulv = self.create_content(line)
                    if "Træværk" in line:
                        room_1_data.træværk = self.create_content(line)
                    if "Radiator" in line:
                        room_1_data.radiator = self.create_content(line)
                        room_1_bool = False
                        room_2_bool = True

                if room_2_bool:
                    if "Værelse" in line:
                        room_2_data.title = line.replace('\n', '')
                    if "Loft" in line:
                        room_2_data.loft = self.create_content(line)
                    if "Vægge" in line:
                        room_2_data.vægge = self.create_content(line)
                    if "Gulv" in line:
                        room_2_data.gulv = self.create_content(line)
                    if "Træværk" in line:
                        room_2_data.træværk = self.create_content(line)
                    if "Radiator" in line:
                        room_2_data.radiator = self.create_content(line)

                if 'Stue' in line or living_room_bool:
                    living_room_bool = True
                    if "Stue" in line:
                        living_room_data.title = line.replace('\n', '')
                    if "Loft" in line:
                        living_room_data.loft = self.create_content(line)
                    if "Vægge" in line:
                        living_room_data.vægge = self.create_content(line)
                    if "Gulv" in line:
                        living_room_data.gulv = self.create_content(line)
                    if "Træværk" in line:
                        living_room_data.træværk = self.create_content(line)
                    if "Radiator" in line:
                        living_room_data.radiator = self.create_content(line)
                        living_room_bool = False
                        room_1_bool = True

        list_of_content = [general_data, hall_data, kitchen_data, toilet_data, living_room_data, room_1_data, room_2_data]
        return list_of_content

    def formatLine(self, line):
        formatted_line = line[line.find(":") + 1:]

        try:
            if formatted_line[0] == ' ':
                formatted_line = formatted_line[1:]
        except:
            print("string index out of range", formatted_line)

        return formatted_line


    def formatGeneralInfoLine(self, line):
        line = self.formatLine(line)
        slashIndex = line.find("/")
        if slashIndex != -1:
            status = line[0:slashIndex - 1]
            comment = line[slashIndex + 2:]
        else:
            status = line
            comment = ""

        return GeneralInfo(status, comment)

    def create_content(self, line):
        content = None
        try:
            line = line.replace('\n', '')
            line = line.split(':', 1)  ##Splitter én gang på :
            line_spltted = []
            try:
                ##Da der altid er højest 3 forskellige typer indhold splittes der kun 2 gange
                ##split antal gange pr slash i stringen - 1
                line_spltted = line[1].split(' / ', 2)
            except:
                print('wtf', line)
            payed_by = ''
            retention_sum = 0
            deduction = 0
            comment = ''
            retention_deduction_bool = False
            condition = line_spltted[0]

            if line_spltted.__len__() > 1:
                for item in line_spltted:
                    item = item.replace(' ', '')
                    if 'T:' in item:
                        #Henter kun beløb ved at splitte på : og fjerner punktum for at gøre det muligt at caste det til int
                        retention_sum = int(item.split(':')[1].replace('.', ''))
                        retention_deduction_bool = True

                    if 'F:' in item:
                        #Henter kun beløb ved at splitte på : og fjerner punktum for at gøre det muligt at caste det til int
                        deduction = int(item.split(':')[1].replace('.', ''))
                        retention_deduction_bool = True

                    if item == 'F':
                        payed_by = 'F'

                    if item == 'B':
                        payed_by = 'B'

            if line_spltted.__len__() == 3:
                comment = line_spltted[line_spltted.__len__() - 1]

            if line_spltted.__len__() == 2 and retention_deduction_bool is False:
                comment = line_spltted[line_spltted.__len__() - 1]

            content = Content(condition, payed_by, retention_sum, deduction, comment)
        except:
            print("FEJL i FileReader linje 370", line)
        return content


    def addPageTwoObjToList(self, temp_list, type_list):
        page_two = PageTwo(temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],
                           temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10])
        type_list.append(page_two)
        return type_list


    def check_if_string_contains_digits(self, line):
        return bool(re.search(r'\d', line))


    # Ændre ikke decimal tal til ints i stedet for float
    def format_line_for_page_two_obj(self, line):
        if '.' in line:
            line = line.replace('.', '')
        try:
            line = float(line)
        except:
            print(line, "not a float")

        if line == 0.0:
            line = ''
        return line
