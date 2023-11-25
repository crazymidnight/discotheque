from pedalboard import Pedalboard, Reverb, Delay
from pedalboard.io import AudioFile

board = Pedalboard([Reverb(), Delay()])


with AudioFile(
    "JINGLE BELLS - FRANK SINATRA - Peipont - The Ken Lane Singers.mp3"
) as file:
    # Open an audio file to write to:
    with AudioFile("processed.wav", "w", file.samplerate, file.num_channels) as output_file:
        # Read one second of audio at a time, until the file is empty:
        while file.tell() < file.frames:
            chunk = file.read(file.samplerate)

            # Run the audio through our pedalboard:
            effected = board(chunk, file.samplerate, reset=False)

            # Write the output to our output file:
            output_file.write(effected)
