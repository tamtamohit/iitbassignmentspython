from flask import Flask,request,jsonify
from json import dumps

app = Flask(__name__)



@app.route('/',methods=['POST'])
def ISPALIN():

        data =  request.get_json()
        string = data['string']
        for i in range(0, int(len(string)/2)):
            if(string[i] != string[len(string) - i -1]):
                return jsonify(result=False)
            else:
                return jsonify(result=True)
        # return jsonify(data)



if __name__ == "__main__":
        app.run(debug= True,threaded=True,host='0.0.0.0',port=5000)