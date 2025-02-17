from . import db
from flask_login import UserMixin

class Tree(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    wirecolor_trunk = db.Column(db.Integer, db.ForeignKey('trunk.id'))
    base = db.Column(db.Integer, db.ForeignKey('base.id'))
    treetype_id = db.Column(db.Integer, db.ForeignKey('treetype.id'))
    price = db.Column(db.Integer)
    led = db.Column(db.Integer, db.ForeignKey('led.id'))
    measurements = db.Column(db.Integer, db.ForeignKey('measurements.id'))

class Trunk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trunktype_id = db.Column(db.String(100))
    
class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basetype_id = db.Column(db.String(100))

class Led(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    ledtype_id = db.Column(db.String(100))

class Attribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tree_id = db.Column(db.Integer, db.ForeignKey('tree.id'))
    materials_id = db.Column(db.Integer, db.ForeignKey('materials.id'))

class Treetype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    treetype_id = db.Column(db.Integer, db.ForeignKey('materials.materialtype_id'))
    treetype = db.Column(db.String(100))

class Materials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    materialtype_id = db.Column(db.Integer)
    materials = db.Column(db.String(100))

class Measurements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    treeheight = db.Column(db.Integer)
    treewidth = db.Column(db.Integer)
    treelength = db.Column(db.Integer) 
    socketwidth = db.Column(db.Integer)
    socketlength = db.Column(db.Integer)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loginname = db.Column(db.String(100))

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
