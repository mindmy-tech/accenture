from deepface import DeepFace
import os
cwd=os.getcwd()
cwd=cwd.removesuffix('pragram.py')
# Path to the image containing known faces (reference image)
reference_image_path = rf"{cwd}\accenture\Dataset\WhatsApp Image 2023-08-06 at 8.00.48 PM.jpeg"

directory_list = os.listdir(rf"{cwd}\accenture\Dataset\mokith")
for path in directory_list:
    # Path to the image you want to recognize (target image)
    target_image_path = rf"{cwd}\accenture\Dataset\mokith\{path}"
    # Perform face recognition
    result = DeepFace.verify(reference_image_path, target_image_path, enforce_detection = False)

# Print the result
    if result["verified"]:
        pass
       # print("The target image contains the same person as the reference image.")
       # print("Facial distance:", result["distance"])
    else:
        os.remove(target_image_path)
       # print("The target image does not contain the same person as the reference image.")
       # print("Facial distance:", result["distance"])
