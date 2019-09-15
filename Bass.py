import mido
from mido import Message, MidiFile, MidiTrack


def bass(filename):

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    midi = mido.MidiFile(filename, clip=True)


    for msg in mido.merge_tracks(midi.tracks):
        if msg.is_meta:
            track.append(msg)
            # print("meta message")
        else:
            # print(msg)
            # track.append(msg)
            out = str(msg)
            pos = out.find("channel=")
            # print()

            if out[pos+8:pos+9] == '9':
                track.append(msg)
                print(out)
    mid.ticks_per_beat = 70
    mid.save('bass.mid')
    return track

# bass('BB.mid')
#
# def base_remove(filename):
#     midi = mido.MidiFile(filename, clip=True)
#     for msg in mido.merge_tracks(midi.tracks):
#     # for track in mid.tracks:
#         # for msg in track:
#         if not msg.is_meta:
#             out = str(msg)
#             pos = out.find("channel=")
#             if not out[pos+8:pos+9] == '9':
#                 del msg
#                 print(out)
#     midi.save('channel-10.mid')

# base_remove('BB.mid')

# channel10 = mido.MidiFile('channel10.mid', clip=True)
# print("")
# print("channel 10 good midi")
# for msg in channel10:
#     print(msg)

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