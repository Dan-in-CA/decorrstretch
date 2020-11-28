# decorrstretch
Decorrelation stretch in Python  
  
Decorrelation stretching enhances the color separation of an image.  
It produces exaggerated colors which can improve visual interpretation  
  
This fork of lbrabec/decorrstretch has been updated to run under Python3.  
  
A commmand line utility named **process_image.py** has been added to make using ds.py easy.  
  
**Python Pillow**, the Python Imaging Library, is **required**. It can be installed with:  
`pip3 install Pillow` 
  
To use process_image:  
from the decorrstretch folder run    
`python3 process_image.py`

Enter the name or path of the image file to process.  
Enter a name or path + name of the output file to be saved.  
Optionally enter a value for a linear stretch, e.g. 0.01,  

The input and output file types can be different and most common file formats such as jpeg, png, etc. should work.
