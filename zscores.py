#Takes in a list of numbers and one of the numbers in that list; returns z-score 
def z_from_raw(seq, x):
    import descriptives 
    mean = descriptives.arith_mean(seq) 
    sd = descriptives.pop_stdev(seq) 
    z = round(((x - mean)/sd), 2)
    return z 

#Takes in a score, mean and standard deviation of the distribution; returns z-score     
def z_from_param(x, mu, sig):
    z = round(((x - mu)/sig), 2) 
    return z 

#Takes in z-score, mean and standard deviation of the distribution; returns raw score     
def x_from_z(z, mu, sig):
    x = round(((z*sig) + mu), 2) 
    return x 

#Finds critical z-score from ztable.txt file 
#Options: one-tail or two-tailed test, .05 or .01 alpha level     
def find_zcrit(alpha):
    opentable = open('ztable.txt')
    new = [[row.rstrip()] for row in opentable]
    new2 = []
    for row in new:
        for string in row:
            splitup = string.split(' ') 
            new2.append(splitup) 
    for i in range(len(new2)):
        new2[i] = [float(num) for num in new2[i] if not num == '']
    differences = []
    tail = input('Type 1 for one-tailed test\nType 2 for two-tailed test:\n')
    if tail == '1':
        for list in new2:
            for number in list:
                diff = abs(number - (1 - float(alpha)))
                differences.append(diff)
        minimum = min(differences) 
        for list in new2:
            for number in list:
                if abs(number - (1 - float(alpha))) == minimum:
                    zcrit = list[0] + (list.index(number)/100)
        return round(zcrit, 2)
    elif tail == '2':
        if float(alpha) == .05:
            zcrit = 1.96
            return zcrit 
        elif float(alpha) == .01:
            zcrit = 2.58 
            return zcrit 
        else:
            print('ERROR: alpha not supported')
    else:
        print('ERROR!') 

#Given group mean, mean of group means, standard deviation, and group size (n), returns z-score for group         
def z_groups(xbar, mu, sd, n):
    import descriptives
    return round(float((xbar - mu)/(descriptives.stderror(sd, n))), 2) 

#One-sample z-test (takes in group mean, mean of group means, SD, n, and desired alpha level)    
def one_sample_ztest(xbar, mu, sd, n, alpha):
    import descriptives 
    global z_groups, find_zcrit
    test = z_groups(xbar, mu, sd, n)
    crit = find_zcrit(alpha) 
    if abs(test) > crit:
        print('z = %r; critical z = %r; Significant; p < %r' %(test, crit, alpha))
    else:
        print('z = %r; critical z = &r; Not Significant; p > %r' %(test, crit, alpha)) 
        
#Calculates 95% or 99% CI based on the normal distribution 
def z_interval(xbar, sd, n):
    import descriptives 
    se = descriptives.stderror(sd, n)
    conf = input('Type 1 for 95% CI\nType 2 for 99% CI\n')
    if conf == '1':
        zcrit = 1.96
        level = '95%'
    elif conf == '2':
        zcrit = 2.58
        level = '99%' 
    else:
        print('ERROR!')
        zcrit = None 
    upper = round((xbar + (zcrit*se)), 2) 
    lower = round((xbar - (zcrit*se)), 2)  
    print('%s CI for pop. mean: %r -- %r' % (level, lower, upper))
    

    
