# Imports the Google Cloud client library
from google.cloud import speech
import io

class AudioRecognition:
	def __init__(self, filename):
		self.client = self.get_speech_client()
		self.config = self.get_recoginition_config()
		self.audio_filename = '/src/audios/' + filename

	def get_speech_client(self):
		return speech.SpeechClient()

	def get_recoginition_config(self):
		return speech.RecognitionConfig(
			encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
			language_code="en-US",
			audio_channel_count=2
		)

	def get_audio_file_content(self):
		speech_file = self.audio_filename
		with io.open(speech_file, 'rb') as f:
			content = f.read()
		return content

	def get_recognition_audio(self):
		content = self.get_audio_file_content()
		return speech.RecognitionAudio(content=content)

	def get_recognized_result(self):
		audio = self.get_recognition_audio()
		return self.client.recognize(config=self.config, audio=audio)

	def get_all_transcript(self, response):
		all_transcript = ''

		if 'results' in response:
			for result in response.results:
				all_transcript += result.alternatives[0].transcript

		return all_transcript

	def calculate_wpm(self, transcript):
		transcript = transcript.replace('.', '')
		return len(transcript.split(' ')) / 2