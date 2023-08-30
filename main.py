import argparse
import numpy as np
from lib import buffer_audio, transcribe_audio, generate_notes, convert_audio_to_pcm
# Define arguments for the program
parser = argparse.ArgumentParser(description='Transcribe a lecture and produce notes from it')
parser.add_argument('-o', '--output', default='output.md', help="The file to output the Markdown notes to")
parser.add_argument('-t', "--transcript-output", default='transcript.txt', help="The file to output the transcription text to")
parser.add_argument('-m', '--model', default='tiny.en', help="The OpenAI Whisper model to use for transcription") # In my testing, tiny.en is more than enough and should be faster and use less resources
subparsers = parser.add_subparsers(title="Subcommands", required=True, dest="subcommand")

# Transcribe directly from the microphone
microphone = subparsers.add_parser("microphone", description="Generate notes directly from the microphone")

audiofile = subparsers.add_parser("filename", description="Generate notes from an audio file")
audiofile.add_argument("filename", help="The audio file to transcribe")

args = parser.parse_args()

if args.subcommand == "microphone":
    audio_data = buffer_audio()
elif args.subcommand == "filename":
    audio_data = convert_audio_to_pcm(args.filename)

print("Transcribing...")

arr = np.frombuffer(audio_data, np.int16).flatten().astype(np.float32) / 32768.0

transcription = transcribe_audio(arr, args.model)

print("Transcription:")
print(transcription)

with open(args.transcript_output, 'w') as f:
    f.write(transcription)

print("Generating notes...")

notes = generate_notes(transcription)

print("Notes:")
print(notes)

with open(args.output, 'w') as f:
    f.write(notes)