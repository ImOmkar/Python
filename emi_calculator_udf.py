def EMI_Cal(p_a,r_i,n_p): #parameters
    
    r_i=r_i/(12*100) #rate of interest
    n_p=n_p*12       #no of period
    emi=(p_a*r_i*((1+r_i)**n_p))/((1+r_i)**n_p-1)
    return int(emi)

p_a=int(input("Enter The Principle Ammount: ")) #principle ammount
r_i=float(input("Enter The Rate Of Interest: "))
n_p=int(input("Enter The Time Period: "))

print("Your EMI Is: ",EMI_Cal(p_a,r_i,n_p))
