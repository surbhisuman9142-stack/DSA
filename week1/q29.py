def remove_duplicates(list):
    result = []
    for item in list:
        if item not  in result:
            result.append(item)
    return result
list = [4,5,6,7,4,8,9,5,0]
print(remove_duplicates(list)) 
    