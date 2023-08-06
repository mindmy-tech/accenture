import deepface

# Load the DeepFace library
deepface.loadModel("models/facenet_keras.h5")

# Load the image of the person you want to identify
image = open("image.jpg", "rb").read()

# Identify the person in the image
face = deepface.detectFace(image)

# Get the face embedding
embedding = deepface.extractFaceEmbedding(image, face)

# Find the person with the closest face embedding
prediction = deepface.findSimilarFace(embedding, "dataset/")

# Print the name of the person
print(prediction["name"])