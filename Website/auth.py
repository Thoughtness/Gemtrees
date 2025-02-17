from flask import Blueprint, flash, render_template, request, redirect

auth = Blueprint('auth', __name__)

@auth.route('/trees')
def trees():
    return render_template("/Main/trees.html")

@auth.route('/order')
def order():
    return render_template("/Main/order.html")

@auth.route('/how-to')
def how_to():
    return render_template("/Main/how_to.html")

@auth.route('/about-me')
def about_me():
    return render_template("/Main/about_me.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template("/Admin/sign_up.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("/Admin/login.html")

@auth.route('/create-entry', methods=['GET', 'POST'])
def create_entry():
    if request.method == 'POST':
        treetype = request.form.get('treetype')    
        trunk = request.form.get('trunk')    
        base = request.form.get('base')    
        led = request.form.get('led')   
        materials = request.form.getlist('materials')    
        treeheight = request.form.get('treeheight')    
        treewidth = request.form.get('treewidth')    
        treelength = request.form.get('treelength')    
        socketwidth = request.form.get('socketwidth')    
        socketlength = request.form.get('socketlength')

        data = request.form
        print(data)

        if len(materials) < 1:
            flash(message='Select at least one material', category='error')
        elif len(treeheight) < 1 or len(treewidth) < 1 or len(treelength) < 1 or len(socketwidth) < 1 or len(socketlength) < 1:
            flash(message='Measurements missing', category='error')
        else:
            flash(message='Entry created', category='success')   

    return render_template("/Admin/create_entry.html")

@auth.route('/add-materials', methods=['GET', 'POST'])
def add_materials():
    if request.method == 'POST':
        type = request.form.get('treetype')    
    return render_template("/Admin/add_materials.html")