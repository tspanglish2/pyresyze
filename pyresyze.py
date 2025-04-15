#!/usr/bin/env python3
import os
import argparse
from PIL import Image, ExifTags

def resize_image(input_path, output_path, scale_factor=0.5):
    """
    Resizes an image by a given scale factor while preserving EXIF metadata.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path where the resized image will be saved
        scale_factor (float): Factor by which to reduce the image size (0.5 = half size)
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Get original dimensions
        width, height = img.size
        
        # Calculate new dimensions
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        
        # Extract EXIF data before resizing
        exif_data = None
        if 'exif' in img.info:
            exif_data = img.info['exif']
        
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Save the resized image with original EXIF data
        if exif_data:
            resized_img.save(output_path, exif=exif_data)
        else:
            resized_img.save(output_path)
        
        print(f"Successfully resized {input_path} from {width}x{height} to {new_width}x{new_height}")
        
    except Exception as e:
        print(f"Error resizing {input_path}: {e}")

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Resize images to reduce their resolution')
    parser.add_argument('input', help='Input image file or directory containing images')
    parser.add_argument('-o', '--output', help='Output directory or file (if input is a single file)')
    parser.add_argument('-s', '--scale', type=float, default=0.5, 
                       help='Scale factor (0.5 = half size, 0.25 = quarter size, etc.)')
    parser.add_argument('-r', '--recursive', action='store_true', 
                       help='Process directories recursively')
    
    args = parser.parse_args()
    
    # Check if input is a file or directory
    if os.path.isfile(args.input):
        # For a single file
        if args.output:
            output_path = args.output
        else:
            # Create output filename by adding '_resized' before the extension
            basename, ext = os.path.splitext(args.input)
            output_path = f"{basename}_resized{ext}"
        
        resize_image(args.input, output_path, args.scale)
    
    elif os.path.isdir(args.input):
        # For a directory of images
        if not args.output:
            # Default output directory is input_resized
            args.output = f"{args.input}_resized"
        
        # Create output directory if it doesn't exist
        os.makedirs(args.output, exist_ok=True)
        
        # Process all files in directory
        for root, dirs, files in os.walk(args.input):
            # Skip processing subdirectories if not recursive
            if root != args.input and not args.recursive:
                continue
            
            for file in files:
                # Check if file is an image (basic extension check)
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                    input_path = os.path.join(root, file)
                    
                    # Create relative path for output
                    rel_path = os.path.relpath(root, args.input)
                    if rel_path == '.':
                        rel_path = ''
                    
                    # Create output subdirectory if needed
                    if rel_path:
                        output_subdir = os.path.join(args.output, rel_path)
                        os.makedirs(output_subdir, exist_ok=True)
                        output_path = os.path.join(output_subdir, file)
                    else:
                        output_path = os.path.join(args.output, file)
                    
                    resize_image(input_path, output_path, args.scale)
    
    else:
        print(f"Error: {args.input} is not a valid file or directory")

if __name__ == "__main__":
    main()
