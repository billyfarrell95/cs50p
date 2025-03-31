import sys, os
from PIL import Image, ImageOps

# todo: validation
# - validation message for incorrect output
# - different messages for input/output
# - Input does not exist message
def main():
    if len(sys.argv) == 3:
        shirt = sys.argv[1].strip()
        background = sys.argv[2].strip()
        if validate_file_types(shirt, background):
            create_image(shirt, background)
        else:
            print("File type error: Input and Output files types must match.")
            sys.exit()
    elif len(sys.argv) > 3:
        print("To many command-line arguments")
        sys.exit()
    else:
        print("To few command-line arguments")
        sys.exit()

def create_image(shirt, background):
    try:
        if not os.path.exists(shirt):
            print(f"Error: The file {shirt} does not exist.")
            sys.exit()
        if not os.path.exists(background):
            print(f"Error: The file {background} does not exist.")
            sys.exit()
        
        image1 = Image.open(shirt)
        image2 = Image.open(background)
        image2_resized = ImageOps.fit(image2, size=(300, 300))
        image1_resized = ImageOps.fit(image1, size=(300, 300))
        image2_resized.paste(image1_resized, (0, 0), image1_resized.convert('RGBA'))
        output_image_path = "output.png"
        image2_resized.save(output_image_path)
    except FileNotFoundError:
        print("File not found")

def validate_file_types(input, output):
    if input.endswith(".jpg") and output.endswith(".jpg"):
        return True
    elif input.endswith(".jpeg") and output.endswith(".jpeg"):
        return True
    elif input.endswith(".png") and output.endswith(".png"):
        return True
    else:
        return False

if __name__ == "__main__":
    main()