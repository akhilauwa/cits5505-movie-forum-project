# cits5505-movie-forum-project
This is a website for film enthusiasts to read and request movie insights, recommendations, and discussions.

TODO: a description of the purpose of the application, explaining the design and use.

## Features
TODO: a list of features that the application provides.

## Collaborators
| UWA ID    | Name            | GitHub Username |
|-----------|-----------------|-----------------|
| 23729213  | Akhila Liyanage | akhilauwa       |
| 24073955  | Yumin Zeng      | Austin1900      |
| 24079757  | Junwu Chen      | jcfive          |
| 24080897  | Wanqi Zhang     | Khalesssi       |

## Project Architecture

## Getting Started
### Requirements
- [Python 3.9 or newer](https://www.python.org/downloads/)
- [Pip 21.1 or newer](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (Optional)
### Installation
Follow these steps to set up the flask web application on your local machine:s
#### Clone the project repository:
```
git clone https://github.com/akhilauwa/cits5505-movie-forum-project
```
#### Navigate to the project directory:
```
cd cits5505-movie-forum-project
```
#### Create a Python Virtual Environment (Optional)
This step is optional but recommended. To create a virtual environment, run the following command:
```
python3 -m venv venv
```
To activate the virtual environment, run one of the following commands depending on your operating system:
```
source venv/bin/activate    # Linux or macOS
venv/Scripts/activate       # Windows
```
To deactivate the virtual environment, run the following command:
```
deactivate
```
#### Install the dependencies:
If a virtual environment is used, activate it first. Then, run the following command:
```
pip install -r requirements.txt
```
This command will install all the libraries and tools specified in the requirements.txt file.

### Run the Application
To run the application, run the following command:
```
flask run
```
The application will be running on http://localhost:5000/ by default.

### Testing
To run the test suite, run the following command:
```
pytest
```
