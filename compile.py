import mido
from midi2audio import FluidSynth
from mido import *
import music21
from mido import MidiFile, MidiTrack
from music21 import *
from F2 import melody
from Bass import bass

def compile(melodySong, bassSong):

    melody(melodySong)
    bass(bassSong)

    mid = MidiFile()
    track = MidiTrack()

    mid.tracks.append(track)
    BassMidi = mido.MidiFile('bass.mid', clip=True)
    MelodyMidi = mido.MidiFile('melody.mid', clip=True)
    mid.ticks_per_beat = 70

    for msg in mido.merge_tracks(BassMidi.tracks):
        out = str(msg)
        track.append(mido.Message.from_str(out))
    for msg in mido.merge_tracks(MelodyMidi.tracks):
        out = str(msg)
        track.append(mido.Message.from_str(out))

    mid.save('final.mid')
    FluidSynth().midi_to_audio('final.mid', 'final.wav')
