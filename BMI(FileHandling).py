#Jonathan L. Tinoy Jr
#3rd Year BS Stat 

#Activity#1
#Determining Body Mass Index (BMI) 

#Following is a chart for determining one’s body mass index (BMI). BMI is a general  indication of the amount of body fat that a person has. The formula for computing BMI  is,  
#BMI = mass / height2 
#Implement a Python program that prompts a user for their height and weight. Height  should be entered as inches and weight should be entered in pounds. Perform the  calculation in units of kilograms and meters as shown in the chart. Compare the result to  the information in the chart. Use class(es) in your program design. 

#Activity#2
#Change in the Program Specification
#Upgrade the BMI Calculator to cater to the additional inputs: age and sex. The program's output will also identify whether the BMI is underweight, normal, obese, or overweight. Then, save the following data in a file with the specified sequence for each row:

#age, sex, weight, height, BMI, BMI classification

class BMI:

    print("Welcome to my BMI calculator!")
    print("If you can tell me your weight and height")
    print("I can tell you your Body Mass Index")
    print("Thank You!\n")
    
    Age = input("Please state your age here: ")
    Sex = input("Please state your sex here: ")
    Inches = float(input("Please enter your height in inches: "))
    Pounds = float(input("Please enter your weight in pounds: "))
    get_height = Inches * 0.0254
    get_weight = Pounds / 2.2


    def BMI(get_height, get_weight):
        body_mass_index = round(get_weight/ (get_height ** 2), 1) 

        return body_mass_index

    class_BMI = ' '
    body_mass_index = BMI(get_height, get_weight)
    print("\nYour BMI is", format(body_mass_index), end='')

    if body_mass_index <= 18.5:
        print(', it means you are underweight.')

    elif body_mass_index > 18.5 and body_mass_index < 25:
        print(', it means you are normal.')

    elif body_mass_index >25 and body_mass_index <30:
        print(', it means you are overweight.')

    elif body_mass_index > 30:
        print(', it means you are obese.')

    else:
        print('THERE IS AN ERROR OF YOUR INPUT.')


    f=open('BMIlist.txt','a')
    f.write(str(Age)+','+Sex+','+str(get_weight)+','+str(get_height)+','+str(body_mass_index)+','+class_BMI+'\n')
    f.close()

    f=open('BMIlist.txt')
    line = 0
    while True:
        con=f.readline()
        if len(con)>0:
            print("\nAge, Sex, get_eight, get_height, BMI, class_BMI\n",con)
        else:
            break
    
