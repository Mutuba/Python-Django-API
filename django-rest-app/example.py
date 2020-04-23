# class Spotify_User:
#     def __init__(self, **user_attributes):
#         self.name = user_attributes.pop('name')
#         self.email = user_attributes.pop('email')
#         self.premium = user_attributes.pop('premium')

#     def isPremium(self):
#         if self.premium:
#             # print("{} is a Premium User".format(self.name))
#             print(f'{self.name} is a premium user')
#         else:
#             print(f'{self.name} is not a premium user')
#             # print("{} is not a Premium User".format(self.name))


# # passing attributes as a dictionary to allow passing of attributes
# # in any order
# user1 = Spotify_User(name='Sarah Phillips',
#                      email='sphillips@gmail.com', premium=True)
# print(user1.isPremium())


from enum import IntEnum


class CustomerTypes(IntEnum):
    PROSPECT = 1
    LEAD = 2
    CUSTOMER = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
