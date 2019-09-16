# SongWeave
## What it does
Going onto our web app, you are given three song choices: one for the Melody, one for the Harmony, and one for the Beat. The respective parts of each of these songs are then extracted and recombined to your own personalized song available for download. A history bar of your previous remixes is also remembered to allow downloads at a later date.
## How we built it
Using JQuery for most of the frontend, we interfaced with Spotify's API to retrieve the song lists from their databases. The remixing is passed via HTTP Requests to the python backend, using the Flask framework. It is then converted into MIDI and analyzed using Mido, allowing us to extract the constituent parts of each song. We then use the same library to recombine the parts into one new song, ultimately uploading it into a Google Cloud Storage bucket. Links from this bucket are then sent to the web app to allow users to download their remixed pieces.
## Challenges we ran into
We had difficulty finding appropriate MIDI analytic libraries with adequate documentation to allow us to do the processing required to distinguish between different parts of the song and splice them up. The fact that nobody in the team had previous experience with Google Cloud also meant a large portion of time was spent on understanding buckets, blobs, and other data structure conventions set by the platform.
## Accomplishments that we're proud of
We managed to fully isolate certain channels on a MIDI file, send requests to download/upload music files up to Google Cloud Storage and integrate the web app with the processing backend via API.
## What we learned
- Python, most importantly its Flask frameworks and Google Cloud clients.

## What's next for SongWeave
"Smarter" Song creation by analyzing a user's song tastes.
Optimize uploading/downloading of audio files to reduce overhead when calling the Google Cloud Platform.
