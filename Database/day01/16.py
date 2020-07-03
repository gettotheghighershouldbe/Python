class Gun:

    def __init__(self,model):

        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):

        self.bullet_count += count

    def shoot(self):

        # 1.判断子弹数量
        if self.bullet_count <= 0:

            print("[%s] 子弹不够了，快装弹" % self.model)
            return

        # 2.发射子弹，-1
        self.bullet_count -= 1

        # 3.提示发射信息
        print("老子刚刚发射了一枚子弹，可还行")
        print("[%s] 突突突... [%d]" % (self.model,self.bullet_count))


class Soldier:

    def __init__(self,name):

        # 1.姓名
        self.name = name

        # 2.枪 - 新兵没有枪
        self.gun = None

    def fire(self):

        # 1.判断士兵是否有枪
        if self.gun == None:
            print("%s 没有枪，我要去拿枪" % self.name)
            return

        # 2.高喊口号
        print("兄弟们，都是有枪的人，亮出家伙%s来" % self.gun)

        # 3.让枪装填子弹
        self.gun.add_bullet(20)
        # 4.让枪发射子弹


# 1. 创建枪对象

ak47 = Gun("AK47")


# 2.创建许三多
xusanduo = Soldier("许三多")

xusanduo.gun = ak47

xusanduo.fire()

print(xusanduo.gun)



