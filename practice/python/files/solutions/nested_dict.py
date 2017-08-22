ramit = {
    'name' : 'Ramit',
    'email' : 'ramit@gmail.com',
    'interests' : ['movies', 'tennis'],
    'friends' : [
        {
            'name' : 'Jasmine',
            'email' : 'jasmine@yahoo.com',
            'interests' : ['photography', 'tennis']
        },
        {
        'name' : 'Jan',
        'email' : 'jan@hotmail.com',
        'interests' : ['movies', 'tv']
        }
    ]
}

r_email = ramit['email']
print(r_email)

r_interests_1 = ramit['interests'][0]
print(r_interests_1)

jas_email = ramit['friends'][0]['email']
print(jas_email)

jas_interests_2 = ramit['friends'][1]['interests'][1]
print(jas_interests_2)
