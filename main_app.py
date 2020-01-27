from flask import Flask, render_template, jsonify, Response, request


app = Flask(__name__)

@app.route("/post_json", methods=['GET', 'POST'])
def json():
    print("JSONNNNNNNNNNNNNNNNNNNNNNNNN")
    print('現在的狀況為',request.method)
    if request.method == 'POST':
        print("post val =", request.values)

        #print("post name =", request.values['name'])
        #print("post url =", request.values['url'] )
        return 'Hello ' + str(request.values) 
    elif request.method == 'GET':
        print(str(request.values['data']))
        return 'hello'+str(request.values['data'])
    else:
        return 'hello json error'

@app.route("/post_submit", methods=['GET', 'POST'])
def submit():
    print('現在的狀況為',request.method)
    if request.method == 'POST':
        print("post name =", request.values['name'])
        print("post url =", request.values['url'] )
        return 'Hello ' + request.values['name'] 
    return 'hello post error'

@app.route('/result/<a>', methods=['GET', 'POST'])
def get_result(a):
    a = int(a)
    print('現在的狀況為',request.method)
    if request.method == 'POST':
        print("post info",request.values)
        print('POST val = ', request.values)
        res_txt = request.values
    elif request.method == 'GET':
        if a < 1:
            res_txt = u"現在小於一拉"
        elif a > 3:
            res_txt = u"跟你講拉現在大於三"
        else:
            res_txt =u"yeeee 1~3"
    res_info = {
        'res_txt': res_txt
    }
    return res_info

@app.route('/index.html')
def index():
    return render_template('my_vue.html')



if __name__ == '__main__':
    app.debug = True
    app.run()