import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from detect import run
import time
from label_description import label as lb

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
        # # check if the post request has the file part
        # if 'file' not in request.files:
        #     #flash('No file part')
        #     return redirect(request.url)
        # file = request.files['gambar']
        # print(file)
        # # If the user does not select a file, the browser submits an
        # # empty file without a filename.
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     return redirect(url_for('download_file', name=filename))
    if request.method == "GET":
        return render_template("home.html")


@app.route("/hasil", methods=["GET","POST"])
def show_result():
    # add_header()
    if request.method != "POST":
        return redirect("index.html")
    else:

        print("Ada request post")
        print(request.files)
        file_gambar = request.files['gambar']
        print("Ini gambarnya guys: \n", file_gambar)

        file_gambar.save("uploads/image_tobe_predicted.jpg")

        # prediksi
        import os
        if len(os.listdir("./static")) > 0:
            os.remove("./static/image_tobe_predicted.jpg")

        predicted_label = run(source="./uploads/image_tobe_predicted.jpg", exist_ok=True, project="./static", name="")
        print("PREDICTED LABEL", predicted_label)
        return render_template("hasil.html", result=lb[predicted_label])

@app.route("/getstarted")
def get_started_page():
    return render_template("index.html")

@app.route("/webgis")
def webgis():
    return render_template("webgis.html")


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def hello_world():
    return render_template('index.html')