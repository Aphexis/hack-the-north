import mido
from mido import Message, MidiFile, MidiTrack
from F3 import calcMelody

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

midi = mido.MidiFile('Backstreet Boys - I Want It That Way.mid', clip=True)

a = calcMelody('Backstreet Boys - I Want It That Way.mid')

for msg in mido.merge_tracks(midi.tracks):
    if msg.is_meta:
        track.append(msg)
        print("meta message")
    else:
        # print(msg)
        # track.append(msg)
        out = str(msg)
        pos = out.find("channel=")
        # print()

        if out[pos+8:pos+9] == str(a):
            track.append(msg)
            print(out)
mid.save('testsong.mid')

# channel10 = mido.MidiFile('channel10.midi', clip=True)


###
# for track in mid.tracks:
#     print(track)
#     if track != 10:
#         mid.tracks.remove(track)
#
# mid.save('track10.mid')
#
# for track in mid:
#     # if (event.type == 'note_on' and event.channel == 9):
#     if (event.type != 'note_on' or event.channel == 10):
#         # print("channel 10")
#         track.events.remove(track.event)
# mid.save('track10.mid')