data=[34,56,45,34,56,45,12,23,45]
def remove_element(arr):
    nodup=[]
    for element in arr:
        if element not in nodup:
            nodup.append(element)
    return nodup
print(remove_element(data))