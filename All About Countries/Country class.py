class Indonesia():
    def capital(self):
        print("The capital of Indonesia is Jakarta")
    def language(self):
        print("Bahasa Indonesia is the official language of Indonesia.")
    def type(self):
        print("Indonesia is a presidential republic.")

class America():
    def capital(self):
        print("The capital of the USA is Washington D.C.")
    def language(self):
        print("English is the official language of the USA.")
    def type(self):
        print("The USA is a presidential republic.")


i=Indonesia()
u=America()

for country in (i,u):
    country.capital()
    country.language()
    country.type()

