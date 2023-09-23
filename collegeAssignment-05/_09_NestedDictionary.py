studentData={
    'vedant':{'ID':123,
              'Course':'BCS',
              'Age':20
              },
    'omkar':{'ID':456,
              'Course':'BSC-CS',
              'Marks':25
              },
    'pratik':{'ID':789,
              'Course':'BA',
              'Marks':30
              },
}

for name, sData in studentData.items():
    print("\nName:", name)

    for key in sData:
        print(key + ':', sData[key])
