#encoding:utf-8
#!/usr/bin/env python
import json

str = '''
*********************************************************************
*                欢迎使用电子科技大学Linux命令学习系统              *
*       本系统由电子科技大学生设计开发，旨在帮助使用者提高Linux命令 *
*    的使用熟练程度。本系统有固定难度和自动难度两种模式，敬请使用者 *
*    根据自身情况选择！                                             *
*     开发人员： 郝超鹏、 赵洋、 赵家玮、蔡文婷、贾唯、何止戈       *
*********************************************************************
'''
def main():
    print str
    while True:
        while(True):
            choice1 = raw_input("请选择开发模式 A(固定难度)、B（自动难度）、Q（退出）：")
            #print choice1
            if choice1 != "A" and choice1 != 'B' and choice1 != "Q":
                print "请输入正确选项！"
                continue
            elif choice1 == "A":
                while True:
                    choice2 = raw_input("请选择困难程度 A（简单）、B（复杂）、C（困难）、Q（退出）：")
                    if choice2 != "A" and choice2 != "B" and choice2 != "C" and choice2 != "Q":
                        print "请输入正确选项！"
                        continue
                    break
                if choice2 == "Q":
                    continue
                break
            else:
                choice2 = ' '
                break
        if choice1 =="A":
            right, result, user_result = choice_test(choice2)
            print_result(right, result, user_result)
        elif choice1 == "B":
            right1, right2, right3, num1, num2, num3, result, user_result = auto_test()
            print_autoresult(right1, right2, right3, num1, num2, num3,  result, user_result)
        else:
            break
    print "非常感谢你的使用，希望你下次再用！"


def choice_test(choice2):
    right = 0
    result = []
    user_result=[]
    question_dict  = load()
    if choice2 == "A":
        for  i in range(0, 30):
            while True:
                answer = raw_input(question_dict["questions"][i]["question"].encode('utf-8')+'\n'+"请输入答案:")
                #print i
                if answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D':
                    break
                else:
                    print "请输入正确选项！"
            if answer == question_dict["questions"][i]["answer"]:
                right += 1
            result.append(question_dict["questions"][i]["answer"])
            user_result.append(answer)
    elif choice2 == "B":
        for  i in range(30, 60):
            while True:
                answer = raw_input(question_dict["questions"][i]["question"].encode('utf-8')+'\n'+"请输入答案:")
                #print i
                if answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D':
                    break
                else:
                    print "请输入正确选项！"
            if answer == question_dict["questions"][i]["answer"]:
                right += 1
            result.append(question_dict["questions"][i]["answer"])
            user_result.append(answer)
    else:
        for  i in range(60, 90):
            while True:
                answer = raw_input(question_dict["questions"][i]["question"].encode('utf-8')+'\n'+"请输入答案:")
                #print i
                if answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D':
                    break
                else:
                    print "请输入正确选项！"   
            if answer == question_dict["questions"][i]["answer"]:
                right += 1
            result.append(question_dict["questions"][i]["answer"])
            user_result.append(answer)

    return right, result, user_result     


def auto_test():
    right1 = 0
    right2 = 0
    right3 = 0
    num1 = 0
    num2 = 0
    num3 = 0
    result = []
    user_result=[]
    question_dict  = load()
    j = 0
    k = 30
    while k>0:
        while True:
            answer = raw_input(question_dict["questions"][j]["question"].encode('utf-8')+'\n'+"请输入答案:")
            print j
            if answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D':
                break
            else:
                print "请输入正确选项！"
        if j<30:
            num1 += 1
        elif  29<j and j<60:
            num2 +=1
        else:
            num3 +=1
        if answer == question_dict["questions"][j]["answer"]:
            if j<30:
                right1 += 1
            elif  29<j and j<60:
                right2 +=1
            else:
                right3 +=1
            result.append(question_dict["questions"][j]["answer"])
            user_result.append(answer)
            if j<59:
                j += 31
            else:
                j += 1
        else:
            result.append(question_dict["questions"][j]["answer"])
            user_result.append(answer)
            if j>29:
                j -=29 
            else:
                j += 1
        k -= 1
    return right1, right2, right3, num1, num2, num3, result, user_result

def load():
    with open('data.json', "r+") as json_file:
        data = json.load(json_file,  strict=False)
        return data


def print_result(right, result, user_result):
    print len(result)
    print len(user_result)
    print '*********************************************************************'
    print '*                                                                   *'
    print '*     正确率： %d/30                                                *' %(right)
    print '*     正确答案 ：'+print_list(result).encode("utf-8") +'                     *'
    print '*     你的答案 ：'+print_list(user_result).encode("utf-8") +'                     *'
    print '*********************************************************************'


def print_autoresult(right1, right2, right3, num1, num2, num3, result, user_result):
    print len(result)
    print len(user_result)
    print '*********************************************************************'
    print '*                                                                   *'
    print '*     简单题正确率： %2d/%2d                                          *' %(right1, num1)
    print '*     复杂题正确率： %2d/%2d                                          *' %(right2, num2)
    print '*     困难题正确率： %2d/%2d                                          *' %(right3, num3)
    print '*     正确答案 ：'+print_list(result).encode("utf-8") +'                     *'
    print '*     你的答案 ：'+print_list(user_result).encode("utf-8") +'                     *'
    print '*********************************************************************'


def print_list(result):
    str = ''
    for i in result:
        str += i
    return str


if __name__ == '__main__':
    main()
