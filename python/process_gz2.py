import asciitable,random
gz2users = asciitable.read('/Users/willettk/Desktop/treemap/gz2_users.csv')
ss5000 = random.sample(gz2users,5000)
asciitable.write(ss5000,'/Users/willettk/Desktop/ss5000.csv')
