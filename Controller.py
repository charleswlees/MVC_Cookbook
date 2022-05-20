'''
Charlie Lees
This class is the Controller, interfaces between the Model and View in order to create the GUI functionality.
'''

from Model import Model
from View import View

class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View(self)

# functions which get data from the model as requested by the view
    def getRecipeNames(self):
        '''getRecipeNames - returns a comprehensive list of all recipes used
        '''
        # Returns a list of all recipe names
        return self.model.getColumn('Name')
    def getAllTags(self):
        '''getAllTags - returns a comprehensive list of all tags used
        '''
        # returns the tags for all recipes
        return self.model.tagList()
    def getRecipeProperty(self, property, recipeName):
        '''getRecipeProperty - Returns the specified property for a certain recipe
        Parameters - Property: string, The property in question to be retrieved
        recipeName: String, the name of the recipe we want to get the property for
        '''
        # calls specialized functoin to get Description, not just it's filepath
        if property == 'Description':
            return self.model.getDescription(recipeName)
        # calls specialized function to get Recipe, not just filepath
        elif property == 'Recipe':
            return self.model.getRecipe(recipeName)
        # for other properties, they can be accessed with our getProperty method
        else: 
            return self.model.getProperty(property, recipeName)    


# functions which call the view
    def applyFilters(self, tagName):
        '''applyFilters - filters the buttons in the view's homepage so that only the recipes for the desired
        category are displayed.
        Parameters: tagName - String, the category in question
        '''
        # calls the needed method in the view
        self.view.filterRecipes(tagName)
    def removeFilters(self):
        '''removeFilters - removes all applied filters to display all recipe buttons
        '''
        # calls the needed method in the view
        self.view.showAllRecipes()
    def closeRecipePage(self, recipePage):
        '''closeRecipePage - Manages the closing of the recipe page to re-enable all the functions of the homepage
        '''
        # calls the needed method of the view
        self.view.recipeClose(recipePage)
    def launchRecipePage(self, recipeName):
        '''launchRecipePage - launches the recipe page with the relevant information for the recipe.
        Also disables functions of the homepage while the recipe page is open.
        '''
        # calls needed method from the view
        self.view.recipePage(recipeName)
    def runApp(self):
        '''runApp - kicks off the program.
        '''
        # starts the view
        self.view.mainloop()


if __name__ == "__main__":
    # defining our controller
    controller = Controller()
    # starts application
    controller.runApp()
