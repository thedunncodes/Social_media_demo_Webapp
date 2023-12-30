# Flask Project
	A demo social media web app.

# Setting Up
	Fork this Repository into your local machine.

	Inside this repo dir, create a virtual environment with 'python -m venv Venv_name'.

	change 'Venv_name' to be your virtual environment name

	Start/activate your virtual environment with the bash script 'startvm'

	'startvm' takes an argument which is your 'Venv_name' to start your virtual env.
		USAGE: ./startvm Venv_name

	'requirements.txt' contains all the needed packages for the project.

	Install the packages in 'requirements.txt' with 'pip install -r'

	Run the 'Run.py' file to start up flask on your local machine and access the website

	You can stop the virtual machine using  the command 'deactivate'

	NOTE: make sure the bash scripts are executables if not run 'chmod +x bash_script' where
		'bash_script' is the script file

# Email config
	In the '__init__.py' file update the 'app.config['MAIL_USERNAME']' section to your prefered email for you

	to be able to test the forgot password section of the webapp

	Do the same also for 'app.config['MAIL_PASSWORD']', it's a app password for your email
