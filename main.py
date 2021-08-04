# Main 

# Imports
import db_connect

# Variables
cur = db_connect.conn.cursor()
user_choice = '0'
program_running = True

# Program loop
print('Welcome!\n')
while program_running:

	while user_choice != '1' and user_choice != '2' and user_choice != '3':
		user_choice = input('\nPlease choose an option:\n(1) Login\n(2) Sign Up\n(3) Exit\n')

	# Login
	if(user_choice == '1'):
		# Reset user_choice
		user_choice = '0'


		login_select_query = 'SELECT * FROM users WHERE user_name=%s AND user_password=%s'
		
		login_user = input('Please enter your username: ')
		login_pass = input('Please enter your password: ')

		cur.execute(login_select_query, (login_user,login_pass))

		if cur.fetchall():
				print('\nYou have logged in!')
		else:
				print('\nERROR: That username and password combination does not exist. Please try again.')


	# Sign Up
	elif(user_choice == '2'):
		# Reset user_choice
		user_choice = '0'

		# Variables
		need_username = True
		user_select_query = 'SELECT * FROM users WHERE user_name=%s'
		sign_up_query = 'INSERT INTO users(user_name,user_password) VALUES (%s,%s);'

		# Get username loop
		while need_username:

			new_user = input('Please enter your username: ')

			cur.execute(user_select_query, (new_user,))

			if cur.fetchall():
				need_username = True
				print('ERROR: That username is already taken! Please try again.')
			else:
				need_username = False

		# Get password and add to database
		new_pass = input('Please enter your password: ')
		cur.execute(sign_up_query, (new_user,new_pass))
		db_connect.conn.commit()
		
	#Exit
	else:
		print('\nHave a good day!')
		program_running = False

cur.close()