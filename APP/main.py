from flask import Flask,  request, render_template

import joblib
from feature import *

from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "pipeline.sav")
print("the paths is ",file_path)

pipeline = joblib.load(file_path)

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        result=request.form
        query_title = result['title']
        query_author = result['author']
        query_text = result['article']
        print(query_text)
        query = get_all_query(query_title, query_author, query_text)
        user_input = {'query':query}
        pred = pipeline.predict(query)
        
        dic = {1:'fake',0:'real'}
        return render_template('show.html',pred_=dic[pred[0]] )

    return render_template('index.html')





if __name__ == '__main__':
    app.run( debug=True)
