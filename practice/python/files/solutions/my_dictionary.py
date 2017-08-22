phonebook_dict = {
    'Alice' : '770-493-1834',
    'Bob' : '857-384-1234',
    'Elizabeth' : '484-584-2923',
}

e_phone_number = phonebook_dict['Elizabeth']
#print(e_phone_number)

phonebook_dict['Kareem'] = '938-489-1234'
knum = phonebook_dict['Kareem']
#print knum

#del phonebook_dict['Alice']
#alice_num = phonebook_dict['Alice']

entries = phonebook_dict.items

#print(entries)

#for value in phonebook_dict:
    #print value

items = phonebook_dict.items()
print items
