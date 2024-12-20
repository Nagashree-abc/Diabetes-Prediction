from flask import Flask,render_template,request
import numpy as np
import joblib

model=joblib.load("model.pkl")


app=Flask(__name__)# here creating server object

@app.route('/')#/ means default route
def index():
    return render_template('sugar.html')
@app.route('/predict',methods=['GET','POST']) #here /predict is the root name
def prediction():
    # below is the coding for list comprehension
    
    testdata=[float(x) for x in request.form.values()]
    # Above technique is known as list comprehension
    print(testdata)
    td=np.array([testdata])
    pred=model.predict(td)

    print(pred,type(pred))
    if pred[0]==0:
        result=f"report is No diabetic"
    else:
        result=f"report is : Yes diabetic"
    return render_template('sugar.html',res=result)
    
    
if __name__=='__main__' :

    app.run(debug=True)# to run automatically