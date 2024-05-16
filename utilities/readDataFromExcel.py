import openpyxl

class ReadExcel:

    @staticmethod
    def read_credentials_from_file(file_path):
        credentials = []
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            username, password = row
            credentials.append({
                "username": username,
                "password": password
            })
        return credentials