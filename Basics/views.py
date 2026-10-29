from django.shortcuts import render
def Sum(request):
    if request.method=='POST':
        num1=int( request.POST.get('num1'))
        num2=int( request.POST.get('num2'))
        sum=num1+num2
        return render(request,'Basics/Sum.html',{'result':sum})
    else:
        return render(request,'Basics/Sum.html')

def Calculator(request):
    if request.method=='POST':
        num1=int(request.POST.get('num1'))
        num2=int(request.POST.get('num2'))
        btn=request.POST.get("btn_submit")
        if btn=='+':
            result=num1+num2
        
        elif btn=='-':
            result=num1-num2
        
        elif btn=='*':
            result=num1*num2
        
        elif btn=='/':
            result=num1/num2

        return render(request,'Basics/Calculator.html',{'result':result})
    else:
        return render(request,'Basics/Calculator.html')
    
def LargestThree(request):
    if request.method=='POST':
        num_1=int(request.POST.get('num_1'))
        num_2=int(request.POST.get('num_2'))
       
        if num_1>num_2:
            result=num_1
        else:
            result=num_2
        return render(request,'Basics/LargestThree.html',{'result':result})
    else:
        return render(request,'Basics/LargestThree.html')

def Largest(request):
    if request.method=='POST':
        num1=int(request.POST.get('num1')) 
        num2=int(request.POST.get('num2')) 
        num3=int(request.POST.get('num3')) 
        if num1>num2 and num1>num3:
            result=num1
        elif num2>num1 and num2>num3:
            result=num2
        else:
            result=num3    
        return render(request,'Basics/Largest3.html',{'result':result})
    else:
        return render(request,'Basics/Largest.html')

def RankList(request):
    if request.method=='POST':
        fname=request.POST.get('txt_fname')
        lname=request.POST.get('txt_lname')
        rollno=request.POST.get('txt_rollno')
        dep=request.POST.get('sel_dep')
        sem=request.POST.get('sel_sem')
        num_mar1=int(request.POST.get('num_mar1'))
        num_mar2=int(request.POST.get('num_mar2'))
        num_mar3=int(request.POST.get('num_mar3'))
        fullname=fname+" "+lname
        t_mark=num_mar1+num_mar2+num_mar3
        if t_mark >=90:
            grade='A+'
        elif t_mark>=80:
            grade='A'
        elif t_mark>=70:
            grade='B+'
        elif t_mark>=60:
            grade='B'
        elif t_mark>=50:
            grade='C+'
        elif t_mark>=40:
            grade='C'
        else:
            grade='fail' 
        return render(request,'Basics/RankList.html',{
            'fullname':fullname,
           'rollno':rollno,
           'dep':dep,'sem':sem,
           't_mark':t_mark,
           'grade':grade})
        
         
    else:
        return render(request,'Basics/RankList.html')
        

def SalaryCalculation(request):
    if request.method=='POST':
        fname=request.POST.get('txt_fname')
        lname=request.POST.get('txt_lname')
        gender=request.POST.get('rd_gen')
        martial=request.POST.get('rd_mar')
        dep=request.POST.get('sel_dep')
        salary=int(request.POST.get('num_sal'))
        fullname=fname+" "+lname

        if salary>=10000:
            TA=salary*.4
            DA=salary*.35
            HRA=salary*.3
            LIC=salary*.25
            PF=salary*.2
        elif salary>=5000 and salary<=10000:
            TA=salary*.35
            DA=salary*.30
            HRA=salary*.25
            LIC=salary*.2
            PF=salary*.15
        elif salary<5000:
            TA=salary*.25
            DA=salary*.25
            HRA=salary*.2
            LIC=salary*.15
            PF=salary*.10
    
        DEDUCTION=LIC+PF
        NET=salary+TA+DA+HRA-(LIC+PF)


        return render(request,'Basics/SalaryCalculation.html',{
            'fullname':fullname,
            'gender':gender,
            'martial':martial,'department':dep,
            'salary':salary,
            'TA':TA,
            'DA':DA,
            'HRA':HRA,
            'LIC':LIC,
            'PF':PF,
            'DEDUCTION':DEDUCTION,
            'NET':NET,})
        
         
    else:
        return render(request,'Basics/SalaryCalculation.html')




