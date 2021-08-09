from dbmanipulation import DBManipulation
from audiorecognition import AudioRecognition

def main():
	# recognizer = AudioRecognition('out.wav')
	# response = recognizer.get_recognized_result()
	# transcript = recognizer.get_all_transcript(response)
	# wpm = recognizer.calculate_wpm(transcript)
	# print(transcript)

	db = DBManipulation()
	# video_urlはどこから取得する？
	sql = db.make_bulk_insert_query('video_wpms', {'wpm': 100.5, 'video_url': 'https://www.youtube.com/watch?v=XjU0lPXry5E'})
	# db.save_result(result={'wpm': wpm, 'video_url': 'https://www.youtube.com/watch?v=XjU0lPXry5E'})
	print(sql)

if __name__ == '__main__':
	main()