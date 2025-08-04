from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates/level4')

@app.route('/lesson')
def lesson():
    return render_template('Continuous_Time_Markov_Chains.html')

if __name__ == '__main__':
    app.run(debug=True) 