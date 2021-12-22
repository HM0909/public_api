from flask import Flask, jsonify
import utils.file_util as file_util

app = Flask (__name__)
 
@app.route('/air')
def environments():
    datas = file_util.csv_reader("C:\\hm_py\\crawling\\result\crawling_air.csv")
    jsonDatas = []
    for data in datas:
        jsonDatas.append({"daegu":data[0],"chungnam":data[1],"incheon":data[2],"daejeon":data[3],"gyeongbuk":data[4],"sejong":data[5],"gwangju":data[6],"jeonbuk":data[7],"gangwon":data[8],"ulsan":data[9],"jeonnam":data[10],"seoul":data[11],"busan":data[12],"jeju":data[13],"chungbuk":data[14],"gyeongnam":data[15],"dataTime":data[16],"dataGubun":data[17],"gyeonggi":data[18],"itemCode":data[1]})
    return jsonify(jsonDatas)

if __name__ == "__main__":
    app.run()