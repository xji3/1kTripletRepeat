# This file is for getting family information of the 1000 genome project data
# Xiang Ji
# xji3@ncsu.edu

from xlrd import open_workbook
# the spreadsheet is downloaded from link below
# ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/working/20130606_sample_info/20130606_sample_info.xlsx

if __name__ == '__main__':
    xls_file = './20130606_sample_info.xlsx'
    wb = open_workbook(xls_file)
    sheet = wb.sheets()[0]
    keys = [str(item.value) for item in sheet.row(0)]

    sample_to_info = dict()
    family_to_id = dict()

    for i in range(1, sheet.nrows):
        info = {keys[j]:str(sheet.row(i)[j].value) for j in range(len(keys))}
        sample_to_info[info['Sample']] = info
        if family_to_id.has_key(info['Family ID']):
            if info['Relationship'] in ['father', 'mother', 'child']:
                family_to_id[info['Family ID']].append(info['Sample'])
        else:
            if info['Relationship'] in ['father', 'mother', 'child']:
                family_to_id[info['Family ID']] = [info['Sample']]

    for k in family_to_id.keys():
        family_to_id[k] = set(family_to_id[k])
        if len(family_to_id[k]) < 3:
            family_to_id.pop(k)

