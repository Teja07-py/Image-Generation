#Creating an Image generation model using hugging face reference

#The requests library is a popular HTTP library for making HTTP requests in Python.
#By importing post specifically, you can use it to send HTTP POST requests to web servers.
#This allows you to send data to a specified URL and retrieve the response from the server.
from requests import post

#Importing Image module from Python Image Library-(PIL) enables us to perform tasks
#such as opening images, applying transformations, resizing, cropping, and saving images in various formats
from PIL import Image

#From io module ,a class called BytesIO offers an interface for binary data stored in memory for binary streams.
#When working with image processing or file modification, this may be quite helpful.
from io import BytesIO

# The post function takes parameters such as the URL to which the request is sent,
# data to be sent in the request body, headers, and other paramteres.
b =post(
    "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1",
    headers={"Authorization": "Bearer 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"},

    # Describing the image to be generated
    json={"inputs":input()}
)

i= Image.open(BytesIO(b.content))

#Saving the generated image in .png format

i.save("img45.png")
