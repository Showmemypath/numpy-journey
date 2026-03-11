# LIST NAMES MUST END WITH _QUESTIONS

set_views_copies_tricky_QUESTIONS = [
"Given A = np.arange(10), create B = A[2:7] and determine whether B shares memory with A.",
"Given A = np.arange(10), modify B = A[2:7]; B[:] = -1 and determine the resulting A.",
"Given A = np.arange(10), create B = A[[2,3,4]] and determine whether B shares memory with A.",
"Given A = np.arange(10), modify B = A[[2,3,4]]; B[:] = -1 and determine the resulting A.",
"Given A = np.arange(12).reshape(3,4), determine whether B = A[:,1:3] shares memory with A.",
"Given A = np.arange(12).reshape(3,4), determine whether B = A[:,[1,2]] shares memory with A.",
"Given A = np.arange(12).reshape(3,4), check if B = A.T shares memory with A.",
"Given A = np.arange(12).reshape(3,4), modify B = A.T; B[0,0] = -1 and determine the effect on A.",
"Given A = np.arange(12).reshape(3,4), determine if reshape returns a view or copy.",
"Given A = np.arange(12).reshape(3,4), compute B = A.reshape(-1) and modify B[0] = -1.",
"Given A = np.arange(12).reshape(3,4), compute B = A.flatten() and modify B[0] = -1.",
"Given A = np.arange(12).reshape(3,4), explain why flatten behaves differently from ravel.",
"Given A = np.arange(12).reshape(3,4), compute B = A.ravel() and modify B[0] = -1.",
"Given A = np.arange(12).reshape(3,4), determine whether ravel always returns a view.",
"Given A = np.arange(12).reshape(3,4), use np.shares_memory(A,B) to verify memory sharing.",
"Given A = np.arange(12).reshape(3,4), check whether B = A.copy() shares memory with A.",
"Given A = np.arange(12).reshape(3,4), modify B = A.copy(); B[0,0] = -1 and determine the effect on A.",
"Given A = np.arange(10), determine whether slicing with negative stride A[::-1] shares memory.",
"Given A = np.arange(10), modify B = A[::-1]; B[0] = -1 and determine the effect on A.",
"Given A = np.arange(12).reshape(3,4), explain why chained indexing like A[:,1:3][:,0] can create copies."
]
