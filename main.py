import requests
import streamlit as st

# Preparing the API
api_key = "wvcC8vMgjpsa0UGnM23RWvrqKmF7BK0IvYGRhuZK"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# getting the data
response1 = requests.get(url)
data = response1.json()

# extract the image title, url and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# image download
response2 = requests.get(image_url)
img_src = f"{title}.png"
with open(img_src, 'wb') as file:
    file.write(response2.content)

# adding a box for the image of the day and explanation
st.title(title)

st.write("")
st.image(img_src)
st.write("")

st.write(explanation)
