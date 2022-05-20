'''
Charlie Lees
This file will be a test for the Model class in this project.

I will be testing each of the functions in the class to make sure it is grabbing the correct data
also going to be sure that it catches bad input.

'''

from Model import Model

# testing the getColumn function with valid and invalid input
def test_valid_getColumn(model):
    # Valid input check
    correctOutput = "0                     Meatloaf\n1                  Pasta Salad\n2                  Pulled Pork\n3                 Clam Chowder\n4                    Prime Rib\n5            Yorkshire Pudding\n6                  Vodka Sauce\n7         Sweet & Sour Chicken\n8         Twice Baked Potatoes\n9    Chicken and Tortilla Soup\nName: Name, dtype: object"
    output = str(model.getColumn('Name'))
    if correctOutput == output:
        # return value for correct output
        return 1
    else:
        # return value for incorrect output
        return 0
def test_bad_getColumn(model):
    # invalid input check
    testResults = 0
    # checks to be sure the method catches a bad string and wrong types
    if model.getColumn('badinput') == 0:
        testResults += 1
    if model.getColumn(0) == 0:
        testResults += 1
    if model.getColumn(0.00) == 0:
        testResults += 1

    # returns a good value if all tests are caught
    if testResults == 3:
        return 1
    # if at least one test fails, return 0
    else:
        return 0


# testing the getProperty function with valid and invalid input
def test_valid_getProperty(model):
    # tests getProperty with valid input
    validOutput = 'descriptions\meatloafDesc.txt'
    testOutput = model.getProperty('Description', 'Meatloaf')
    # returns 1 for correct output, returns 0 for bad output
    if validOutput == testOutput:
        return 1
    else:
        return 0
def test_bad_getProperty(model):
    # tests getProperty with invalid input
    invalidOutputInteger = model.getProperty(5, 10)
    invalidOutputFloat = model.getProperty(1.0, 2.0)
    invalidOutputString = model.getProperty('dog', 'beans')

    # if all of the bad data was caught, return 1.
    if invalidOutputFloat == 0 and invalidOutputInteger == 0 and invalidOutputString == 0:
        return 1
    else:
        return 0

# testing the tagList function
def test_tagList(model):
    # compares the taglist with what it should be for our data
    correctList = ['Bread', 'MeatBased', 'Pasta', 'BBQ', 'Soup', 'Fish', 'Christmas', 'QuickDinner', 'Potatoes', 'Mexican']
    output = model.tagList()

    # compares the two lists together.
    if correctList == output:
        return 1
    else:
        return 0

# testing the nameList function
def test_nameList(model):
    # compares the namelist with what it should be for our data
    correctList = ['Meatloaf', 'Pasta Salad', 'Pulled Pork', 'Clam Chowder', 'Prime Rib', 'Yorkshire Pudding', 'Vodka Sauce', 'Sweet & Sour Chicken', 'Twice Baked Potatoes', 'Chicken and Tortilla Soup']
    output = model.nameList()
    

    # compares the two lists together.
    if correctList == output:
        return 1
    else:
        return 0

# testing the getDescription function with valid and invalid input
def test_valid_getDescription(model):
    # gets fresh output as well as what it should be
    validOutput = '\nMix together with your hands - if sticky add more crumbs\nIf Meatballs:\n- Form into balls and arrange on an aluminum foil lined cookie sheet \n- Bake 30 minutes at 350\n- Place par cooked meatballs in spaghetti sauce in crockpot\n- Cook on high for 2 hours or low for up to 6 hrs. Stir 2-3 times.\nIf Meatloaf:\n- Form into a large ball and push into a bread pan\n- Bake at 350 for about an hour.\n- Use meat thermometer when center reaches 160 the center is medium rare and ready.\nSource : Lees Family Recipe\n'
    testOutput = model.getDescription('Meatloaf')
    # if the output is valid, return 1
    if validOutput == testOutput:
        return 1
    else:
        return 0
