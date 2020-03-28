
# def walkout():
#     print('Bye Felicia')


# def debug_transformer(fun):
#     def wrapper():
#         print(f'Function `{fun.__name__}` called')
#         fun()
#         print(f'Function `{fun.__name__}` finished')

#     return wrapper


# walkout = debug_transformer(walkout)
# walkout()



# def debug_transformer(fun):
#     def wrapper(*args, **kwargs):
#         print(f'Function `{fun.__name__}` called')
#         res = fun(*args, **kwargs)
#         print(f'Function `{fun.__name__}` finished')
#         return res
#     return wrapper


# @debug_transformer
# def walkout(name):
#     # print(f'Bye {name}')
#     return f'Bye {name}'


# value = walkout('Bob')
# print(value)


Django polymorphic r/ships(m2m)

# from polymorphic.models import PolymorphicModelclass Driver(PolymorphicModel):
pass


class Owner(Driver):

    # ...
    name = models.CharField(max_length=255)


class Valet(Driver):

    # ...
    name = models.CharField(max_length=255)


class Car(models.Model):

    # ...

    name = models.CharField(max_length=255)
    drivers = models.ManyToManyField(
        Driver,
        related_name='cars'
    )
# One to many r/ship

from polymorphic.models import PolymorphicModelclass Buyer(PolymorphicModel):
    pass

class Woman(Buyer):

    # ...
    name = models.CharField(max_length=255)



class Man(Buyer):

    # ...
    name = models.CharField(max_length=255)



class Car(models.Model):

    # Fields

    name = models.CharField(max_length=255)
    buyer = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE,
        related_name='cars'
    )
