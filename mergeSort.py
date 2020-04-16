"""
Hey! Thank you for supporting my youtube channel 
( https://www.youtube.com/channel/UCKrs-v_MlKjzVbe4jyLSrPQ ). 

This video is part of my code along series:
https://www.youtube.com/playlist?list=PLFHNXQ6Nn6P4d74m69moUMP8xsWkz4IXa

DeveloperDamion
"""

def merge(leftArray = [], rightArray = []):

	mergedArray = []

	while len(leftArray) > 0 and len(rightArray) > 0:
		if leftArray[0] < rightArray[0]:
			mergedArray.append(leftArray.pop(0))
		else:
			mergedArray.append(rightArray.pop(0))

	return mergedArray + leftArray + rightArray


def mergeSort(unsortedArray = []):

	if len(unsortedArray) <= 1: return unsortedArray

	midPoint = len(unsortedArray)//2

	leftArray = unsortedArray[:midPoint]
	rightArray = unsortedArray[midPoint:]

	return merge( leftArray= mergeSort(leftArray), rightArray = mergeSort(rightArray) )


if __name__ == "__main__":
	unsortedArray = [12,15,10,8,5,7,9]

	print(mergeSort(unsortedArray))