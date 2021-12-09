print('---Hello---')

# 简单的1+1计算：
a = 1
b = 2
print('计算结果等于：', 1+2)

# 用户名验证：
def denglu():
    yonghuming = 'wangjieni'
    mima = 'Python'

    yong_hu_ming = input('请输入您的用户名：')
    mi_ma = input('请输入您的密码：')

    if yong_hu_ming == yonghuming:
        if mi_ma == mima:
            print('登录成功！')
        else:
            print('您的密码错误！')
    else:
        print('请输入正确的用户名！')

if __name__ == '__main__':
    denglu()