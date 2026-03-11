# LIST NAMES MUST END WITH _QUESTIONS
set_sorting_basics_QUESTIONS = [
"Given A = np.array([5,2,9,1,7]), return a sorted copy of the array using np.sort.",
"Given A = np.array([[4,2,7],[1,5,3]]), sort each row using np.sort with axis.",
"Given A = np.array([[4,2,7],[1,5,3]]), sort each column using np.sort with axis.",
"Given A = np.array([8,3,6,1,9]), sort the array in-place using ndarray.sort.",
"Given A = np.array([8,3,6,1,9]), verify that ndarray.sort modifies the original array.",
"Given A = np.array([50,20,40,10,30]), return indices that would sort the array using argsort.",
"Given A = np.array([50,20,40,10,30]), reorder the array using argsort.",
"Given A = np.array([50,20,40,10,30]), find indices of the three smallest elements using argsort.",
"Given A = np.array([[9,3,5],[2,8,1],[7,4,6]]), sort each row and return the sorted result.",
"Given A = np.array([[9,3,5],[2,8,1],[7,4,6]]), return column indices that would sort each row using argsort.",
"Given A = np.array([7,2,9,4,1,5]), find the 3 smallest elements using partition.",
"Given A = np.array([7,2,9,4,1,5]), find the 3 largest elements using partition.",
"Given A = np.array([7,2,9,4,1,5]), return indices of the 3 smallest elements using argpartition.",
"Given A = np.array([7,2,9,4,1,5]), return indices of the 2 largest elements using argpartition.",
"Given A = np.array([7,2,9,4,1,5]), retrieve the actual 3 smallest values using argpartition.",
"Given A = np.array([7,2,9,4,1,5]), retrieve the actual 2 largest values using argpartition.",
"Given A = np.array([1+2j,3+1j,2+4j,1+1j]), sort complex numbers using np.sort and observe ordering.",
"Given A = np.array([1+2j,3+1j,2+4j,1+1j]), sort complex numbers by magnitude using sort_complex.",
"Given names = np.array(['Tom','Alice','Bob','Alice']) and ages = np.array([25,30,25,22]), sort by age using argsort.",
"Given names = np.array(['Tom','Alice','Bob','Alice']) and ages = np.array([25,30,25,22]), sort by age and break ties using names with lexsort."
]

set_sorting_mastery_QUESTIONS= [
"Given A = np.array([40,10,30,20]), compute the rank of each element using argsort twice.",
"Given A = np.array([40,10,30,20]), return indices that would sort the array and use them to reorder A.",
"Given A = np.array([9,3,7,1,6]), retrieve the 3 smallest values using argpartition and then sort them.",
"Given A = np.array([9,3,7,1,6]), explain why argpartition does not fully sort the first 3 elements.",
"Given A = np.array([9,3,7,1,6]), retrieve the indices of the 2 largest values using argpartition.",
"Given A = np.array([9,3,7,1,6]), use argpartition to move the smallest element to its correct position.",
"Given A = np.array([[5,2,9],[1,7,3],[8,4,6]]), return indices that would sort each row using argsort.",
"Given A = np.array([[5,2,9],[1,7,3],[8,4,6]]), reorder each row using the indices returned by argsort.",
"Given A = np.array([[5,2,9],[1,7,3],[8,4,6]]), find indices of the two smallest elements in each row using argpartition.",
"Given A = np.array([5,5,2,2,9,9]), verify that argsort preserves stable ordering of equal values.",
"Given names = np.array(['Tom','Alice','Bob','Alice']) and ages = np.array([25,30,25,22]), sort by age using argsort.",
"Given names = np.array(['Tom','Alice','Bob','Alice']) and ages = np.array([25,30,25,22]), reorder names according to sorted ages.",
"Given names = np.array(['Tom','Alice','Bob','Alice']) and ages = np.array([25,30,25,22]), sort by age and break ties using names with lexsort.",
"Given scores = np.array([85,90,85,92]) and ids = np.array([3,1,4,2]), sort by scores and break ties using ids with lexsort.",
"Given two arrays X = np.array([1,1,2,2]) and Y = np.array([3,1,4,2]), sort by X first and Y second using lexsort.",
"Given X = np.array([1,1,2,2]) and Y = np.array([3,1,4,2]), explain why the order of keys matters in lexsort.",
"Given A = np.array([8,4,7,1,9,2]), find the median element using partition.",
"Given A = np.array([8,4,7,1,9,2]), place the 3rd smallest element into its correct position using partition.",
"Given A = np.array([8,4,7,1,9,2]), verify that elements before the partition index are smaller but not sorted.",
"Given A = np.array([3+4j,1+2j,2+1j,1+1j]), sort complex numbers using sort_complex and compare with np.sort."
]

set3_QUESTIONS = [
"Given A = np.array([8,3,15,1,9,12,7,5]), sort ascending.",
"Given A = np.array([8,3,15,1,9,12,7,5]), sort descending.",
"Given A = np.array([8,3,15,1,9,12,7,5]), get indices that would sort the array.",
"Given A = np.array([8,3,15,1,9,12,7,5]), find index of largest value.",
"Given A = np.array([8,3,15,1,9,12,7,5]), find index of smallest value.",
"Given A = np.array([8,3,15,1,9,12,7,5]), get the 3 largest values.",
"Given A = np.array([8,3,15,1,9,12,7,5]), get the 3 smallest values.",
"Given A = np.array([8,3,15,1,9,12,7,5]), find positions where value > 8.",
"Given A = np.array([8,3,15,1,9,12,7,5]), count elements greater than the mean.",
"Given A = np.array([8,3,15,1,9,12,7,5]), find unique elements."
]