# match case
a='hello'

match a:
  case 'hi':
    print('hi case matched')
  case 'hello':
    print('hello case matched') 
  case _:
    print('no case matched')