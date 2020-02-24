# robo-advisor


## Installation
Use Github.com's online interface to fork this repository then clone or download your remote repository to your local computer. Then navigate from the command line (assuming you are running it from the local repository's root directory):
```sh
cd robo-advisor
```
You could also download it to your desktop in which case use this command line to access file:
```sh
cd  ~/Desktop/robo-advisor 
```
## Setup

Create and activate a new Anaconda virtual environment
```sh
conda create -n stocks-env python=3.7
conda activate stocks-env
```
And from in this virtual environment run 
```sh
python robo_advisor.py
```
Remeber to

## Security
Also remember to create a .env file with your secret key for storage (for the alphavantage API) and a .gitignore file for security if your git repository is public. The gitignore file should have a .env. 


