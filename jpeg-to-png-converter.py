import os
from PIL import Image

def convert_to_png(input_path):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Check if the image is already in PNG format
            if img.format == 'PNG':
                print(f"The image {input_path} is already in PNG format.")
                return input_path
            
            # If it's a JPEG, convert to PNG
            if img.format == 'JPEG':
                # Create the output filename
                output_path = os.path.splitext(input_path)[0] + '.png'
                
                # Convert and save as PNG
                img.save(output_path, 'PNG')
                print(f"Successfully converted {input_path} to {output_path}")
                return output_path
            
            # If it's neither PNG nor JPEG
            print(f"The file {input_path} is neither PNG nor JPEG. No conversion performed.")
            return input_path

    except Exception as e:
        print(f"An error occurred while processing {input_path}: {str(e)}")
        return None

def main():
    print("JPEG to PNG Converter")
    
    # Get input file path
    input_path = input("Enter the path to the image file: ")
    
    # Check if file exists
    if not os.path.exists(input_path):
        print("File does not exist. Please provide a valid file path.")
        return
    
    # Perform conversion
    result = convert_to_png(input_path)
    
    if result:
        print("Process completed.")
    else:
        print("Conversion failed.")

if __name__ == "__main__":
    main()
