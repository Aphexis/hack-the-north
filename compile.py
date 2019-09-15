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
    harm = mido.MidiFile('four-chord2.mid', clip=True)


    mid = MidiFile()
    perc = bass(bassSong)
    mel = melody(melodySong)
    mid.tracks.append(mel)
    mid.tracks.append(perc)


    # mid.tracks.append(track)
    # BassMidi = mido.MidiFile('bass.mid', clip=True)
    # MelodyMidi = mido.MidiFile('melody.mid', clip=True)
    mid.ticks_per_beat = 70
    mid.tracks.append(harm.tracks[0])
    midi.tecks_per_beat = 120
    # for msg in mido.merge_tracks(BassMidi.tracks):
    #     track.append(msg)
    # for msg in mido.merge_tracks(MelodyMidi.tracks):
    #     track.append(msg)

    mid.save('final.mid')

    # fs = FluidSynth()
    # fs.midi_to_audio('final.mid', 'final.wav')

compile('Dragons.mid','BB.mid')