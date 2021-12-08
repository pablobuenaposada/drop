from constants import MEAT, VEGETARIAN
from models import Curry, Customer, Proposals

c1 = Customer([Curry(id=1, type=MEAT), Curry(id=3, type=VEGETARIAN), Curry(id=5, type=VEGETARIAN)])
c2 = Customer([Curry(id=2, type=VEGETARIAN), Curry(id=3, type=MEAT), Curry(id=4, type=VEGETARIAN)])
c3 = Customer([Curry(id=5, type=MEAT)])

c4 = Customer([Curry(id=1, type=VEGETARIAN), Curry(id=2, type=MEAT)])
c5 = Customer([Curry(id=1, type=MEAT)])

c6 = Customer([Curry(id=2, type=MEAT)])
c7 = Customer([Curry(id=5, type=VEGETARIAN)])
c8 = Customer([Curry(id=1, type=VEGETARIAN)])
c9 = Customer([Curry(id=5, type=VEGETARIAN), Curry(id=1, type=VEGETARIAN), Curry(id=4, type=MEAT)])
c10 = Customer([Curry(id=3, type=VEGETARIAN)])
c11 = Customer([Curry(id=5, type=VEGETARIAN)])
c12 = Customer([Curry(id=3, type=VEGETARIAN), Curry(id=5, type=VEGETARIAN), Curry(id=1, type=VEGETARIAN)])
c13 = Customer([Curry(id=3, type=VEGETARIAN)])
c14 = Customer([Curry(id=2, type=MEAT)])
c15 = Customer([Curry(id=5, type=VEGETARIAN), Curry(id=1, type=VEGETARIAN)])
c16 = Customer([Curry(id=2, type=MEAT)])
c17 = Customer([Curry(id=5, type=VEGETARIAN)])
c18 = Customer([Curry(id=4, type=MEAT)])
c19 = Customer([Curry(id=5, type=VEGETARIAN), Curry(id=4, type=MEAT)])

c20 = Customer([Curry(id=1, type=VEGETARIAN)])
c21 = Customer([Curry(id=1, type=MEAT)])

c22 = c1 = Customer([Curry(id=1, type=VEGETARIAN), Curry(id=2, type=VEGETARIAN), Curry(id=3, type=MEAT)])
c23 = Customer([Curry(id=2, type=MEAT), Curry(id=2, type=VEGETARIAN), Curry(id=3, type=VEGETARIAN)])
c24 = c1 = Customer([Curry(id=1, type=MEAT), Curry(id=2, type=MEAT), Curry(id=3, type=VEGETARIAN)])


#print(Proposals(5, [c1, c2, c3]).main())
#print(Proposals(2, [c4, c5]).main())
#print(Proposals(5, [c6, c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19]).main())
#print(Proposals(1, [c20, c21]).main())
#print(Proposals(3, [c24, c23, c22]).main())


c50 = Customer([Curry(id=1, type=VEGETARIAN)])
c51 = Customer([Curry(id=1, type=VEGETARIAN), Curry(id=2, type=MEAT)])
c52 = Customer([Curry(id=1, type=VEGETARIAN), Curry(id=2, type=MEAT)])
print(Proposals(2, [c50, c51, c52]).main())
