# robo-advisor


## Installation
Use Github.com's online interface to fork this repository then clone or download your remote repository to your local computer and save it to the desktop. Then you can navigate from the command line to access file like this:
```sh
cd  ~/Desktop/robo-advisor 
```
## Setup

### Environment Setup 

Create and activate a new Anaconda virtual environment
```sh
conda create -n stocks-env python=3.7
conda activate stocks-env
```

From witin the virtual environment install the required packages specified in the "requirements.txt" file you created:
```sh
pip install -r requirements.txt
```

And from in this virtual environment run 
```sh
python app/robo_advisor.py
```
### .env file 

You should set up a .env file with your ALPHAVANTAGE API key (provided by the website). An example could be: 
```sh
ALPHAVANTAGE_API_KEY="abc123"
```
In addition you should have a the parameters for Twilio (this program is Twilio enabled) where you should have TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and the SENDER_SMS. You will need to get these credentials from Twilio. When you set up an SMS enabled project with Twilio, it will instruct you on how to get your credentials. The credentials above need to be in your .env file. You may need to install Twilio
```sh
pip install twilio
```

## Security
When you fork then download the program, there should already be two gitignore files: one in the data folder. This should cover security as means that your .env file with your credentials and prices.csv (created later) will not be read by Git.


