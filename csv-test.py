import py_midicsv
import csv

# Load the MIDI file and parse it into CSV format
csv_string = py_midicsv.midi_to_csv("BB.mid")

#
print(csv_string[100])
print(csv_string)
#
# f = open(csv_string)
# csv_f = csv.reader(f)
#
# for row in csv_f:
#   print(row)

# with open(csv_string, newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

#

# Parse the CSV output of the previous command back into a MIDI file
midi_object = py_midicsv.csv_to_midi(csv_string)

# Save the parsed MIDI file to disk
with open("example_converted.mid", "wb") as output_file:
    midi_writer = py_midicsv.FileWriter(output_file)
    midi_writer.write(midi_object)