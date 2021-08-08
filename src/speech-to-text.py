
# Imports the Google Cloud client library
from google.cloud import speech
import io

def main():
	# Instantiates a client
	client = speech.SpeechClient()
	# The name of the audio file to transcribe
	content = get_audio_file_pointer('out.wav')
	# Get audio data for recognition
	audio = speech.RecognitionAudio(content=content)
	# Get config for speech recognition
	config = get_recoginition_config()
	# Detects speech in the audio file
	response = client.recognize(config=config, audio=audio)
	# Get transcript from response
	transcript = get_all_transcript(response)
	# Calculate wpm from transcript of 2 min audio
	wpm = calculate_wpm(transcript)
	print(wpm)


def get_audio_file_pointer(filename):
	speech_file = '/src/audios/' + filename
	with io.open(speech_file, 'rb') as f:
		content = f.read()
	return content

def get_recoginition_config():
	return speech.RecognitionConfig(
		encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
		language_code="en-US",
		audio_channel_count=2
	)

def get_all_transcript(response):
	all_transcript = ''

	if 'results' in response:
		for result in response.results:
			all_transcript += result.alternatives[0].transcript

	print(all_transcript)
	return all_transcript

def calculate_wpm(transcript):
	transcript = transcript.replace('.', '')
	return len(transcript.split(' ')) / 2

main()