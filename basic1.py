import turtle as t     # 导入turtle库

#t.mode('logo')        # 切换成Logo坐标、角度系统
t.shape('turtle')    #箭头转变为小乌龟

t.pendown()            # 落笔
#t.forward(300)         # 划过300个单位的长度
# 效果：向右300个单位
t.left(90)             # 左转90度
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)   # 笔端向右，图形未变
t.penup()              # 抬笔

t.pendown()
for j in range(4):    # 重复执行4次，是上述的简化版，引入了循环
    t.forward(100)
    t.left(90)
t.penup()

# 以下为阶梯
t.pendown()
t.forward(50)
t.left(90)             # 左转90度
t.forward(50)
t.right(90)            # 右转90度
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)            # 右转90度
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)            # 右转90度
t.penup()

t.pendown()
for j in range(3):         # 重复执行3次
    t.forward(50)
    t.left(90)             # 左转90度
    t.forward(50)
    t.right(90)            # 右转90度
t.penup()

t.done()
