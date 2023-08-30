# Note Writer

This tool uses on-device OpenAI Whisper language models, along with `gpt-3.5-turbo-16k` to transcribe college lectures, and turn them into usable notes for students. This is designed to supplement personal note-taking, and allow for students to review information they may have missed. Since many colleges don't allow students to record lectures, this tool includes an option to transcribe directly from the microphone, without ever producing an audio file. In this mode, audio data is never stored and never leaves the device.

## Usage

```sh
poetry install # Install dependencies

poetry run python main.py microphone # Run the tool of microphone input
# OR
poetry run python main.py file ./path_to_audio_file.mp3 # Run the tool on an audio file
```

```
options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        The file to output the Markdown notes to
  -t TRANSCRIPT_OUTPUT, --transcript-output TRANSCRIPT_OUTPUT
                        The file to output the transcription text to
  -m MODEL, --model MODEL
                        The OpenAI Whisper model to use for transcription

Subcommands:
  {microphone,file}
```
