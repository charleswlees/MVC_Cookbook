'''
Charlie Lees
CS 5001 Final Project
This class contains the information for the View, the visual elements of the GUI itself.
'''


from tkinter import *
from tkinter import ttk
from tkinter.font import Font



class View(Tk):
# Creating our homepage
    def __init__(self, controller):
        # Inherits from Tkinter
        super().__init__()
        self.controller = controller
        self.title('Cookbook')

        # Defines window size and prevents resizing.
        self.geometry('1280x720+50+50')
        self.resizable(FALSE,FALSE)

        
        # defines the background image for the homepage itself
        background = PhotoImage(file = "Cookbook_Background3.png")
        backgroundLabel = ttk.Label(self)
        backgroundLabel.img = background
        backgroundLabel.config(image = backgroundLabel.img)
        backgroundLabel.place(x = 0, y = 0, height = 720, width = 1280)
        
               
        # Creates label for the recipe buttons
        recipeLabel = Label(self, text = 'Recipes: ', borderwidth = 0, highlightthickness = 0)
        recipeLabelIcon = PhotoImage(file = 'title_Recipes.png')
        recipeLabel.img = recipeLabelIcon
        recipeLabel.config(image = recipeLabel.img)
        recipeLabel.place(x=30, y=20)
        

        # Creates frame that will house the recipe buttons
        buttonFrame = Frame(self, height = 550, width = 300, relief = GROOVE, background = "#DEEBF7")
        buttonFrame.pack_propagate(FALSE)
        self.buttonFrame = buttonFrame
        buttonFrame.place(x = 30, y = 150)
        
        # generates the buttons and packs them into the specified frame
        buttonList = self.generateButtons()
        self.buttonList = buttonList   

        # creates a label for the tags
        tagLabel = Label(self, text = 'Categories: ', borderwidth = 0, highlightthickness = 0)
        tagIcon = PhotoImage(file = 'title_Categories.png')
        tagLabel.img = tagIcon
        tagLabel.config(image = tagLabel.img)
        tagLabel.place(x=875, y = 20)

        # Creates frame that will house the tag buttons
        tagFrame = Frame(self, height = 550, width = 245, relief = GROOVE, background = "#DEEBF7")
        tagFrame.pack_propagate(FALSE)
        self.tagFrame = tagFrame
        tagFrame.place(x = 925, y = 150)
        
        # generates the buttons for each recipe tag and packs them into their frame
        tagButtonList = self.generateTagButtons()
        self.tagButtonList = tagButtonList

# Creating Buttons
    def generateTagButtons(self):
        '''generateTagButtons - generates a list of buttons which will filter the recipes based on their category
        '''
        
        # creates a font for these buttons to use
        tagButtonFont = Font(family = 'Calibri', size = 11, weight = 'bold', underline = True)
        
        # creates and packs a button to show all recipes
        showAllButton = Button(self.tagFrame, text = 'Show All', background='black', foreground = 'white', command = lambda: self.controller.removeFilters())
        
        # allows it to change color when hovering over it with a mouse
        showAllButton.bind('<Enter>', func = lambda e:  showAllButton.config(background = 'grey'))
        showAllButton.bind('<Leave>', func = lambda e: showAllButton.config(background = 'black'))
        showAllButton.pack(pady = 8)

        # a comprehensive list of tags that are used across all recipes
        tagList = self.controller.getAllTags()

        # create buttons for each tag

        # list of tag buttons
        buttonList = []
        for i in range(len(tagList)):
            currentTag = tagList[i]
            # Makes the frame which has the blue outline for each button
            currentFrame = Frame(self.tagFrame, highlightbackground = '#2E75B6', highlightthickness=3, bd = 0)
            currentButton = Button(currentFrame, text = currentTag, command = lambda currentTag = currentTag: self.controller.applyFilters(currentTag))
            currentButton.config(font = tagButtonFont, fg = '#2E75B6', bg = '#DEEBF7', relief = FLAT)
            currentButton.pack()
            buttonList.append(currentFrame)
        
        for i in range(len(buttonList)):
            buttonList[i].pack(pady = 5)
        return buttonList

    def generateButtons(self):
        '''generateButtons - Returns a list of recipe buttons which will launch a recipe page for the specified recipe
        '''
        # creates empty list which will house our buttons
        nameList = self.controller.getRecipeNames()
        buttonList = []
        for i in range(len(nameList)):
            recipeName = nameList[i]
            currentIconPath = self.controller.getRecipeProperty('Icons', recipeName)
            currentIcon = PhotoImage(file = currentIconPath)
            currentButton = Button(self.buttonFrame, text = recipeName, command = lambda currentRecipe = recipeName :self.controller.launchRecipePage(currentRecipe))
            currentButton.img = currentIcon
            currentButton.config(image = currentButton.img, width = 480, borderwidth = 0, highlightthickness = 0)
            buttonList.append(currentButton)
        
        for i in range(len(buttonList)):
            buttonList[i].pack(anchor = 'w', pady = 7)
        return buttonList

