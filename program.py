from deepface import DeepFace
import os
cwd=os.getcwd()
cwd=cwd.removesuffix('pragram.py')
folders=['000','001','002','003','004','005']
for folder in folders:
    # Path to the image containing known faces (reference image)
    reference_image_path = rf"{cwd}\accenture\Dataset\{folder}.jpeg"

    directory_list = os.listdir(rf"{cwd}\accenture\Dataset\mokith\All images")
    no_of_files = 0
    no_of_verified = 0
    for path in directory_list:
        no_of_files += 1
        # Path to the image you want to recognize (target image)
        target_image_path = rf"{cwd}\accenture\Dataset\mokith\{folder}\valid\{path}"
        # Perform face recognition
        result = DeepFace.verify(reference_image_path, target_image_path, enforce_detection = False)

    # Print the result
        if result["verified"]:
            no_of_verified += 1
            os.remove(rf"{cwd}\accenture\Dataset\mokith\{folder}\invalid\{path}")
        # print("The target image contains the same person as the reference image.")
        # print("Facial distance:", result["distance"])
        else:
            os.remove(target_image_path)
            #print("The target image does not contain the same person as the reference image.")
            #print("Facial distance:", result["distance"])
    print(no_of_verified,'are matched, out of 241 files in',folder,'folder')