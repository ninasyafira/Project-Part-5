from flask import Flask, render_template, request, session
from wtforms import Form, StringField, validators
import Process
import datetime


app = Flask(__name__)


@app.route('/' , methods=['GET', 'POST'])
def home():
    session['userid'] = 'Mary'
    form = SpendForm(request.form)
    if request.method == 'POST' and form.validate():
        monthMM = form.monthStr.data
        yearYY = form.yearStr.data
        print(monthMM)
    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December')

    if todayMonth == 1:
        prevMonth = 12
    else:
        prevMonth = todayMonth - 1

    if todayYear == 2018 :
        prevYear = 2017
    else :
        prevYear = now.year - 1

    usersList = []
    usersList = Process.processUser(session['userid'], todayMonth, todayYear)
    savings = []
    limit = []
    limit = Process.limit(session['userid'],todayMonth,todayYear)
    over = Process.over(session['userid'],todayMonth,todayYear)
    interest = Process.interest(session['userid'],todayMonth,todayYear)
    return render_template('homepage.html', users=usersList,saving=savings,todayMonth=todayMonth, prevMonth=prevMonth, todayYear=todayYear, prevYear=prevYear,limits=limit,over=over,form=form,interest=interest)

@app.route('/hey')
def hey():
    return render_template('homepage2.html')


@app.route('/dec')
def dec():
    session['userid'] = 'Mary'

    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year
    months = ('January','February','March','April','May','June','July','August','September','October','November','December')

    if todayMonth == 1:
        prevMonth = 12
    else :
        prevMonth = todayMonth - 1

    if todayYear == 2018 :
        prevYear = 2017
    else :
        prevYear = now.year - 1
    usersList = []
    usersList = Process.processUser(session['userid'],prevMonth,prevYear)
    totalLeft = Process.savingsLeft(session['userid'], prevMonth, prevYear)
    limit = []
    limit = Process.limit(session['userid'], prevMonth, prevYear)
    over = Process.over(session['userid'], prevMonth, prevYear)

    return render_template('dec.html',users=usersList,todayMonth=todayMonth, prevMonth=prevMonth, todayYear=todayYear, prevYear=prevYear,left=totalLeft,limits=limit,over=over)


class SpendForm(Form):
    monthStr = StringField('Month', [validators.Length(min=1, max=12), validators.DataRequired()])
    yearStr = StringField('Year', [validators.Length(min=1, max=2018), validators.DataRequired()])

@app.route('/selected', methods=['GET', 'POST'])
def selected():
    session['userid'] = 'Mary'
    form = SpendForm(request.form)
    if request.method == 'POST' and form.validate():
        monthMM = form.monthStr.data
        yearYY = form.yearStr.data
        print(monthMM)

    months = ('Null','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December')


    usersList = []
    checkMonth = int(monthMM)
    checkYear = int(yearYY)
    usersList = Process.processUser(session['userid'], todayMonth=checkMonth, todayYear=checkYear)
    limit = []
    limit = Process.limit(session['userid'], checkMonth, checkYear)
    over = Process.over(session['userid'], checkMonth, checkYear)
    interest = Process.interest(session['userid'],checkMonth,checkYear)

    return render_template('nov.html', checkMM=months[checkMonth], checkYY=checkYear,
                           users=usersList, count=len(usersList),limits=limit,over=over,form=form,interest=interest)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()