def test_bad_getDescription(model):
    # tests getDescription with various bad data
    testInt = model.getDescription(1)
    testFloat = model.getDescription(1.0)
    testStr = model.getDescription('beans')

    # if all tests are caught successfully, return 1
    if testInt == 0 and testFloat == 0 and testStr == 0:
        return 1
    else:
        return 0

# testing the getRecipe function with valid and invalid input
def test_valid_getRecipe(model):
    # the correct output as well as the current output from the model
    correctOutput = '\n- 1t Bells Seasoning\n- 1t Garlic Powder\n- 1t Onion Powder\n- 2 eggs\n- 1t dried basil\n- 1/2 t salt\n- 1/2 t ground pepper\n- 2T Milk\n- 3/4 C Breadcrumbs\n- 1/4 C Parmesan\n'
    testOutput = model.getRecipe('Meatloaf')

    # if the current output is correct, return 1
    if correctOutput == testOutput:
        return 1
    else:
        return 0
def test_bad_getRecipe(model):
    # tests getRecipe with various bad data
    testInt = model.getRecipe(1)
    testFloat = model.getRecipe(1.0)
    testStr = model.getRecipe('beans')

    # if all tests are caught successfully, return 1
    if testInt == 0 and testFloat == 0 and testStr == 0:
        return 1
    else:
        return 0

# Not going to test _readdata, it is a private method used when a Model is created.

# runs tests
if __name__ == '__main__':
    # creates model for testing
    testModel = Model()
    # getColumn tests
    validGetColumn = test_valid_getColumn(testModel)
    badGetColumn = test_bad_getColumn(testModel)
    
    # getProperty tests
    validGetProperty = test_valid_getProperty(testModel)
    badGetProperty = test_bad_getProperty(testModel)

    # tagList test
    tagList = test_tagList(testModel)

    # nameList test
    nameList = test_nameList(testModel)

    # getDescription tests
    validGetDescription = test_valid_getDescription(testModel)
    badGetDescription = test_bad_getDescription(testModel)

    # getRecipe tests
    validGetRecipe = test_valid_getRecipe(testModel)
    badGetRecipe = test_bad_getRecipe(testModel)

    # prints test results
    print('\n Test Results: \n ----------------------------------------')
    # get column results
    if validGetColumn == 1:
        print('Expected: getColumn is processing good data successfully')
    else:
        print('Unexpected: getColumn is not processing good data properly')
    
    if badGetColumn == 1:
        print('Expected: getColumn is catching bad data correctly')
    else:
        print('Unexpected: getColumn is not catching bad data')

    # get property results
    if validGetProperty == 1:
        print('Expected: getProperty is processing good data successfully')
    else:
        print('Unexpected: getProperty is not processing good data properly')
    
    if badGetProperty == 1:
        print('Expected: getProperty is catching bad data correctly')
    else:
        print('Unexpected: getProperty is not catching bad data')

    # tagList results
    if tagList == 1:
        print('Expected: tagList has the correct output')
    else:
        print('Unexpected: tagList has bad output')
    
    # nameList results
    if nameList == 1:
        print('Expected: nameList has the correct output')
    else:
        print('Unexpected: nameList has bad output')
    
    # get description results
    if validGetDescription == 1:
        print('Expected: getDescription is processing good data successfully')
    else:
        print('Unexpected: getDescription is not processing good data properly')
    
    if badGetDescription == 1:
        print('Expected: getDescription is catching bad data correctly')
    else:
        print('Unexpected: getDescription is not catching bad data')
    
    # get recipe results
    if validGetRecipe == 1:
        print('Expected: getRecipe is processing good data successfully')
    else:
        print('Unexpected: getRecipe is not processing good data properly')
    
    if badGetRecipe == 1:
        print('Expected: getRecipe is catching bad data correctly')
    else:
        print('Unexpected: getRecipe is not catching bad data')
