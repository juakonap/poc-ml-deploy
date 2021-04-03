import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
    return '<h1> La aplicación está funcionando!</h1>'


@app.route('/predict',methods=['GET'])
def predict():
    import pickle
    model = pickle.load(open('data/marriage_age_predict_model.ml', 'rb'))
    predicted_age_of_marriage = model.predict([[int(request.args['gender']),
                            int(request.args['religion']),
                            int(request.args['caste']),
                            int(request.args['mother_tongue']),
                            int(request.args['country']),
                            int(request.args['height_cms']),
                           ]])
    return str(round(predicted_age_of_marriage[0],2))

<<<<<<< HEAD
=======

if __name__ == "__main__":
    app.run(debug=True)

>>>>>>> dev
#http://127.0.0.1:5000/predict?gender=0&religion=10&caste=2&mother_tongue=2&country=3&height_cms=170