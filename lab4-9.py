num_students = int(input())
all_known_languages = set()

at_least_one_known_languages = set()

for _ in range(num_students):
  
    num_languages_known = int(input())
    

    student_languages = set()
    
  
    for _ in range(num_languages_known):
        language = input()
        student_languages.add(language)
    

    if not all_known_languages:
        all_known_languages = student_languages.copy()
        at_least_one_known_languages = student_languages.copy()
    else:
      
        all_known_languages.intersection_update(student_languages)
        at_least_one_known_languages.update(student_languages)


all_known_languages = sorted(all_known_languages)
at_least_one_known_languages = sorted(at_least_one_known_languages)


print(len(all_known_languages))
for language in all_known_languages:
    print(language)

print(len(at_least_one_known_languages))
for language in at_least_one_known_languages:
    print(language)
