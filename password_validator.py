special = ['!','@','#','$','%','&','*']
num = ['1','2','3','4','5','6','7','8','9','0']
fc = 0
sc = 0 
password = input('Enter:')
ln = len(password)
for i in password:
  if i in special:
    fc += 1
  if i in num:
    sc += 1
if fc >= 2 and sc >= 2 and ln == 14:
  print('Strong')
else:
  print('Weak')
print(num.index('0')) 
