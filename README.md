# Electrolarynx_Capstone

# Getting started

start by getting the relevant requirements installed on your machine by using `: pip install -r requirements.txt`. If you want to do so in a virtual environment, feel free to. You should be able to run al the relevant notebooks and source files when that runs. If you're running on Rivanna, make sure you have a terminal window opened and `:cd` to this repository before continuing.

# Importing Dataset

Assuming you have our dataset in a box shared link, you can recursively add the dataset to your clone of this repository by running `$ cd source` followed by `$ python dataset_builder.py`. This script will ask you for 3 credentials, two for the Oauth creds and 1 developer token. Both of these can be built in the [developers_console](https://virginia.app.box.com/developers/console) of the UVABox. Once it has these connections, it'll check to see if you have a "data" repository already there. If it does not, it'll pull all the data from the given shared box link url and store it in a new /data directory. Don't worry, this is added to the .gitignore so you won't accidentally upload a few gigabytes to github. 

If the `data/` directory does exist already, then this will ask if you want to overwrite it. If you do, it *DELETES ALL EXISTING FILES* in that directory and replaces them with whatever is in that box link. proceed with caution here. 

The other source files are expecting that `data/` directory to be there and populated so please make sure that runs to completion before continuing. Will likely take at least 20 min.


### UVA MSDS Capstone Project: Deep Learning STT Models for Patients using Electrolarynx devices

# Purpose
    - TBD

# Downloading and getting started
    - TBD

# Method
    - TBD

# Performance
    - TBD

# Ownership

### Authors
    - Will Johnson 
    - Mani Shanmugavel
    - Chris Lee

### Sponsors
    - TBD

### Academic Advisor
    - TBD
