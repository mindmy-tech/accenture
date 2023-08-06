from deepface import DeepFace

# Path to the image containing known faces (reference image)
reference_image_path = "path_to_reference_image.jpg"

# Path to the image you want to recognize (target image)
target_image_path = "path_to_target_image.jpg"

# Perform face recognition
result = DeepFace.verify(reference_image_path, target_image_path)

# Print the result
if result["verified"]:
    print("The target image contains the same person as the reference image.")
    print("Facial distance:", result["distance"])
else:
    print("The target image does not contain the same person as the reference image.")
    print("Facial distance:", result["distance"])
