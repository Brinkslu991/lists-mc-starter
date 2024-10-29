# Lucas Brinks
# 10/29/24
# Generating Grade Reports

joshua = ['Josh', 'PHILLIPS', 'Alba', 'Web & Game Design',]
j_tests = [87,90,64,73]

avj_test = sum(j_tests) / len(j_tests)

lucas = ['Lucas', 'BRINKS', 'Home Schooled', 'Web & Game Design']
l_tests = [84,96,67,71]

avl_test = sum(l_tests) / len(l_tests)

print('Semester 1 Grade Report')

print('-----------------------')

print(f'Student: {joshua[1]}, {joshua[0]}')
print(f'School: {joshua[2]}')
print(f'Course: {joshua[3]}')
print(f'Average score: {avj_test:.2f}')

print()

print(f'Student: {lucas[1]}, {lucas[0]}')
print(f'School: {lucas[2]}')
print(f'Course: {lucas[3]}')
print(f'Average score: {avl_test:.2f}')