text = input('Enter your text: ')
text_list = text.split()

if len(text_list)>=3:
    print(text_list[-3:])
if len(text_list)<3:
    print('There are less than 3 elements: ', len(text_list))