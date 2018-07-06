# Extracting key information from Issue description.

Dataset used : github issues from kaggle.

# Python files and what they do:
1.)Sample the datatset consisting of 10 million rows to required amount by running sampling.py

2.)Extract only those rows which has atleast 2 words common between title and description using extract.py

3.)Pre process the csv file using preproc.py

4.)TF-IDF analysis is done in analyze.py

5.)pipeline.py accepts an user given text and processes it. Run on Node server.


# Run the App
1.)Run npm install 

2.)Run pip install requirements.txt to install python dependencies.

3.)Run npm install express

4.)start the server by nodemon server.js




#dependencies and versions:
npm version:6.1.0
node version: 10.5.0




