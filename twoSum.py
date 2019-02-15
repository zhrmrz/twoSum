class Sol:
    def __init__(self,goal,list):
        self.goal=goal
        self.list=list
    def find_goal(self):
        answers=[]
        list.sort()
        left,right=0,len(list)-1
        while(right>left):
            f = list[left]
            l = list[right]
            result=f+l
            if(result<self.goal):
                left+=1
            elif(result>self.goal):
                right-=1
            else:
                answers.append([f,l])
                left += 1
                right -= 1
        return answers
if __name__ == '__main__':
    goal=5
    list=[1,2,6,4,5,3]
    p1=Sol(goal,list)
    print(p1.find_goal())
