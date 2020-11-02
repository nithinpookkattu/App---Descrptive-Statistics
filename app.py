from flask import Flask, render_template, request
import statistics
from scipy.stats import skew
from scipy.stats import kurtosis
import numpy

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        user_input = str(request.form['user_input'])
        user_list = user_input.split()
        user_list = [int(i) for i in user_list]
        mean = round(statistics.mean(user_list), 2)
        stdev = round(statistics.stdev(user_list), 2)
        var = round(statistics.variance(user_list), 2)
        skewness = round(skew(user_list), 2)
        kurt = round(kurtosis(user_list), 2)
        minimum = min(user_list)
        first = numpy.percentile(user_list, 25)
        med = statistics.median(user_list)
        third = numpy.percentile(user_list, 75)
        maximum = max(user_list)

        return render_template('app.html', user_list=user_list, mean=mean, stdev=stdev, var=var, skewness=skewness, kurt=kurt, minimum=minimum, first=first, med=med, third=third, maximum=maximum)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)