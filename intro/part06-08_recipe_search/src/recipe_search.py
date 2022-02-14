# Write your solution here

def search_by_name(filename: str, word: str):
    recipe_list = []
    formated_recipe = []
    found_recipes = []
    with open(filename) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            recipe_list.append(line)

        while True:
            if '' in recipe_list:
                recipe_dict = {}
                point = recipe_list.index('')
                recipe_dict['name'] = recipe_list[0]
                recipe_dict['time'] = recipe_list[1]
                recipe_dict['recipe'] = recipe_list[2:point]
                recipe_list = recipe_list[point+1:]
                formated_recipe.append(recipe_dict)
            else:
                recipe_dict = {}
                recipe_dict['name'] = recipe_list[0]
                recipe_dict['time'] = recipe_list[1]
                recipe_dict['recipe'] = recipe_list[2:point]
                formated_recipe.append(recipe_dict)
                break
    for r in formated_recipe:
        if word.lower() in r['name'].lower():
            found_recipes.append(r['name'])
    return found_recipes
        
def search_by_time(filename: str, prep_time: int):
    recipe_list = []
    formated_recipe = []
    found_recipes = []
    with open(filename) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            recipe_list.append(line)

        while True:
            if '' in recipe_list:
                recipe_dict = {}
                point = recipe_list.index('')
                recipe_dict['name'] = recipe_list[0]
                recipe_dict['time'] = recipe_list[1]
                recipe_dict['recipe'] = recipe_list[2:point]
                recipe_list = recipe_list[point+1:]
                formated_recipe.append(recipe_dict)
            else:
                recipe_dict = {}
                recipe_dict['name'] = recipe_list[0]
                recipe_dict['time'] = recipe_list[1]
                recipe_dict['recipe'] = recipe_list[2:point]
                formated_recipe.append(recipe_dict)
                break
    for r in formated_recipe:
        if int(r['time']) <= prep_time:
            found_recipes.append(f"{r['name']}, preparation time {r['time']} min")
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipe_list = []
    formated_recipe = []
    found_recipes = []
    with open(filename) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            recipe_list.append(line)

        while True:
            if '' in recipe_list:
                recipe_dict = {}
                point = recipe_list.index('')
                recipe_dict['name'] = recipe_list[0]
                recipe_dict['time'] = recipe_list[1]
                recipe_dict['recipe'] = recipe_list[2:point]
                recipe_list = recipe_list[point+1:]
                formated_recipe.append(recipe_dict)
            else:
                recipe_dict = {}
                recipe_dict['name'] = recipe_list[0]
                recipe_dict['time'] = recipe_list[1]
                recipe_dict['recipe'] = recipe_list[2:point]
                formated_recipe.append(recipe_dict)
                break
    for r in formated_recipe:
        if ingredient in r['recipe']:
            found_recipes.append(f"{r['name']}, preparation time {r['time']} min")
    return found_recipes
            
if __name__ == "__main__":
    #found_recipes = search_by_name("recipes1.txt", "cake")
    #for recipe in found_recipes:
        #print(recipe)
    
    #found_recipes = search_by_name("recipes2.txt", "oat")
    #for recipe in found_recipes:
        #print(recipe)

    #found_recipes = search_by_time("recipes1.txt", 20)
    #for recipe in found_recipes:
        #print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)
