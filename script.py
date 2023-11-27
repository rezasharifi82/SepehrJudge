#In The Name Of God
# Sharifi Mohammadreza

from collections import deque
import subprocess
import sys,os,importlib,json


def reshaper(filee):  #Reshape the string due to string sensitivity of matching
    o=[]
    for j in filee:
        if(j.strip() != ""):
            o.append(j.strip())
    return o



def check_student_source(Student_src): #Check if the student source is a valid file
    try: 
        i=open(Student_src,"r")
        i.close()
    except Exception as e:
        print(e)
        raise Exception("Internal Error #1206: Student Source file not found!")
    


def judge(student_ouput,correct_out): #Main function that check if the answer is correct or not
    if(len(student_ouput) != len(correct_out)):
        return False
    else:
        for i in range(len(correct_out)):
            if(str(correct_out[i]).strip() == str(student_ouput[i]).strip()):
                continue
            else:
                return False      
    return True



def run_py(testNo:int,Student_src:str): #Python interpreter function: which can return the result of that test
    try:
        Correct_out=open("./output/output{}.txt".format(testNo),"r")
        inn="./input/input{}.txt".format(testNo)
        Correct_out=reshaper(Correct_out.readlines())
        # inn=reshaper(inn.readlines())
        command='python {} < {}'.format(Student_src,inn)
        p = os.popen(command)
        Student_output=p.read()
        Student_output=reshaper([Student_output])
        point=judge(Student_output,Correct_out)
        return ((testNo,point))


    except Exception as e:
        print(e)
        print("###########################")
        raise Exception ("Internal Error #2237: test file not found")
    


def run_java(testNo:int,Student_src:str): #java interpreter function : which can return the result of that test
    try:
        Correct_out=open("./output/output{}.txt".format(testNo),"r")
        inn="./input/input{}.txt".format(testNo)
        Correct_out=reshaper(Correct_out.readlines())
        name_of=Student_src[:-5]
        # inn=reshaper(inn.readlines())
        os.system("javac {}".format(Student_src))
        command='java {} < {}'.format(name_of,inn)
        p = os.popen(command)
        Student_output=p.read()
        Student_output=reshaper([Student_output])
        point=judge(Student_output,Correct_out)
        return ((testNo,point))


    except Exception as e:
        print(e)
        print("###########################")
        raise Exception ("Internal Error #7801: test file not found")
    
def run_cpp(testNo:int,Student_src:str):   #cpp compiler function : which can return the result of that test
    try:
        Correct_out=open("./output/output{}.txt".format(testNo),"r")
        inn="./input/input{}.txt".format(testNo)
        Correct_out=reshaper(Correct_out.readlines())
        name_of=Student_src[:-4]
        # inn=reshaper(inn.readlines())
        os.system("g++ {} -o res".format(Student_src))
        command='./res < {}'.format(inn)
        p = os.popen(command)
        Student_output=p.read()
        Student_output=reshaper([Student_output])
        point=judge(Student_output,Correct_out)
        return ((testNo,point))


    except Exception as e:
        print(e)
        print("###########################")
        raise Exception ("Internal Error #3217: test file not found")
    
def runner(Student_src,Inputs): #Primary function that can realise the format of source and report the final result
    try:
        check_student_source(Student_src=Student_src)
        point=[]
        summi=0
        size_test=len(Inputs)
        if (str(Student_src).endswith(".py")):
            for i in range(size_test):
                x=run_py(i+1,Student_src=Student_src)
                point.append(x)
                if(x[-1]==True):
                    summi+=1
        elif(str(Student_src).endswith(".java")):
            for i in range(size_test):
                x=run_java(i+1,Student_src=Student_src)
                point.append(x)
                if(x[-1]==True):
                    summi+=1
        elif(str(Student_src).endswith(".cpp")):
            for i in range(size_test):
                x=run_cpp(i+1,Student_src=Student_src)
                point.append(x)
                if(x[-1]==True):
                    summi+=1
        else:
            raise Exception("Language Not Supported! #1100")
        
        point.append((summi*100)//len(point))
        return point
            
    except:
        raise Exception("Internal Error #1007: runner!")

def save_json(result:list): #Save result to json
    testNo=len(result)-1
    ans={"point":int((result[-1]//testNo)*100)}
    ress={"Test {}".format(x[0]):x[-1] for x in result[:-1]}
    ans.update({"Tests_result":ress})
    i=open("result.json","w")
    i.write(json.dumps(ans))
    return ans

def save_text(result:list): # save result as text
    testNo=len(result)-1
    ans="point = {}".format((result[-1]//testNo)*100)
    ress={"Test {}".format(x[0]):x[-1] for x in result[:-1]}
    i=open("result.txt","w+")
    i.write(ans)
    i.write("\n")
    i.write(str(ress))
    i.close()

def saver(result:list): #Save the reports
    save_json(result=result)
    save_text(result=result)
#--------------------------------------------------------------------------------------------------------------------
#Define number of tests
a=os.listdir("./input")
b=os.listdir("./output")

# Check the logical hypothesis 
if (len(a)!= len(b)):
    raise Exception("Internal Error #1102: Unequality at the number of inputs and outputs!")

Student_src=sys.argv[-1]

x=runner(Student_src=Student_src,Inputs=a)
saver(x)
print(x)

