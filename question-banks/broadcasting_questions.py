# LIST NAMES MUST END WITH _QUESTIONS

set_broadcasting_tricky_QUESTIONS = [
"Given A = np.arange(6).reshape(2,3) and B = np.array([1,2,3]), determine the result of A + B.",
"Given A = np.arange(6).reshape(2,3) and B = np.array([[1],[2]]), determine the result of A + B.",
"Given A = np.arange(6).reshape(2,3) and B = np.array([1,2]), determine why A + B raises an error.",
"Given A = np.arange(6).reshape(2,3) and B = np.array([[1,2,3]]), determine the result of A + B.",
"Given A = np.arange(6).reshape(2,3), compute A + np.array([10]). Explain why broadcasting works.",
"Given A = np.arange(6).reshape(2,3), subtract the column means using broadcasting.",
"Given A = np.arange(6).reshape(2,3), subtract the row means using broadcasting.",
"Given A = np.arange(6).reshape(2,3), explain why A - A.mean(axis=1) fails.",
"Given A = np.arange(6).reshape(2,3), fix the previous operation using keepdims.",
"Given A = np.arange(6).reshape(2,3), compute A - A.mean(axis=1, keepdims=True).",
"Given A = np.arange(6).reshape(2,3), determine the shape of A + np.arange(3).",
"Given A = np.arange(6).reshape(2,3), determine the shape of A + np.arange(2)[:,None].",
"Given A = np.arange(6).reshape(2,3), determine the shape of A + np.arange(2).reshape(2,1).",
"Given A = np.arange(12).reshape(3,4), add row indices to each row using broadcasting.",
"Given A = np.arange(12).reshape(3,4), add column indices to each column using broadcasting.",
"Given A = np.arange(12).reshape(3,4), explain why np.arange(3) + np.arange(4) broadcasts to a 3x4 result when reshaped.",
"Given A = np.arange(12).reshape(3,4), compute A + np.arange(3)[:,None].",
"Given A = np.arange(12).reshape(3,4), compute A + np.arange(4).",
"Given A = np.arange(12).reshape(3,4), determine why A + np.arange(3) fails.",
"Given A = np.arange(12).reshape(3,4), determine the result of A * np.array([[1],[2],[3]]).",
"Given A = np.arange(12).reshape(3,4), determine the result of A * np.array([1,2,3,4]).",
"Given A = np.arange(12).reshape(3,4), explain why broadcasting does not copy data.",
"Given A = np.arange(12).reshape(3,4), explain how broadcasting works from the trailing dimensions.",
"Given A = np.arange(12).reshape(3,4), determine the shape of A + np.ones((3,1)).",
"Given A = np.arange(12).reshape(3,4), determine the shape of A + np.ones((1,4))."
]

set4_QUESTIONS = [
"Given A = np.arange(12).reshape(4,3), add 5 to every element.",
"Given A = np.arange(12).reshape(4,3), multiply all elements by 2.",
"Given A = np.arange(12).reshape(4,3), subtract row means from each row.",
"Given A = np.arange(12).reshape(4,3), normalize the array to 0-1 range.",
"Given A = np.arange(12).reshape(4,3), add vector [10,20,30] to each row.",
"Given A = np.arange(12).reshape(4,3), multiply columns by [1,2,3].",
"Given A = np.arange(12).reshape(4,3), compute row sums.",
"Given A = np.arange(12).reshape(4,3), compute column means.",
"Given A = np.arange(12).reshape(4,3), convert values >6 to 1 else 0.",
"Given A = np.arange(12).reshape(4,3), square every element.",
"Compute difference between each element and column mean.",
"Normalize each row by its row sum.",
"Find positions of multiples of 5.",
"Given A = np.random.randint(0,20,(5,5)), get indices of the max value."
]