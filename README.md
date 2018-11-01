# Serving Fastai Models

The aim of this project was to develop a minimal Django webapp that will allow you to serve a fastai model. There are currently three ways to submit an image:

- From the "webapp"
- Via an API request
- Through a telegram chatbot

## Get started

Install dependencies using conda environment:

```sh
conda create --name "myEnv" python=3.6 --file package-list.txt
conda activate myEnv
```

Then run the webapp:

```sh
python manage.py runserver
```

## Structure

Put trained `.pth` models in `models/models`

Put dummy categories into `models/train` and `models/validate`. Test is not required.

Create `tmp` directory to store uploaded photos.

In the `webhook` directory, add your telegram chatbot's token.

## Querying the Chatbot

Sending an image to the chatbot will automatically add the image to a queue to be classified.