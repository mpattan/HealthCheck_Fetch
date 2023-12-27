
# health-check
## Installation
<!-- #Please include instructions on how to install and run your code -->
**1. Clone the GitHub Repository:**

First, clone the GitHub repository to your local machine using the following command:
```bash
git clone https://github.com/mpattan/HealthCheck_Fetch.git
```
**2. Navigate to the Repository Directory:**

Change your current working directory to the cloned repository directory:

```bash
cd HealthCheck_Fetch
```
**3. Setup the Virtual Environment:**

Note: In windows python3 is replaced by python

Setup a virtual environment:
```bash
python3 -m venv ./venv
```
Activate the virtual environment(Fill in the current working directory in the PATH):
```bash
source ${PATH}/venv/bin/activate # Mac Os or Linux

venv\Scripts\activate # Windows
```
**4. Install the dependencies**
```bash
python3 -m pip install -r requirements.txt
```

**5. Develop the Module**

Run the following command to develop the module using Python3:

```bash
python3 setup.py develop
```

## Usage
For the tool to work, you need to provide the path of the <span style="color: violet">YAML</span> file. The tool accepts the following command-line arguments:

1. -h, --help: show the help message and exit
```
HC -h         
usage: HC [options] path

Health Check - Provides the availability percentage of the HTTP endpoints

positional arguments:
  path        Enter path to yaml file

optional arguments:
  -h, --help  show this help message and exit

Example: HC input.yaml, 
         HC /Users/{user}/Code/HealthCheck_Fetch/input2.yaml
```
2. path: Enter path to yaml file
```bash
HC input.yaml
```
3. Provide the absolute path to the YAML file
```bash
HC input.yaml /Users/{user}/Code/HealthCheck_Fetch/input2.yaml
```

## Testing

To run the tests, run the following command:

```bash
pytest test
```

## Author
Mohammed Sarfraz Khan Pattan