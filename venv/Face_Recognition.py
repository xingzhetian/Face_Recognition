import face_recognition
import os
import cv2

known_dir="known_faces"
unknown_dir="unknown_faces"
toleance=0.8          #funtine the model: the lower, the strict
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL='cnn'

# Returns (R, G, B) from name
def name_to_color(name):
    # Take 3 first letters, tolower()
    # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color

print('Loading known faces...')
known_faces = []
known_names = []

#loading images
for name in os.listdir(known_dir):

    # Next we load every file of faces of known person
    for filename in os.listdir(f'{known_dir}/{name}'):

        # Load an image
        image = face_recognition.load_image_file(f'{known_dir}/{name}/{filename}')

        # Get 128-dimension face encoding
        # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
        encoding = face_recognition.face_encodings(image)[0]

        # Append encodings and name
        known_faces.append(encoding)
        known_names.append(name)

print('Processing unknown faces...')
# Now let's loop over a folder of faces we want to label
for filename in os.listdir(unknown_dir):

    # Load image
    print(f'Filename {filename}', end='')
    image = face_recognition.load_image_file(f'{unknown_dir}/{filename}')

    locations = face_recognition.face_locations(image, model=MODEL)

    encodings = face_recognition.face_encodings(image, locations)

    #cover RGB to GBR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    print(f', found {len(encodings)} face(s)')
    for face_encoding, face_location in zip(encodings, locations):
        # We use compare_faces (but might use face_distance as well)
        # Returns array of True/False values in order of passed known_faces
        results = face_recognition.compare_faces(known_faces, face_encoding, toleance)

    match=None
    if True in results:  # If at least one is true, get a name of first of found labels
        match = known_names[results.index(True)]
        print(f' - {match} from {results}')

        # Each location contains positions in order: top, right, bottom, left
        top_left = (face_location[3], face_location[0])
        bottom_right = (face_location[1], face_location[2])

        # Get color by name using our fancy function
        color = name_to_color(match)

        # Paint frame
        cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

        # Now we need smaller, filled grame below for a name
        # This time we use bottom in both corners - to start from bottom and move 50 pixels down
        top_left = (face_location[3], face_location[2])
        bottom_right = (face_location[1], face_location[2] + 22)

        # Paint frame
        cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

        # Wite a name
        cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (200, 200, 200), FONT_THICKNESS)

        # Show image
    cv2.imshow(filename, image)
    cv2.waitKey(100000)
    #cv2.destroyWindow(filename)



