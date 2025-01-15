import time
age = 32

# the test condition is always True
# while True:
#     print('You can vote')
#     time.sleep(0.3)
#     print('You can drive')

students = ["Nicolas", "Geogios", "Homan", "Elena", "Cyrille"]
a = 10

for i in range(a):
    print(i)
    if i %2 == 0:
        i+=2
        
print()

for student in students:
    print(student)