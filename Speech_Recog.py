from speech_recognition import Microphone , Recognizer, AudioFile, UnknownValueError,RequestError
def callback(recognizer,source):
    try:
        recognized = recognizer.recognizer_google(source)
        print("You said ", recognized)

    except RequestError as exc:
        print(exc)

    except UnknownValueError:

        print("Unable to recognizer")
def listen():
    recog = Recognizer()
    mic = Microphone()
    with mic:
        recog.adjust_for_ambient_noise(mic)

    print("Talk")
    audio_stopper=recog.listen_in_background(mic,callback)
    sleep(120)
    audio_stopper(wait_for_stop=False)

def foo():
    while True:
        print("hello")
        sleep(1)
listen()
foo()
