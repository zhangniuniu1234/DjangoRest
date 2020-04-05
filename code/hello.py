def learn(name,course=None):
    if not (isinstance(course,list)):
        course=[]



    course.append(name)
    print(course)

if __name__=="__main__":
    learn("jack")
    learn("xiao")

