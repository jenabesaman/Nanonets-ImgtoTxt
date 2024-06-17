# import requests
# import json
#
# url = 'https://app.nanonets.com/api/v2/OCR/Model/f1db07e3-d99a-4d5d-b8e6-7b878a8287fe/LabelFile/'
#
# data = {'file': open('C:/Workarea/several-text-projects/melli.jpg', 'rb')}
#
# response = requests.post(url, auth=requests.auth.HTTPBasicAuth('4f372524-2cc5-11ef-b749-1ea4552a8b53', ''), files=data)
#
# # Parse the JSON response
# response_json = json.loads(response.text)
#
# # Extract the predictions from the response
# predictions = response_json['result'][0]['prediction']
#
# # Print the extracted text from each prediction
# for prediction in predictions:
#     text = prediction['ocr_text']
#     # Remove the replacement characters
#     text = text.replace('�', '')
#     print(text)



# import requests
# import cv2
# import numpy as np
# import json
# import matplotlib.pyplot as plt
#
# # The API endpoint with the default OCR model ID
# url = 'https://app.nanonets.com/api/v2/OCR/Model/f1db07e3-d99a-4d5d-b8e6-7b878a8287fe/LabelFile/'
#
# # The path to your image file
# image_path = 'C:/Workarea/several-text-projects/melli.jpg'
#
# # Read the image
# img = cv2.imread(image_path)
#
# # Convert the image to grayscale
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Increase the contrast of the image by increasing the pixel values
# contrast_img = cv2.convertScaleAbs(img, alpha=1, beta=0)
#
# # Display the preprocessed image
# # plt.imshow(contrast_img, cmap='gray')
# plt.imshow(cv2.cvtColor(contrast_img, cv2.COLOR_BGR2RGB))
# plt.show()
#
# # Save the preprocessed image
# cv2.imwrite('preprocessed_image.jpg', contrast_img)
#
# # Open the preprocessed image in binary mode
# with open('preprocessed_image.jpg', 'rb') as f:
#     # The data for the API request
#     data = {
#         'file': f
#     }
#
#     # Make the POST request and get the response
#     response = requests.post(url, auth=requests.auth.HTTPBasicAuth('4f372524-2cc5-11ef-b749-1ea4552a8b53', ''), files=data)
#
# # Parse the JSON response
# response_json = json.loads(response.text)
#
# # Extract the predictions from the response
# predictions = response_json['result'][0]['prediction']
#
# # Print the extracted text from each prediction
# for prediction in predictions:
#     text = prediction['ocr_text']
#     # Remove the replacement characters
#     text = text.replace('�', '')
#     print(text)


import requests
import cv2
import numpy as np
import json
import matplotlib.pyplot as plt

url = 'https://app.nanonets.com/api/v2/OCR/Model/f1db07e3-d99a-4d5d-b8e6-7b878a8287fe/LabelFile/'

image_path = 'C:/Workarea/several-text-projects/melli.jpg'
img = cv2.imread(image_path)

cv2.imwrite('preprocessed_image.png', img)

with open('preprocessed_image.png', 'rb') as f:
    data = {'file': f}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('4f372524-2cc5-11ef-b749-1ea4552a8b53', ''),
                             files=data)

response_json = json.loads(response.text)
predictions = response_json['result'][0]['prediction']

for prediction in predictions:
    text = prediction['ocr_text']
    text = text.replace('�', '')
    print(text)
