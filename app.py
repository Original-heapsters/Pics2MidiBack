import json
from flask import Flask, request, url_for, redirect, render_template, abort, send_from_directory

app = Flask(__name__)
vis = VisualGenerator.VisualGenerator(name="BOBBY")
img = imageStuff.imageStuff()
midi = midiStuff.midiStuff()

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

@app.route('/upload')
def upload():
    return "Here is the upload page"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)