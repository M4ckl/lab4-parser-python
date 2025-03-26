Task:

Study the characteristics of protocols and formats used for data exchange between systems: JSON, YAML, XML. Write a program in Python 3.x that performs parsing and conversion of the source file into a new format.

Source file format:

subjects = { 
            "subject1": { 
                   "Day": "Пон",
                   "Time": "10.00-11.30", 
                   "NumberOfWeeks": "2 4 6 8 10 12 14 16", 
                   "Room": "2435/4 (бывш. 431в) ауд.", 
                   "Lesson": "Информатика(лаб)", 
                   "Teacher": "Болдырева Елена Александровна", 
                   "Location": "Кронверский пр. д.49 лит.А", 
             }, 
             "subject2": { 
                   "Day": "Пон", 
                   "Time": "11.40-13.10", 
                   "NumberOfWeeks": "2 4 6 8 10 12 14 16", 
                   "Room": "2435/4 (бывш. 431в) ауд.", 
                   "Lesson": "Информатика(лаб)", 
                   "Teacher": "Болдырева Елена Александровна", 
                   "Location": "Кронверский пр. д.49 лит.А", 
             }, 
                   "subject3": { 
                   "Day": "Пон", 
                   "Time": "15.20-16.50", 
                   "NumberOfWeeks": "3 5 7 9 11 13 15 17", 
                   "Room": "2306/2 (бывш. 305) ауд.", 
                   "Lesson": "Основы профессиональной деятельности(лаб)", 
                   "Teacher": "Ткешелшвили Нино Мерабиевна", 
                   "Location": "Кронверский пр. д.49 лит.А", 
             }, 
             "subject4": { 
                   "Day": "Пон", 
                   "Time": "17.00-18.30", 
                   "NumberOfWeeks": "3 5 7 9 11 13 15 17", 
                   "Room": "2306/2 (бывш. 305) ауд.", 
                   "Lesson": "Основы профессиональной деятельности(лаб)", 
                   "Teacher": "Ткешелшвили Нино Мерабиевна", 
                   "Location": "Кронверский пр. д.49 лит.А", 
             }
        }
        
              
- Mandatory Task:

Write a Python 3.x program that parses and converts the original file into a new format.

- Additional Task 1:

Rewrite the original code using appropriate libraries. Regular expressions are not allowed.

- Additional Task 2:

Rewrite the original code using regular expressions.

Additional Task 3:

Using your programs from the mandatory task, additional task 1, and additional task 2, compare the execution time of parsing + conversion by running each 10 times in a loop.

python -m timeit "from lab4_parser import function"

Result:

1)500000 loops, best of 5: 850 nsec per loop

2)500000 loops, best of 5: 848 nsec per loop

3)500000 loops, best of 5: 868 nsec per loop

- Additional Task 4:

Rewrite the original code to perform parsing and conversion of the source file into another format (other than JSON, YAML, XML, HTML): e.g., PROTOBUF, TSV, CSV, WML, etc.



















