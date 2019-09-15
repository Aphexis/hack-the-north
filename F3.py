from music21 import *
import music21
# from mido import MidiFile
import mido


def calcMelody(name):
    mf = midi.MidiFile()
    mf.open(name, attrib='rb')
    mf.read()

    piece = converter.parse(name)
    h = 0
    arr = []
    domo = 0

    for part in piece.parts:
        #print(part.partName)

        if part.partName == 'Voice' or part.partName == 'Vocal' or part.partName == 'Flute' or part.partName == 'Oboe':
            domo = 1
            break
        h += 1

    print (h)
    return h
