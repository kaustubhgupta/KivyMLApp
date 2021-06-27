from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
Filename = 'model/model_tree.pkl'
with open(Filename, 'rb') as file:  
    model = pickle.load(file)

@app.route('/')
def index_page():
    return jsonify({'meaasge':'This is the api which returns the type of song rock or hip hop.', 
                    'Parameters_required':'acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence'})

@app.route('/predict', methods=['POST', 'GET'])
def predict_logic():
    query = request.args
    acousticness = float(query.get('acousticness'))
    danceability = float(query.get('danceability'))
    energy = float(query.get('energy'))
    instrumentalness = float(query.get('instrumentalness'))
    liveness = float(query.get('liveness'))
    speechiness = float(query.get('speechiness'))                  
    tempo = float(query.get('tempo'))
    valence = float(query.get('valence'))
    #print(acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence)
    pred_name = model.predict([[acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence]]).tolist()[0]
    return jsonify({'prediction':pred_name})

if __name__ == "__main__":
    app.run(debug=True)