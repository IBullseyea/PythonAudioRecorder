import sounddevice as sd
import soundfile as sf
import time
import keyboard

def countdown(duration):
    print("Recording started...")
    for i in range(1, duration + 1):
        print(f"⏰ {i}")
        time.sleep(1)
        if keyboard.is_pressed('q'):
            sd.stop(True)
            return
    print("✅ Recording finished!")

def record_with_limit(filename, duration, fs, channels):
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    countdown(duration)
    sf.write(filename, myrecording, fs)
    sd.wait()

def record_until_q(filename, duration, fs, channels):
    print("Recording started... Press 'q' to stop.")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    total_time = 0
    while total_time < duration:
        print(f"⏰ {total_time+1}")
        time.sleep(1)
        total_time += 1
        if keyboard.is_pressed('q'):
            print("Stopping recording...")
            sd.stop()
            break
    sf.write(filename, myrecording[:int(total_time * fs)], fs)
    print("✅ Recording saved!")

print('1- Continues until you press q')
print('2- Continues for a certain duration')

choice = int(input('What is your choice? '))

if choice == 1:
    record_until_q(
        filename='test.wav',
        duration=86400,
        fs=44100,
        channels=2
    )
elif choice == 2:
    seconds = int(input('How many seconds? '))
    record_with_limit(
        filename='test.wav',
        duration=seconds,
        fs=44100,
        channels=2
    )
else:
    print('Invalid choice')