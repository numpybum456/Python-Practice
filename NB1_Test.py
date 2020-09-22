# Test 1: Example
d1= {'inds': [1, 0, 0, 17, 5, 2, 4, 1, 8, 1, 19, 19, 19, 0, 2, 8, 5, 8, 13, 2, 9], 'vals': [0.7, 0.1, 0.4, 0.5, 0.1, 0.3, 0.5, 0.6, 0.0, 0.9, 0.6, 0.4, 0.5, 0.4, 0.8, 0.9, 0.7, 0.7, 0.8, 0.3, 0.5]}
d2 = {'inds': [0, 3, 1, 0, 2, 1, 18, 2, 6, 1, 16, 16, 12, 15, 10, 0, 10, 2], 'vals': [0.1, 0.3, 0.9, 0.4, 0.1, 0.4, 0.1, 0.4, 0.6, 0.9, 0.9, 0.0, 0.1, 0.1, 0.1, 0.9, 0.3, 0.9]}
expected_ans = [2, 0, 1]

### YOUR CODE HERE
new_ls = []
ind1 = d1['inds']
ind2 = d2['inds']
if len(ind1) >= len(ind2):
    for i in ind1:
        if i in ind2 and i not in new_ls:
            new_ls.append(i)
    print(new_ls)
else:
    for i in ind2:
        if i in ind1 and i not in new_ls:
            new_ls.append(i)

print(new_ls)


###################################################################
grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]

grades

# YOUR CODE HERE
students = []
for i in range(1, len(grades)):
    students.append(grades[i][0])
print(students)

assignments = []
asn_len = len(grades[1])
count=1
for j in range (count,len(grades)):
    for i in range(1,asn_len):
        assignments.append(grades[1][i])
        count = count + 1
print(assignments)