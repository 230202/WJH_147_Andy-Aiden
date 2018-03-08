import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def custom(original_image, color,frame_width):
    """ THis first function, custom is meant to create the mask that I set on each image. I added 4 rectangles for a frame and two triangles in the opposite corners
    to add on to the frame. Then i colored everything to make it look nice using the fill command. After this, I pasted in 3 different images, my logo, my slogan , and 
    the picture of my classmates face. AKA the client. 
    """
    #set the radius of the rounded corners
    width, height = original_image.size # setting the width and height to the images size. length and width are now an integer value
    thickness = int(frame_width * min(width, height)) # thickness in pixels
    
    
    #create a mask
    
    
    #start with transparent mask
    r,g,b = color
    framed_mask = PIL.Image.new('RGBA', (width, height), (0,0,0,0))
    drawing_layer = PIL.ImageDraw.Draw(framed_mask)
    
    drawing_layer.rectangle((0,0,width,thickness), fill=(50,50,50,255))# creating top rectangle for picture frame
    drawing_layer.rectangle((0,0,thickness, height), fill=(105,105,105,255))# creating left rectangle for picture frame
    drawing_layer.rectangle((width,height,width-thickness,0), fill=(105,105,105,255))# creating right rectangle for picture frame
    drawing_layer.rectangle((0, height , width,height - thickness), fill=(50,50,50,255)) # creating bottom rectangle for picture frame
    
    drawing_layer.polygon([(thickness,thickness,),(height * 1/5,thickness),(thickness, width * 1/5)], fill=(25,25,25,255))
    #Line above created a triangle in the top left corner - one of our 2 geometry figures we added 
    drawing_layer.polygon([(width-thickness,height-thickness),(width - thickness, height*4/5 - thickness),(width*11/12-thickness, height - thickness)], fill=(25,25,25,255))
    #line above created a triangle in the bottom right corner - our other geometry figure we added
    
    ''' first paste section'''
    
    result = original_image.copy()#setting result to our main image
    directory = os.path.dirname(os.path.abspath(__file__))#setting the variable directory equal to our actual working directory
    charan_file = os.path.join(directory, 'Charan.png')# calling the image file of charan to join with the directory - to be re named charan_file
    charan_final = PIL.Image.open(charan_file)# opening charan file as a PIL Image
    charan_finals = charan_final.resize((int(width*.4), int(height*.4)))# resizing the charan.png image - 40 percent main image size
    result.paste(charan_finals, (int(width*5/10),int(height*5/10)), mask=charan_finals)#using the paste method to place charan image on top of main image
    ''' second paste section - inline comments are the same as the first paste section so look to those to see what the code does'''
    disaster_file= os.path.join(directory, 'DisasterGuys.png')
    Disaster_Guy = PIL.Image.open(disaster_file)
    Disaster_Final = Disaster_Guy.resize((int(width*.4), int(height*.4)))
    result.paste(Disaster_Final, (int(width/20), int(height*6/10)), mask=Disaster_Final)
    ''' third paste section - inline comments are the same as the first paste section so look to those to see what the code does'''
    Slogan_File = os.path.join(directory, 'Slogan.png')
    Slogan_name = PIL.Image.open(Slogan_File)
    Slogan_Final = Slogan_name.resize((int(width*.8), int(height*.2)))
    result.paste(Slogan_Final, (int(width/7), int(height/10)), mask=Slogan_Final)
    
    result.paste(framed_mask, (0,0), mask=framed_mask)#pasting the frame on the mask
    
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    

def custom_all_images(directory=None, color=(255,255,100), frame_width=.1):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'custom images'
    new_directory = os.path.join(directory, 'custom_images')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print n
        filename, filetype = file_list[n].split('.')
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = custom(image_list[n],color,frame_width) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)