# flask program that includes url decoders and functions for all of the template pages
# imports
from flask import Flask, render_template, request

app = Flask(__name__)


# url decoder and functions for each template page including default hello world
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/base')
def display_base():
    return render_template('base.html')


@app.route('/index')
def display_index():
    return render_template('index.html')


@app.route('/activities')
def display_activities():
    return render_template('activities.html')


# url decoder and function that includes methods parameter to handle POST and GET when user submits. Includes exception
# handling and request functions
@app.route('/awards', methods=['POST', 'GET'])
def display_awards():
    try:
        if request.method == 'POST':
            return render_template('awards.html', message='Thank you for Voting!')
        else:
            return render_template('awards.html')
    except Exception as e:
        print(e)
        return render_template('awards.html')


@app.route('/keynote')
def display_keynote():
    return render_template('keynote.html')


@app.route('/meals')
def display_meals():
    return render_template('meals.html')


@app.route('/workshopschedule')
def display_workshopschedule():
    return render_template('workshopschedule.html')


@app.route('/registration', methods=['POST', 'GET'])
def display_registration():
    try:
        if request.method == 'POST':
            return render_template('thankyou.html')
        else:
            return render_template('registration.html')
    except Exception as e:
        print(e)
        return render_template('registration.html')


@app.route('/poll', methods=['POST', 'GET'])
def display_poll():
    try:
        if request.method == 'POST':
            return render_template('poll.html', message='Thank you for Voting!')
        else:
            return render_template('poll.html')
    except Exception as e:
        print(e)
        return render_template('poll.html')


if __name__ == '__main__':
    app.run()
