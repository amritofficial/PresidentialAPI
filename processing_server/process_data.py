import csv, datetime, re
from flask import send_file

# a separate class for processing all the information
class Process_Data():

    # create a CSV from JSON file and return it as an attachment
    def create_json_csv(self, json_data):
        custom_json = self.create_custom_json(json_data)

        csv_file_name = 'results.csv'
        csv_file = open(csv_file_name, 'w', newline='')
        csv_file_writer = csv.writer(csv_file)

        # create header
        header_fields = ['Name', 'Party', 'Presidential term', 'President number', 'Ingestion Time']
        csv_file_writer.writerow(header_fields)

        for item in custom_json:
            if 'Federalist' not in item['pp']:
                row = [item['nm'],
                       item['pp'],
                       item['tm'],
                       item['president'],
                       datetime.datetime.now()]
                csv_file_writer.writerow(row)

        csv_file.close()
        # send the file as an attachment
        return send_file('results.csv', as_attachment=True)

    # create a customized json with all the required settings
    def create_custom_json(self, json_data):
        custom_json = json_data
        for item in json_data:
            item['nm'] = self.reverse_first_name(item['nm'])
            item['pp'] = self.create_party_acroynm(item['pp'])
            item['tm'] = self.create_term(item['tm'])

        return sorted(custom_json, key=lambda d: d['nm'])

    # reverse the first word of a full name
    def reverse_first_name(self, full_name):
        reversed_name = self.split_full_name(full_name)[::-1]
        return reversed_name

    # split the full name and return the first word
    def split_full_name(self, full_name):
        return full_name.partition(' ')[0]

    # create an acronym from a party name
    def create_party_acroynm(self, party):
        split_words = re.findall(r"[\w']+", party)
        acronym = ''.join([word[0] for word in split_words])
        return acronym

    # create a presidential term
    def create_term(self, year):
        years = year.split('-')
        return years[0]