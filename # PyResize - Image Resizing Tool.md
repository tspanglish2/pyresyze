# PyResize - Image Resizing Tool

A simple Python utility that resizes images while preserving EXIF metadata. Supports both single files and batch processing of directories.

## Features

- Resize individual images or entire directories
- Preserve EXIF metadata during resizing
- Support for recursive directory processing
- Adjustable scale factor
- Supports common image formats (PNG, JPG, JPEG, BMP, GIF, TIFF)
- Maintains directory structure in batch processing

## Requirements

- Python 3.x
- Pillow (PIL) library

Install required dependency:
```bash
pip install Pillow
```

## Usage

```bash
python pyresyze.py input [-o OUTPUT] [-s SCALE] [-r]
```

### Arguments

- `input`: Path to input image file or directory
- `-o, --output`: Output directory/file path (optional)
- `-s, --scale`: Scale factor (default: 0.5)
- `-r, --recursive`: Enable recursive directory processing

### Examples

1. Resize single image:
```bash
python pyresyze.py photo.jpg
```

2. Resize with custom scale:
```bash
python pyresyze.py photo.jpg -s 0.75 -o resized_photo.jpg
```

3. Process directory:
```bash
python pyresyze.py photos/ -o resized_photos/
```

4. Process directory recursively:
```bash
python pyresyze.py photos/ -r -o resized_photos/
```

## Output

- Single file mode: Adds "_resized" suffix if no output specified
- Directory mode: Creates "*_resized" directory if no output specified
- Preserves original directory structure in recursive mode
