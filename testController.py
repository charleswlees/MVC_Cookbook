'''
Charlie Lees
This file will be a test for the Controller class in this project.

As the controller is going calling methods from the Model, I will be 
importing some of those tests as needed. 

I will be testing the functions of the Controller class with both good and bad
input

'''

from Controller import Controller
from testModel import *
from tkinter import *

# functions that call the Model

# tests for the methods with no input
def test_getRecipeNames(controller):
    # calls the relevant test from our model tests
    return test_nameList(controller.model)

def test_getAllTags(controller):
    # calls the relevant test from our model tests
    return test_tagList(controller.model)

# methods that take in input
def test_valid_getRecipeProperty(controller):
    # tests getting the description
    desc = test_valid_getDescription(controller.model)
    # tests getting the recipe
    recipe = test_valid_getRecipe(controller.model)
    # tests getting a different recipe
    other = test_valid_getProperty(controller.model)

    # verifies that the tests ran successfully
    if desc == 1 and recipe == 1 and other == 1:
        return 1
    else:
        return 0

def test_bad_getRecipeProperty(controller):
    # tests getting the description
    desc = test_bad_getDescription(controller.model)
    # tests getting the recipe
    recipe = test_bad_getRecipe(controller.model)
    # tests getting a different recipe
    other = test_bad_getProperty(controller.model)

    # verifies that the tests ran successfully
    if desc == 1 and recipe == 1 and other == 1:
        return 1
    else:
        return 0

'''
The testing of the view methods are more cumbersome as they involve launching new windows. 
Please go to testView.py to see the tests on the View.

'''

if __name__ == '__main__':
    # creates test Controller
    testController = Controller()
    # runs model tests
    recipeNames = test_getRecipeNames(testController)
    allTags = test_getAllTags(testController)
    validGetRecipe = test_valid_getRecipeProperty(testController)
    badGetRecipe = test_bad_getRecipeProperty(testController)

    # printing test results
    print('\n Test Results: \n ----------------------------------------')

    if validGetRecipe == 1:
        print('Expected: getRecipeProperty is processing good data successfully')
    else:
        print('Unexpected: getRecipeProperty is not processing good data properly')
    
    if badGetRecipe == 1:
        print('Expected: getRecipeProperty is catching bad data correctly')
    else:
        print('Unexpected: getRecipeProperty is not catching bad data')
    
    if recipeNames == 1:
        print('Expected: getRecipeNames has the correct output')
    else:
        print('Unexpected: getRecipeNames has bad output')
    
    if allTags == 1:
        print('Expected: getAllTags has the correct output')
    else:
        print('Unexpected: getAllTags has bad output')
    
