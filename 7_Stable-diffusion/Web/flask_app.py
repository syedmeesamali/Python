from flask import *
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)       #Define the flask app thing
bootstrap = Bootstrap(app)

app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF", "DOCX", "RAR", "PDF", "XLS", "XLSX", "TXT"]
app.config['SECRET_KEY'] = 'my_rand_secret_key_here'
app.config['MAX_CONTENT_LENGTH'] = 0.5 * 1000 * 1000             #Accept only up to 16MB of file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['IMAGE_UPLOADS'] = '/static/uploads'

db = SQLAlchemy(app)

#ORM model for the links
class Link(db.Model):
    __tablename__ = "links"
    id = db.Column(db.Integer, primary_key = True)
    link_name = db.Column(db.String(100), nullable = False)
    link_url = db.Column(db.String(200), nullable = False)
    link_type = db.Column(db.String(40), nullable = False)
    read = db.Column(db.Boolean, default = False, nullable = False)
    date_created = db.Column(db.Date, default = datetime.utcnow)
    date_read = db.Column(db.Date)

#Main model for the messages to be received from users.
class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    date_val = db.Column(db.String(40), default = datetime.utcnow)
    message = db.Column(db.String(1000), nullable = False)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"), 500

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/save_form', methods=['POST'])
def save_form():
    try:
        Name1 = request.form.get('name_val')
        Email1 = request.form.get('email')
        Title1 = request.form.get('title')
        Message1 = request.form.get('message')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_post = Post(name = Name1, title = Title1, email = Email1, date_val = timestamp, message = Message1)
        #post1 = Post(name='ali', title='title1',email='ali@ali.co',date_val='sunday',message='message-1')
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"success": True})
    except:
        return jsonify({"success": False})

@app.route('/blog')
def blog():
    return render_template("robotic_arm.html")

#Allowed type of files for upload
def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

#Allowed type of files for upload
def allowed_image_size(filesize):
    if int(filesize) < app.config['MAX_CONTENT_LENGTH']:
        return True
    else:
        return False

@app.route('/upload-image', methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                flash('No selected file! Please select file to upload')
                return redirect(request.url)
            if not allowed_image_size(request.cookies.get('filesize')):
                flash('Size exceeds limit!')
                return redirect(request.url)
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                picture_path = os.path.join(app.root_path, 'static/uploads', filename)
                image.save(picture_path)
                return redirect(url_for('uploaded'))
            else:
                flash('Some error !')
                return redirect(request.url)
    return render_template('upload_image.html')

@app.route('/uploaded')
def uploaded():
    image_names = os.listdir(os.path.join(app.root_path, 'static/uploads'))
    return render_template('uploaded.html', image_names = image_names)

@app.route('/uploaded/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    full_path = os.path.join(app.root_path,  'static/uploads')
    return send_from_directory(full_path, filename)

if __name__ == "__main__":
    app.run(debug=True)