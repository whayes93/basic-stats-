#Returns the arithmetic mean of a list of numbers 
def arith_mean(seq):
    total = sum(seq)
    count = len(seq)
    return (float(total/count)) 

#Returns the sum of squares of a list of numbers 
def sumsq(seq):
    global arith_mean
    mean = arith_mean(seq)
    sumsqdev = []
    for num in seq:
        sqdev = float((num - mean)**2)
        sumsqdev.append(sqdev) 
    return round((sum(sumsqdev)), 2) 

#Returns the population variance of a list of numbers    
def pop_var(seq):
    global sumsq 
    return float(sumsq(seq)/len(seq)) 

#Returns the sample variance of a list of numbers     
def sample_var(seq):
    global sumsq
    return round((float(sumsq(seq)/(len(seq) - 1))), 2)

#Returns the population standard deviation of a list of numbers    
def pop_stdev(seq):
    import math 
    global pop_var
    return float(math.sqrt(pop_var(seq))) 

#Returns the sample standard deviation of a list of numbers     
def sample_stdev(seq):
    import math 
    global sample_var
    return round((float(math.sqrt(sample_var(seq)))), 2)  

#Returns the range of a list of numbers     
def rrange(seq):
    return max(seq) - min(seq) 

#Returns the weighted mean of a set of lists of numbers (different n's)    
def wght_mean(*args):
    totals = []
    counts = []
    for seq in args:
        summed = sum(seq)
        n = len(seq)
        totals.append(summed)
        counts.append(n) 
    Total = sum(totals)
    Count = sum(counts)
    return float(Total/Count)

#Given a SD and N, returns the standard error     
def stderror(sd, n):
    import math 
    return round((float(sd/math.sqrt(n))), 2) 

#Given two lists of numbers, returns the pooled variance     
def pooled_var(seq1, seq2):
    global sumsq
    SS1 = sumsq(seq1)
    SS2 = sumsq(seq2) 
    n1 = len(seq1)
    n2 = len(seq2) 
    return ((SS1+SS2)/((n1-1)+(n2-1))) 

#Returns the standard error of the difference for a separate variances t-test    
def sep_stderr_diff(seq1, seq2):
    import math 
    global sample_var
    var1 = sample_var(seq1)
    var2 = sample_var(seq2)
    n1 = len(seq1)
    n2 = len(seq2) 
    return (math.sqrt((var1/n1)+(var2/n2))) 

#Returns the standard error of the difference for a regular independent-samples t-test     
def pooled_stderr_diff(seq1, seq2):
    import math 
    global pooled_var
    pooled = pooled_var(seq1, seq2)
    n1 = len(seq1); n2 = len(seq2)
    return round(((math.sqrt((pooled/n1)+(pooled/n2)))), 2)
        