# Button Actions
    def recipePage(self, recipeName):
        '''recipePage - launches a recipe page for the given recipe
        Parameters - recipeName: String, the name of the recipe in question
        '''
        # creates and displays a recipe page for a recipe item.
        recipeWindow = Toplevel(self)
        recipeWindow.title(f'{recipeName} Recipe')
        recipeWindow.resizable(FALSE, FALSE)
        recipeWindow.geometry('1280x720+50+50')
        recipeWindow.lift()

        

        recipeBackground = PhotoImage(file = "Cookbook_Background3.png")
        recipeBackgroundLabel = ttk.Label(recipeWindow)
        recipeBackgroundLabel.img = recipeBackground
        recipeBackgroundLabel.config(image = recipeBackgroundLabel.img)
        recipeBackgroundLabel.place(x = 0, y = 0, height = 720, width = 1280)

        # back button to go back to the regular 
        backButton = Button(recipeWindow, text = 'Back', foreground = 'white', width = 10, background = 'black', command = lambda: self.controller.closeRecipePage(recipeWindow))
        backButton.bind('<Enter>', func = lambda e:  backButton.config(background = 'grey'))
        backButton.bind('<Leave>', func = lambda e: backButton.config(background = 'black'))
        backButton.place(x=20, y=20)

        
        # recipe information on the page
        # Displays name information
        recipeHeader = self.controller.getRecipeProperty('Headers', recipeName)
        recipeHeaderImage = PhotoImage(file = recipeHeader)
        nameLabel = Label(recipeWindow,text = f'Recipe Name: {recipeName}' , background= '#DEEBF7')
        nameLabel.img = recipeHeaderImage
        nameLabel.config(image = nameLabel.img)
        nameLabel.place(x=400, y=20)



        # Displays Description Information
        descriptionFrame = LabelFrame(recipeWindow, text = 'Description')
        recipeDescription = self.controller.getRecipeProperty('Description', recipeName)
        descriptionLabel = ttk.Label(descriptionFrame, text = recipeDescription)
        descriptionLabel.pack()
        descriptionFrame.place(x=75, y=200)

        # Displays step by step Recipe Information
        stepsFrame = LabelFrame(recipeWindow, text = "Ingredients")
        recipeSteps = self.controller.getRecipeProperty('Recipe', recipeName)
        stepsLabel = ttk.Label(stepsFrame, text = recipeSteps)
        stepsLabel.pack()
        stepsFrame.place(x=600, y=200)
        
        # Displays the tags for the recipe in question

        tagsFrame = LabelFrame(recipeWindow, text = 'Categories')
        tagsList = self.controller.getRecipeProperty('Tags', recipeName)
        tagsLabel = ttk.Label(tagsFrame, text = ', '.join(tagsList))
        tagsLabel.pack()
        tagsFrame.place(x=1000, y = 20)
        # When opening a recipe window, all other recipe buttons will be disabled. 
        # Prevents user from opening a million different recipes at the same time.
        for i in self.buttonFrame.winfo_children():
            i.configure(state = 'disabled')
        # prevents user from using filter buttons while in a recipe
        for i in self.tagFrame.winfo_children():
            for k in i.winfo_children():
                k.configure(state = 'disabled')
        recipeWindow.protocol('WM_DELETE_WINDOW', lambda: self.controller.closeRecipePage(recipeWindow))

    def filterRecipes(self, desiredTag):
        '''filterRecipes - removes recipeButtons that do not apply to the desired Recipe and/or 
        re-adds buttons that do apply that were removed
        Parameters - desiredTag: String, the desired category
        '''
        # step 1. Create list of recipes that fit in our tags
        # Step 2 a. hide all buttons that aren't for those recipes 
        # Step 2 b. show all buttons that are for those recipes
        # Stores the recipe names that have the tag in question
        goodRecipes = []
        recipeList = self.controller.getRecipeNames()

        for i in range(len(recipeList)):
            currentRecipeName = recipeList[i]
            currentRecipeTags = self.controller.getRecipeProperty('Tags', currentRecipeName)
            match = FALSE
            for k in range(len(currentRecipeTags)):
                currentTag = currentRecipeTags[k]
                if currentTag == desiredTag:
                    match = TRUE
            if match == TRUE:
                goodRecipes.append(currentRecipeName)

        for i in range(len(self.buttonList)):
            currentButton = self.buttonList[i]
            currentButtonName = currentButton['text']
            match = FALSE
            for k in range(len(goodRecipes)):
                if currentButtonName == goodRecipes[k]:
                    match = TRUE
            if match == TRUE:
                currentButton.pack(anchor = 'w', pady = 7)
            elif match == FALSE:
                currentButton.pack_forget()

    def showAllRecipes(self):
        '''showAllRecipes - restores all recipe buttons
        '''
        # makes all recipe buttons visable
        buttons = self.buttonFrame.winfo_children()
        for i in buttons:
            i.pack(anchor = 'w', pady = 7)    
        
    def recipeClose(self, window):
        '''recipeClose - Restores functionality to the homepage after closing a recipe window
        Parameters - window: Window Object from TKinter.
        '''
        # This function defines what happens when we close a recipe screen
        # We want to close the window and re-enable the recipe buttons back on the navigation screen.
        # re-enables recipe buttons
        for i in self.buttonFrame.winfo_children():
            i.configure(state = 'normal')
        # re-enables filter buttons
        for i in self.tagFrame.winfo_children():
            for k in i.winfo_children():
                k.configure(state = 'normal')
        window.destroy()