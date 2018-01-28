import imageStuff
import mido
from mido import MidiFile, Message, MidiFile, MidiTrack

class midiStuff:
    def __init__(self, midiData=None, points=[]):
        self.points = points
        self.midiData = midiData
        print("initialized")

    # x value: turn on and off
    # y value: map to midi musical note (midi g or c note), maybe 0-100 min and max number
    # if there are 5 notes, divide by 5
    def plotPoints(self):
        print("* POINTS *")
        pathToImage = "shrek2.jpg"
        imgStuff = imageStuff.imageStuff(path=pathToImage)

        myPoints = imgStuff.getPoints()
        self.points = myPoints
        print("POINTS FROM imageStuff")
        return self.points

    # possibly use either optimize or fitToModel
    # optimize to make midi song sound good, may not be necessary
    def optimize(self):
        return
    # if optimize does not work out, use an existing machine learning model
    def fitToModel(self):
        return

    def openMidiFile(self):
        mid = MidiFile('lavender-town.mid')
        return

    # https://mido.readthedocs.io/en/latest/midi_files.html
    # create midi file
    def createFile(self):
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)

        track.append(Message('program_change', program=12, time=0))
        track.append(Message('note_on', note=64, velocity=64, time=32))
        track.append(Message('note_off', note=64, velocity=127, time=50))

        mid.save('new_song.mid')
        return

    # print out all messages in the file,
    def printAllFileMessages(self):
        for i, track in enumerate(mid.tracks):
            print('Track {}: {}'.format(i, track.name))
            for msg in track:
                print(msg)

# can test code in this class
if __name__ == "__main__":
    midiStuff = midiStuff()
    midiStuff.plotPoints()
    # midiStuff.fitToModel()
    # midiStuff.optimize()
    # midiStuff.openMidiFile()
    # midiStuff.createFile()
    # midiStuff.printAllFileMessages()
