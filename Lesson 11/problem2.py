print('-'*80)
print('Narrative Bot')
print()

name = input('Student name:')
Grade = input('Grade:')
Grade = int(Grade)

if Grade >= 65:
	print('Narrative:')
	print('Skye, Your final grade in AP Computer Sicence is 94%.You have excelled in all components of the class! I wish you have continued success in the next semester of AP Computer Science')
else: print('Cary, Your final grade in AP Computer Sicence is 62%.This largely a result of missing projects and homework assignments.Unfortunately, because this grade is ess then a 65, you will have to complete an MBA assignments next semester ')
