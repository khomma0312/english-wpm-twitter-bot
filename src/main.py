from __future__ import unicode_literals
import youtube_dl
import os
from pydub import AudioSegment

def main():
	original_audio_path = download_audio()
	slice_downloaded_audio(original_audio_path)
	remove_file(original_audio_path)

def download_audio():
	output_audio_path = make_audio_file_path('test-en.wav')

	ydl_opts = {
		'format': 'bestaudio/best',
		'outtmpl': "audios/test-en" + '.%(ext)s',
		'postprocessors': [
			{'key': 'FFmpegExtractAudio',
			'preferredcodec': 'wav',
			'preferredquality': '192'},
			{'key': 'FFmpegMetadata'},
		],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download(['https://www.youtube.com/watch?v=XjU0lPXry5E'])
	
	return output_audio_path

def slice_downloaded_audio(original_audio_path):
	sound = AudioSegment.from_wav(original_audio_path)
	# 最初の2分間のみ取り出す
	period = 40 * 1000
	processedAudio = sound[:period]
	processedAudio.export(make_audio_file_path('out.wav'), format='wav')

def make_audio_file_path(filename):
	return '/src/audios/' + filename

def remove_file(path):
	os.remove(path)

if __name__ == '__main__':
	main()