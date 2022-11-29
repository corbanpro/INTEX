from functions import searchRecipes

recipeDict = (searchRecipes('chicken quesadilla'))
for i in recipeDict:
    print(i, recipeDict[i])