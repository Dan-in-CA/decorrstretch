
from PIL import Image
import numpy as np
from ds import decorrstretch

# get imput from user.
infile = input("Enter file to process:")
outfile = input("Enter output file:")
tol_val = input("Enter tol value (optional):")

# If a value is given, convert to float.
if tol_val:
    tol = float(tol_val)
else:
    tol = None

print("Processing ...")

# Load input file using PIL.
img = Image.open(infile)
# Convert image to numpy array.
A = np.array(img)
# process image.
processed = decorrstretch(A, tol)
# Save processed image to output file.
Image.fromarray(processed).save(outfile)

print("Done")
