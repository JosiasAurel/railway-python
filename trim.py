from pydub import AudioSegment


def trim_stuff():
    song = AudioSegment.from_mp3("song.mp3")
    ten_seconds = 10 * 1000

    # slice out the first 10 secs of the video
    first_10_secs = song[:ten_seconds]

    first_10_secs.export("mod.mp3", format="mp3")
