from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'


@app.route('/api',methods=["POST"])
def crud():
    if request.method=='POST':
        # Handle POST Request here
        request_data = request.get_json()
        if "name" in request_data:
            name = request_data["name"]
            usr = User(name=name)
            db.session.add(usr)
            db.session.commit()
            return jsonify({"success":True, "message":"User created", "id":usr.id}), 201
        else:
            return jsonify({"success":False, "message":"Bad request missing 'name' attribute"}), 400


    return jsonify({"success": False, "message":"Method not allowed"}), 405

@app.route('/api/<int:id>',methods=["GET", "PUT", "DELETE"])
def rud(id):
    if request.method=='GET':
        # Handle GET Request here
        usr = User.query.get(id)
        if usr != None:
            return jsonify({"id": usr.id, "name":usr.name}), 200
        else:
            return jsonify({"success": False, "message":"User not found"}), 404

    elif request.method=='PUT':
        # Handle PUT Request here
        usr = User.query.get(id)
        request_data = request.get_json()
        if "name" in request_data:
            if usr == None:
                return jsonify({"success": False, "message":"User not found"}), 404       
            else:
                name = request_data["name"]
                usr.name = name
                db.session.commit()
                return jsonify({"success":True, "message":"User updated", "id":usr.id}), 200
        else:
            return jsonify({"success":False, "message":"Bad request missing 'name' attribute"}), 400


    elif request.method=='DELETE':
        # Handle DELETE Request here
        usr = User.query.get(id)
        if usr == None:
            return jsonify({"success": False, "message":"User not found"}), 404       
        else:
            db.session.delete(usr)
            db.session.commit()
        return jsonify({"success":True}), 200

    return jsonify({"success": False, "message":"Method not allowed"}), 405

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)