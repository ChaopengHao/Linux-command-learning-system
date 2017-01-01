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
    while(True):
        choice1 = raw_input("请选择开发模式 a(固定难度)、b（自动难度）：")
        print choice1
        if choice1 != "a" and choice1 != 'b' :
            continue
        elif choice1 == "a":
            choice2 = raw_input("请选择困难程度 a（简单）、b（复杂）、c（困难）：")
            print choice2
            break
        else:
            choice2 = ' '
            break
    result = test(choice1, choice2)
    print result

def test(choice1,  choice2):
          file = "question.json"
          fb = open(file, 'r')
          question_dict = json.dumps(fb.read())
          print question_dict
          return "good"     





if __name__ == '__main__':
    main()
