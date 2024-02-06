<b>Password Generator</b>

This is a simple Django project that auto generates passwords for users based on their preferences. Users can specify the length, case and special characters of the password they want.

<b>Features</b>
•  Users can enter the desired length of the password (minimum 6, maximum 11).

•  Users can choose whether they want the password to be upper case, lower case or mixed case.

•  Users can choose whether they want the password to include special characters and numbers (such as !, 7, 0, 9, @, #, etc.) or not.

•  Users can copy the generated password to the clipboard with one click.

•  Users can generate a new password with different settings without reloading the page.

<b>Installation</b>

Clone this repository to your desired location:

git clone https://github.com/LnPaulin/Password_gen.git
To run this project locally, you will need Python 3.6 or higher and Django 3.2 or higher installed on your machine. You can install Django using pip:

pip install django
All requirements for the project are found in the requirements file. run pip install -r requirements.txt to install them

Then, clone this repository to your desired location:

git clone https://github.com/LnPaulin/Password_gen.git

Navigate to the project directory and run the following command to start the development server:

python manage.py runserver

You should see a message like this:

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 27, 2023 - 20:15:39
Django version 3.2.4, using settings 'password_generator.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Now you can open your browser and go to http://127.0.0.1:8000/ to see the project in action.

<b>Usage</b>

To use the password generator, follow these steps:

•  Select the length of the password you want.

•  Choose the case of the password you want by clicking on one of the radio buttons labeled "Upper".

•  Choose whether you want the password to include special characters and or numbers clicking on the checkbox labeled "Special Characters" and "Numbers"

•  Click on the button labeled "Generate Password" to generate a random password based on your settings.

•  You will see the generated password

•  You can generate a new password with different settings by changing the input values and clicking on the "Generate Password" button again.
<br>

<b>Screenshots</b>
<p align="center">
Installing requirements: <br/>
<img src="https://i.imgur.com/7PqpOg2.png" width="80%" alt="requirements"/>
<br />
<br />
Running ther server: <br/>
<img src="https://i.imgur.com/Z2Vehfc.png" width="80%" alt="django_server"/>
<br /><br />
  Project on Browser <br/>
<img src="https://i.imgur.com/ivGW10w.png" width="80%" alt="dashboard"/>
<br /><br />
   Generated Password <br/>
<img src="https://i.imgur.com/pBsgSn9.png" width="80%" alt="dashboard"/>
<br /><br />

  ✅ Test it out here https://password.gitcotech.net 
</p>
