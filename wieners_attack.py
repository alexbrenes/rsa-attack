from fractions import Fraction
N = 31572253668946223368340157100721987766746218463736824783505635131921053880398741320644875421329504217933416422336918416263408538952177986508994175591182768950207147336188432455124667514201867376909227788134941323555902495049233601287696456816385455907725032886562051454322468668214625612317109993078620529639774616518443677804391408891641903175536847686030211632523660782037213447088479131269565204282324663517421706048402910651099744974056786727812991192176997050739471403369421617160003772289048267809022469915924569385942569022178774225834165571053657200129401052764120020877313983409004932571630004656678491554033
e = 7084215194443599160339614321138928983214362269664400507990258691986234567347379532809700232256805715669899435125455589766395600413533503573822989102823878826540036317848245491834763460693299412011619210827311587500311657621439893147815582844814748650942186449787061150827753958225319378164169085724521950445516816392443392835946057362175733538556192411994505858592612662805711714449145899544166354660465794567570468563034819166109105798194936416549149864412218709017864526810122862155857826601574302659442260666643066114221374852104428425503135373985569499838251381802559047735816838596220653454921257900296590700089


def sqrt_l(N):
    x = N
    y = (x + N // x) // 2
    while(y < x):
        x = y
        y = (x + N // x) // 2
    return x


def continued_fraction(coefficients):
    if len(coefficients) == 1:
        return coefficients[0]
    return coefficients[0] + 1/continued_fraction(coefficients[1:])


def test_convergents(coefficients):
    fraction_value = continued_fraction(coefficients)
    fraction = Fraction(fraction_value).limit_denominator()
    k = fraction.numerator
    if k == 0:
        return -1, 0, 0
    d = fraction.denominator
    if d % 2 == 0:
        return -1, 0, 0
    if fraction == 1:
        return -1, 0, 0
    phi = (e * d - 1) // k
    if phi - phi % 1 != phi:
        return -1, 0, 0
    return phi, k, d


def find_phi(N, e):
    a = N
    b = e
    successive_convergents = []
    while True:
        c = b // a
        rem = b % a
        successive_convergents.append(c)
        phi, k, d = test_convergents(successive_convergents)
        if phi > 0:
            break
        b = a
        a = rem
    return phi, k, d


def quadratic_equation(N, e):
    phi, k, d = find_phi(N, e)
    b = -(N-phi+1)
    c = N
    a = 1
    x1 = (-b+sqrt_l(b*b-4*a*c))//2*a
    x2 = (-b-sqrt_l(b*b-4*a*c))//2*a
    return x1, x2, d


def wieners_attack(N, e):
    _, _, d = quadratic_equation(N, e)
    return d


def main():
    print(wieners_attack(N, e))


if __name__ == "__main__":
    main()
