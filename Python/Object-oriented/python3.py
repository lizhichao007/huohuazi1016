# 多态
# class User:
#     def __init__(self,name):
#         self.name = name 
#     def printUser(self):
#         print('hello' + self.name)

# class UserVip(User):
#     def printUser(self):
#         print('hello! 尊敬的VIP客户:' + self.name)

# class UserGeneral(User):
#     def printUser(self):
#         print('hello, 尊敬的用户：'+ self.name)

# def printUserInfo(user):
#     user.printUser()

# if __name__ == '__main__':
#     uservip = UserVip('huohuazi1016')
#     uservip.printUser()
#     printUserInfo(uservip)
#     usergeneral = UserGeneral('火华子')
#     usergeneral.printUser()
#     printUserInfo(usergeneral)

# 类属性的访问控制
class UserInfo(object):
    def __init__(self,name,age,account):
        self.name = name
        self.age = age
        self.__account = account 
    def get_account(self):
        return self.__account
if __name__ == '__main__':
    userinfo = UserInfo('huohuazi1016',2,123456)
    print(dir(userinfo))
    print(userinfo.__dict__)
    print(userinfo.get_account())
    print(userinfo._UserInfo__account)
    