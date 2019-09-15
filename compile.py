import mido
import fluidsynth
from midi2audio import FluidSynth
import music21
from music21 import *
from mido import MidiFile, MidiTrack
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
    mid.ticks_per_beat = 120
    # for msg in mido.merge_tracks(BassMidi.tracks):
    #     track.append(msg)
    # for msg in mido.merge_tracks(MelodyMidi.tracks):
    #     track.append(msg)

    mid.save('final.mid')
    
    #audio
    mf = midi.MidiFile()
    mf.open('final.mid')
    mf.read()
    mf.close()

    s = midi.translate.midiFileToStream(mf)
    sp = midi.realtime.StreamPlayer(s)
    sp.play()


compile('Dragons.mid','BB.mid')