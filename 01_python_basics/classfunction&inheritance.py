class Chef:
    def make_chicken(self):
        print("The chef makes chicken")

    def make_protein_rich_meal(self):
        print("The chef makes protein rich meal")

    def make_salad(self):
        print("The chef makes salad")


class JunkChef(Chef):
    def make_chicken(self):
        print("The chef makes chicken with oil")

    def make_burger(self):
        print ("The chef makes unhealthy burger")


food1=Chef()
food1.make_protein_rich_meal()
food1.make_chicken()

food2= JunkChef()
food2.make_chicken()
food2.make_burger()


