from flask import Blueprint, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

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

@auth.route('/login', methods=['POST'])
def login():
    data = request.form
    print(data)
    return render_template("/Admin/login.html")

@auth.route('/create-entry')
def index():
    return render_template("/Admin/create_entry.html")

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
        uploaded_file = request.files['file']

        data = request.form
        print(data)
        print(uploaded_file)

        if len(materials) < 1:
            flash(message='Select at least one material', category='error')
        elif len(treeheight) < 1 or len(treewidth) < 1 or len(treelength) < 1 or len(socketwidth) < 1 or len(socketlength) < 1:
            flash(message='Measurements missing', category='error')
        elif uploaded_file.filename == '':
            flash(message='No pictures selected', category='error')
        else:        
            for uploaded_file in request.files.getlist('file'):
                if uploaded_file.filename != '':
                    uploaded_file.save('Website/static/Pictures/' + secure_filename(uploaded_file.filename))
            flash(message='Entry created', category='success') 
        return redirect(url_for('auth.create_entry'))

    return render_template("/Admin/create_entry.html")


@auth.route('/add-materials', methods=['GET', 'POST'])
def add_materials():
    if request.method == 'POST':
        type = request.form.get('treetype')    
    return render_template("/Admin/add_materials.html")