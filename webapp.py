# from flask import Flask
import sounddevice as sd

# app = Flask(__name__)
 
# @app.route("/")
def main():
    fs = 44100
    sd.default.samplerate = fs
    sd.default.channels = 2
    duration = 2
    rec = sd.rec(int(duration * fs), dtype='float64')
    sd.wait()
    print(rec) 
 
# if __name__ == "__main__":
#     app.run()

main()


