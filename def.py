from flask import Flask
import utils.file_util as file_util
from flask import jsonify

app = Flask (__name__)
app.config['JSON_AS_ASCII'] = False
 
@app.route('/def')
def car_def():
    datas = file_util.csv_reader('C:\\hm_py\\crawling\\result\crawling_def.csv')
    
    jsonList = []
    
    for data in datas:
        jsonList.append({"가격": data[0], "경로": data[1]})
        
    return jsonify(jsonList)

if __name__ == "__main__":
    app.run()