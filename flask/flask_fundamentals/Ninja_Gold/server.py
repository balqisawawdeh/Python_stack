from flask import Flask, render_template,request,session,redirect 
from datetime import datetime
import random
app=Flask(__name__)
app.secret_key="Gold Ninja"

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
        print("Total Gold = 0")
        session['activities'] = []
    date=datetime.now()
    date_time = date.strftime("%m/%d/%Y, %H:%M")
    return render_template("index.html",date_time=date_time)

@app.route('/process_money',methods=['POST'])
def process():
    session['message']=''
    number= session['total_gold']
    date=datetime.now()
    date_time = date.strftime("%m/%d/%Y, %H:%M")
    
    if request.form['building'] == 'farm':
        ran=random.randint(10, 20)
        number+= ran
        session['activities'].append(f"Earned {number} gold from the farm! ({date_time})")
        for i in range(len(session['activities'])):
            session['message'] += session['activities'][i]
    
    elif request.form['building'] == 'cave':
        ran=random.randint(10, 20)
        number+= ran
        session['activities'].append(f"Earned {number} gold from the farm! ({date_time})")
        for i in range(len(session['activities'])):
            session['message'] += session['activities'][i]
    
    elif request.form['building'] == 'house':
        ran=random.randint(10, 20)
        number+= ran
        session['activities'].append(f"Earned {number} gold from the farm! ({date_time})")
        for i in range(len(session['activities'])):
            session['message'] += session['activities'][i]
    
    elif request.form['building'] == 'Cafeteria':
        ran=random.randint(10, 20)
        number+= ran
        session['activities'].append(f"Earned {number} gold from the farm! ({date_time})")
        for i in range(len(session['activities'])):
            session['message'] += session['activities'][i]
    
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    print('Session Cleared')
    return redirect("/")    
if __name__=="__main__":
    app.run(debug=True)