import pymysql.cursors

class DBManipulation:
	connection = None

	def __init__(self):
		self.connection = self.get_db_connection()

	def get_db_connection(self):
		# Connect to the database
		connection = pymysql.connect(host='192.168.99.103',
									port=3636,
									user='pyuser',
									password='pypasswordlocal',
									database='python_db',
									cursorclass=pymysql.cursors.DictCursor)
		return connection

	def save_result(self, result):
		self.insert_data_to_db(table='video_wpms', result=result)

	def insert_data_to_db(self, table, result):
		sql = self.make_bulk_insert_query(table=table, result=result)

		with self.connection:
			with self.connection.cursor() as cursor:
				# Create a new record
				cursor.execute(sql)
			# connection is not autocommit by default. So you must commit to save
			# your changes.
			self.connection.commit()

	def make_bulk_insert_query(self, table, result):
		final_sql = ''
		sql = f'INSERT INTO `{table}` '

		keys = ','.join(result.keys())
		keys_sql = f'({keys}) '

		values = []
		for value in result.values():
			if isinstance(value, float):
				values.append(str(value))
			elif isinstance(value, str):
				values.append(f'"{value}"')

		values_str = ','.join(values)

		values_sql = f'VALUES ({values_str})'
		final_sql = sql + keys_sql + values_sql
		return final_sql

	def get_video_info(self):
		with self.connection:
			with self.connection.cursor() as cursor:
				# Read a single record
				sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
				cursor.execute(sql, ('webmaster@python.org',))
				result = cursor.fetchone()
		return result