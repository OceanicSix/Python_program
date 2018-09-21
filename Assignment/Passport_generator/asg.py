from random import randint

#to get new name

#first name
f_fname=input('please input a first name: ')
s_fname=input('please input the second first name: ')
#length of first half of first name.if odd, floor division.
len_1f=len(f_fname)//2
#length of second half of first name,if odd, ceiling division
len_2f=(len(s_fname)//2)+1
# two parts of new first name, concatenation
n_fname1=f_fname[:len_1f]
n_fname2=s_fname[len_2f-1:]
n_fname=n_fname1+n_fname2

#last name
f_lname=input('please input a last name: ')
s_lname=input('please input the second last name: ')
len_1l=len(f_lname)//2
len_2l=(len(s_lname)//2)+1
# two parts of new last name
n_lname1=f_lname[:len_1l]
n_lname2=s_lname[len_2l-1:]
n_lname=n_lname1+n_lname2

#new name
n_name=n_fname.capitalize()+' '+n_lname.capitalize()


#to get new date of birth

f_age=input('please input first age: ')
s_age=input('please input the second age: ')
sum1=0
#for each digit,convert to int and add together
for digit1 in f_age:
    sum1+=int(digit1)
sum2=0
for digit2 in s_age:
    sum2+=int(digit2)
# new age
age=sum1+sum2

#to get birthday
year_now=int(input('please input the current year: '))
# year of birth
year=year_now-age
# month of birth
month=randint(1,12)
#number of days in every month,including Feb has 29 days scenario
month_29=[0,31,29,31,30,31,30,31,31,30,31,30,31]
month_28=[0,31,28,31,30,31,30,31,31,30,31,30,31]
#generate date of birth from 1 to the last day in a month
if (year%100!=0 and year%4==0) or (year%100==0 and year%400==0):
    day=randint(1,month_29[month])
else:
    day=randint(1,month_28[month])

#new date of birth
b_date=str(day).zfill(2)+'/'+str(month).zfill(2)+'/'+str(year).zfill(4)


#get new ID

#seperate each digit
list_id=list(str(age))
length=len(str(age))
#to get 10 digits
for times in range(10-length):
    sum3 = 0
    # get last two digits in list_a
    for letter in list_id[-1:-3:-1]:
        sum3 += int(letter)
    # append the last digit,change to str to keep format consistent
    list_id.append(str(sum3%10))

id=''.join(list_id)


#encrypted method

shift=randint(1,25)
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
new_alphabet=alphabet[:]
#cut the front and append to the end
cut_alphabet=new_alphabet[0:shift]
del new_alphabet[0:shift]
new_alphabet.extend(cut_alphabet)
#generate dict
zipped_alphabet=zip(new_alphabet,alphabet)
list_alphabet=list(zipped_alphabet)
cipher=dict(list_alphabet)


#to print the encrypted information

#unencrypted info and print
pass_info=n_name+'\t'+id+'\n'+'\n'+b_date+'\n'+'\n'+'Authorised by Najam Zaidi'
print('\n'+'\n'+pass_info)
en_passinfo=''
#only encrypt letters
for item in pass_info.lower():
    if item in cipher:
        en_passinfo+=cipher[item]
    else:
        en_passinfo+=item

print('\n'+'\n'+en_passinfo)
print('\n'+'\n'+'Caesar cipher: left shift '+str(shift))







