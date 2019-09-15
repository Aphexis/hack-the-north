import mido
from mido import Message, MidiFile, MidiTrack
from F3 import calcMelody

def melody(filename):

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    midi = mido.MidiFile(filename, clip=True)

    a = calcMelody(filename)
    if a != 16:
        for msg in mido.merge_tracks(midi.tracks):
            out = str(msg)
            pos = out.find("channel=")
            if out[pos+8:pos+9] == str(a):
               track.append(mido.Message.from_str(out))
                    #print(out)
    mid.save('melody.mid')
    return track
