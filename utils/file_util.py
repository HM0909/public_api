import csv

CSV_FILE_ENCODING ="utf-8-sig"
FILE_ENCODING ="utf-8"
NEW_LINE = '\n'

# 텍스트 파일 생성
def file_writer(file_path, datas):
    f = open(file_path, "w", encoding=FILE_ENCODING)

    for data in datas:
        for i in range(len(data)):
            f.write(data[i] + NEW_LINE)
            
        f.write(NEW_LINE)

    f.close()
    
    
# csv 파일 생성
def csv_writer(file_path, datas, header):
    f = open(file_path,'w', newline='', encoding="utf-8-sig")

    r = csv.writer(f)
    r.writerow(header)

    for data in datas:
        r.writerow(data)
     
        
def csv_reader(file_path):
    result = []        
    f = open(file_path, 'r', encoding=CSV_FILE_ENCODING)
    rdr = csv.reader(f)
    for line in rdr:
        result.append(line)
        # print(line)
    f.close()   
    
    return result