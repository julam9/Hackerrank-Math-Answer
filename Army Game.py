## Army Game
# Objective : Given square with n rows and m columns, determine minimum # of packages need to be sent to
# supply all the boxes
# Ilustration : https://www.hackerrank.com/challenges/game-with-cells/problem?isFullScreen=true 
def gamewithcells(n, m):
    new_n = n if n % 2 == 0 else n+1
    new_m = m if m % 2 == 0 else m+1
    n_packages = new_m//2*new_n//2
    return n_packages


# testing function
print(gamewithcells(1000, 999))