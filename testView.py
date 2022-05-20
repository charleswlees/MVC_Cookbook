'''
Charlie Lees
CS 5001 Final Project
This file will be testing the GUI created by the View

Both of these tests are visual, they will launch the live version of a page along with an image
displaying what it should look like.
'''


from Controller import Controller
from tkinter import *

# Tests the view of the homepage
def test_homepage(controller):
    # Creates a new window that will contian the image for the recipe page
    testWindow = Toplevel(controller.view)
    # image contianing what the recipe page should look like
    testWindow.title('Homepage Test Image')
    imageLabel = Label(testWindow)
    image2 = PhotoImage(file = 'test_image1.png')
    imageLabel.config(image = image2)
    # showing homepage
    imageLabel.pack()
    testWindow.mainloop()

# creates the view of the recipe page
def test_recipePage(controller):
    # Creates a new window that will contain the image for the recipe page
    testWindow = Toplevel(controller.view)
    # image contianing what the recipe page should look like
    testWindow.title('RecipePage Test Image')
    # Creating and packing a label for the image
    imageLabel = Label(testWindow)
    image2 = PhotoImage(file = 'test_image2.png')
    imageLabel.config(image = image2)
    imageLabel.pack()
    # showing the recipe page
    controller.view.recipePage('Meatloaf')
    testWindow.mainloop()

if __name__ == '__main__':
    testController = Controller()

    '''
    Below are the code for the tests, as each one creates new windows, it would be cumbersome to run them all. 
    Uncomment and run the test in particular that you wish to see.
    '''
    # test_recipePage(testController)
    # test_homepage(testController)

