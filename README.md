## In this repo, I suggested 2 way to autofill response in Google Form
### Autofill using selenium
This way used to create similar response in google form or you can generate random choice
### Autofill using fetching API
I pretty like this way, you can fake all your response in a .xlxs file and then fetch it to API of Google Form. You can modify data in whatever you want

## Installation
First of all, clone this repo into your laptop
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install virtual environment (env)

```bash
python -m pip install --user virtualenv
```
Then create a virtual environment
```bash
virtualenv env
```
Run your environment
```bash
.\env\Scripts\activate
```
Install every package to run project
```bash
pip install -r .\requirements.txt
```
Finally, cd to your file you choose and run 
```bash
py main.py
```
