from flask import Flask , render_template ,request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl' , 'rb'))


@app.route('/')
def main():
    return render_template("main.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if output > 100000:
        return render_template('main.html', prediction_text='Predicted house price is : {}'.format(output), rich = "damn boi thats an expensive house")
    else:
        return render_template('main.html', prediction_text='Predicted house price is : {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)