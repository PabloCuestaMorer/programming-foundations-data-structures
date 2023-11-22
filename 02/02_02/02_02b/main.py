''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''
student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]
student_pet_count_list[2] = 3
student_pet_count_list[3] += 1
student_pet_count_list[-1] += 2
student_pet_count_list.append(4)

NUM_STUDENTS = len(student_pet_count_list)

total_pets_list = 0
for studen_num_pets in student_pet_count_list:
    total_pets_list += studen_num_pets

average = total_pets_list / NUM_STUDENTS

print(f'Average: {total_pets_list} / {NUM_STUDENTS} = {average}')