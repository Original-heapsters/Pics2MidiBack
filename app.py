import json
import os
import midiStuff
from flask import Flask, request, url_for, redirect, render_template, abort, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
midStuff = midiStuff.midiStuff()
UPLOAD_FOLDER = "./static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():

    return "index"

@app.route('/prettyjson')
def prettyjson():
    # img = cv2.imread('dog.jpg')
    # # cv2.startWindowThread()
    # # cv2.namedWindow("preview")
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    listOfGarbage = ["one", "two", 4, "cool"]
    anotherListOfGarbage = ["four", "five", 200, "what"]
    dictionaryOfStuff = {"here is a cool list one" : listOfGarbage, "something else" : anotherListOfGarbage}
    print(json.dumps(dictionaryOfStuff, indent=4))
    return(json.dumps(dictionaryOfStuff))

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        print("enetered method")
        # check if the post request has the file part
        file = request.files['photo']
        print("got file")
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return "there is no file"
            # flash('No selected file')
            # return redirect(request.url)
        if file:
            print "in the if"
            filename = secure_filename(file.filename)
            filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filePath)
            output = midStuff.plotPoints(pathToImage=filePath)

            # midi operations
            # midiFilePath = midiStuff.getPath()

            outPutJson = {"OriginalImage": request.url_root + "static/" + file.filename, "midiData":str("output"), "MidiUrl": "temporary string for midiFilePath"} # midiFilePaths will be given later

            return json.dumps(outPutJson, indent=4)
    return
# @app.route('/upload')
# def upload():
#     # allow user to upload file
#     # i need to use that file to allow operations on it
#     # save midi file such as "static" file
#     # give user url 'you can get midi file here'
#     return "Here is the upload page"

# tasks:
# make midi file from points
# make midi file available from static directory to user

@app.route('/testMidiStuff')
def testMidiStuff():
    # output = midStuff.plotPoints()
    return str(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)