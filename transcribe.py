import argparse
from pydub import AudioSegment
import speech_recognition as sr

def transcribe_audio(file_path, language='hi-IN'):
    try:
        # Load the audio file
        audio = AudioSegment.from_file(file_path)

        # Convert to WAV format
        wav_path = "converted_audio.wav"
        audio.export(wav_path, format='wav')

        # Initialize recognizer
        recognizer = sr.Recognizer()

        # Transcribe the audio
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            transcription = recognizer.recognize_google(audio_data, language=language)
        
        return transcription
    except Exception as e:
        return f"Error: {e}"

def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="Transcribe audio to text.")
    parser.add_argument("-f", "--file", type=str, required=True, help="Path to the audio file")
    parser.add_argument("-l", "--language", type=str, default="hi-IN", help="Language code for transcription (default: hi-IN for Hindi)")
    args = parser.parse_args()

    # Transcribe audio
    result = transcribe_audio(args.file, args.language)
    print("Transcription:")
    print(result)

if __name__ == "__main__":
    main()