# fuzzysearch


## Step 1
- To create the dictionary pickle file run 
```
python prepare_dict.py input_csv_file word_dict.pickle
```
## Step 2
- Install all the requirements using
```
pip install -r requirements.txt
```

## Step 3 
- Run the server using 
```
python manage.py runserver
```

## Step 4
- Search for suggested words by calling the following url in your browser
```
http://localhost:8000/search/?word=practica
```
