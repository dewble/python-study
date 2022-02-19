import csv


def write_csv_template(filename, listdata):
    with open(filename, 'w', encoding='utf-8-sig', newline='') as writer_csv:
        writer = csv.writer(writer_csv, delimiter=',')

        for item in listdata:
            writer.writerow(item)


datas1=['csv data1','csv data2','csv data3']

write_csv_template('tmp.csv', datas1)