# from flask import Flask
import sounddevice as sd
import librosa

# app = Flask(__name__)
 
# @app.route("/")
def main():
    name = input("Enter name of song:")
    fs = 44100
    sd.default.samplerate = fs
    sd.default.channels = 2
    duration = 9
    rec = sd.rec(int(duration * fs), dtype='float64')
    sd.wait()
    librosa.output.write_wav(name+"Hum.wav", rec, fs)
    print("Done.")
 
# if __name__ == "__main__":
#     app.run()

main()


