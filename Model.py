'''
Charlie Lees
CS 5001 Final Project
This class is the Model, it holds and organizes the data which is going to be used in the GUI
'''

import pandas as pd

class Model:
    def __init__(self):
        self.binder = self._readData()

# feeds information to the Controller
    def getColumn(self, attribute):
        '''getColumn - Returns all of the different values for a sertain attribute
        Parameters - Attribute: String, the attribute in question
        '''
        # returns a column of the dataframe of a certain attribute
        value = ""
        # retrieves the column in question, throws error if attribute is not correct
        try:
            value = self.binder[attribute]
        except KeyError as ex:
            print('Entered Attribute is not a valid attribute', type(ex), ex)
            return 0
        return value
    def getProperty(self, attribute, recipeName):
        '''getProperty - Returns a certain property from a certain recipe.
        Parameters - Attribute: String, the attribute in question
        recipeName: String, the recipe in question
        '''
        # returns a specific item from the dataframe for a particular recipe
        desiredAttribute = ''
        # Tries to retrieve the attribute from the recipe in question, throws errors as needed
        try:
            recipeRow = self.binder[(self.binder['Name'] == recipeName)]
            if attribute == 'Tags':
                desiredAttribute = recipeRow['Tags'].item().split()
            else: 
                desiredAttribute = recipeRow[attribute].item()
        except KeyError as ex:
            print('Entered Attribute/Recipe is not valid', type(ex), ex)
            return 0
        return desiredAttribute
    def tagList(self):
        '''tagList - returns a comprehensive list of all tags used for recipes
        '''
        # create a comprehensive list of all tags in the data frame
        # no duplicates
        tags = self.binder['Tags']
        list = []
        for i in range(len(tags)):
            newList = tags[i].split()
            for k in range(len(newList)):
                if newList[k] not in list:
                    list.append(newList[k])
        return list
    def nameList(self):
        '''nameList - returns a comprehensive list of all names used for recipes
        '''
        # creates a list of all names in the dataframe
        names = self.binder['Name']
        list = []
        for i in range(len(names)):
            if names[i] not in list:
                list.append(names[i])
        return list
    def getDescription(self, recipeName):
        '''getDescription - returns the full description of a given recipe from it's text file
        Parameters - recipeName: String, the name of the desired recipe
        '''
        # returns the full description for a given recipe
        fullDesc = ''
        try:
            recipeRow = self.binder[(self.binder['Name'] == recipeName)]
            descLocation = recipeRow['Description'].item()
            input = open(descLocation)
            fullDesc = "".join(input.readlines())
        except ValueError as ex:
            print('Entered Recipe name is not valid', type(ex), ex)
            return 0
        return fullDesc      
    def getRecipe(self, recipeName):
        '''getRecipe - returns the full recipe of a given recipe from it's text file
        Parameters - recipeName: String, the name of the desired recipe
        '''
        # returns the full guide for a given recipe
        fullRecipe = ''
        try:
            recipeRow = self.binder[(self.binder['Name'] == recipeName)]
            recipeLocation = recipeRow['Recipe'].item()
            input = open(recipeLocation)
            fullRecipe = "".join(input.readlines())
        except ValueError as ex:
            print('Entered Recipe name is not valid', type(ex), ex)
            return 0
        return fullRecipe

# populates model
    def _readData(self):
        '''readData - Populates the Model's dataframe with the textfiles in the program's folder.        
        '''
        # reads in information from text files and creates a DataFrame to contain it
        # read in recipe names
        input = open('_names.txt')
        namesList = input.readlines()
        input.close()
        for i in range(len(namesList)):
            namesList[i] = namesList[i].strip('\n')

        # read in recipe descriptions
        input = open('_descPlaces.txt')
        descList = input.readlines()
        input.close

        for i in range(len(descList)):
            descList[i] = descList[i].strip('\n')

        # read in recipe descriptions
        input = open('_recipePlaces.txt')
        recipeList = input.readlines()
        input.close
        for i in range(len(recipeList)):
            recipeList[i] = recipeList[i].strip('\n')

        # read in recipe descriptions
        input = open('_tags.txt')
        tagList = input.readlines()
        input.close
        for i in range(len(tagList)):
            tagList[i] = tagList[i].strip('\n')

        # read in button icons
        input = open('_buttonIcons.txt')
        iconList = input.readlines()
        input.close
        for i in range(len(iconList)):
            iconList[i] = iconList[i].strip('\n')
        
        # read in all recipe headers
        input = open('_headers.txt')
        headerList = input.readlines()
        input.close
        for i in range(len(headerList)):
            headerList[i] = headerList[i].strip('\n')


        # creates dictionary with all values
        dic = {'Name': namesList, 'Description' : descList, 'Recipe': recipeList, 'Tags' : tagList, 'Icons': iconList, 'Headers': headerList}
        df = pd.DataFrame(dic)
        return df

if __name__ == "__main__":
    # This is test code which will print out the dataframe in the console
    # IMPORTANT POINT: if the DataFrame is larger than your console window, it will not fully display. 
    # those fields are not missing but just off screen.
    test = Model()
    print(test.binder)