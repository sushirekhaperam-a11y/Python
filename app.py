from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to flask web Server!"
#get method end point
@app.route('/users',methods = ['GET'])
def get_users():
    return jsonify({"users":["alice","bob","charlie"]})
#post method end point
@app.route('/users',methods = ['POST'])
def add_users():
    data = request.get_json()
    return jsonify(data),201
#put method end point
@app.route('/users/int:id>',methods = ['PUT'])
def update_users(id):
    return jsonify({"message:"f"User{id}updated"})
#delete the endpoint
@app.route('/users/<int:id>',methods = ['DELETE'])
def delete_users(id):
    return jsonify({"message":f"User{id}updated"})
#patch the endpoint
@app.route('/users/<int:id>',methods = ['PATCH'])
def patch_users(id):
    data = request.get_json()
    return jsonify({"message":"User updated partially","user_id":id,"updated_fields":data})



if __name__ == "__main__":
    app.run(debug = True)