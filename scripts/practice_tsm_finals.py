"""TSM cumulative practice forms: six institutional families, four supplements."""
from build_practice_tests import *

def final(course,v):
    k=v+3
    if course=='TSM 098':
        prod=((v+3)*x-4)*(x+v+3);dist=-(v+2)*x**(v+1)*(2*x*x-(v+3)*x+4)
        p=(v+2)*x*x+3*x-4;q=-x*x-(v+4)*x+2
        l=(v+2)*x-3;r=-x+(v+5)+2*x;roots,_=solved('I098-4',l,r)
        if v==1:exc=[f'3(x+{k})-2 = 3x+{3*k-2}'];exans='All real numbers; both sides agree after distribution.'
        else:exc=[f'2(x-{k})+7 = 2x+{8-2*k}'];exans='No solution; the constants differ by 1 after distribution.'
        fl=(x+k)/3+x/4;fr=S.Integer(v+2);fs,_=solved('I098-6',fl,fr)
        out=[question('I098-1','Multiply and simplify.',[par((v+3)*x-4)+par(x+v+3)],[ans('Polynomial',tex(exact('I098-1',prod)),10)]),
          question('I098-2','Distribute and simplify.',[f'-{v+2}x^{v+1}'+par(2*x*x-(v+3)*x+4)],[ans('Polynomial',tex(exact('I098-2',dist)),10)]),
          question('I098-3','Add and combine like terms.',[par(p)+' + '+par(q)],[ans('Polynomial',tex(exact('I098-3',p+q)),10)]),
          question('I098-4','Solve and check.',[f'{v+2}x-3 = -x+{v+5}+2x'],[ans('Solution',solution_tex(roots),10)]),
          question('I098-5','Solve and state the complete solution set.',exc,[ans('Solution set',exans,10,True)]),
          question('I098-6','Solve and check in the original equation.',[frac(x+k,3)+' + '+frac(x,4)+' = '+tex(fr)],[ans('Solution',solution_tex(fs),10)])]
        ev=3*x-(v+2)*y+1;px=-k;py=v+1
        a,b,c,d=[(1,4,1,6),(2,9,1,6),(1,8,1,12)][v];val=S.Rational(a,b)+S.Rational(c,d)
        sp,sq=k,v+1;sb=sq-2*sp;pp=2*x*x-(v+1)*x+3;qq=x*x+(v+2)*x-4
        out += [question('S098-eval',f'Evaluate at x = {px}, y = {py}. Show substitution.',[tex(ev)],[ans('Value',tex(exact('S098-eval',ev.subs({x:px,y:py}))),10)]),
          question('S098-fraction','Add and reduce to lowest terms.',[frac(a,b)+' + '+frac(c,d)],[ans('Fraction',tex(val),10)]),
          question('S098-system','Solve by substitution or elimination; check both equations.',[eq(y,2*x+sb),eq(x+y,sp+sq)],[ans('Ordered pair',tex(S.Tuple(sp,sq)),10)]),
          question('S098-sub','Subtract; show distribution of the negative and combine like terms.',[par(pp)+' - '+par(qq)],[ans('Polynomial',tex(exact('S098-sub',pp-qq)),10)])]
    else:
        factors=[(3*x+2)*(2*x-3),(2*x-3)*(5*x+2),(3*x-1)*(4*x+3)][v];fp=S.expand(factors)
        a=v+2;b=v+5;c=v+7;rn=x*x-a*a;rd=S.expand((x+b)*(x-c));sd=x*x+a*x;mult=rn/rd*(x+b)/sd
        ad1=x*x-a*x;ad2=x*x-a*a;addition=2/ad1+3/ad2
        qp=S.expand((x-(v+2))*(x+v+4));qr,_=solved('I099-4',qp)
        nq=(v+2)*x*x+x-(v+4);nr,_=solved('I099-5',nq);assert not S.sqrt(S.Poly(nq,x).discriminant()).is_integer
        h=v+3;num=2*(v+4);z=v+6;l=num/(2*x-2*h)+2/(x-h);rr=S.Rational(v+6,z-h);roots,_=solved('I099-6',l,rr,[z],[x-h])
        out=[question('I099-1','Factor completely.',[tex(fp)],[ans('Factors',tex(S.factor(fp)),10)]),
          question('I099-2','Multiply and simplify.',[frac(rn,rd)+r'\times'+frac(x+b,sd)],[ans('Expression',tex(S.factor(exact('I099-2',mult))),10)]),
          question('I099-3','Add and simplify.',[frac(2,ad1)+' + '+frac(3,ad2)],[ans('Expression',tex(S.factor(exact('I099-3',addition))),10)]),
          question('I099-4','Solve by factoring.',[eq(x*x+2*x,(v+2)*(v+4))],[ans('Solutions',solution_tex(qr),10)]),
          question('I099-5','Solve using the quadratic formula. Give exact simplified solutions.',[eq((v+2)*x*x,-x+(v+4))],[ans('Solutions',solution_tex(nr),10)]),
          question('I099-6','Solve and check in the original equation.',[frac(num,2*x-2*h)+' + '+frac(2,x-h)+' = '+tex(rr)],[ans('Solution/check',solution_tex(roots),10)])]
        fm=S.Rational(v+1,2);fb=v-2;pt1=(2,2*fm+fb);pt2=(4,4*fm+fb)
        A,B,C=[(2,1,6),(1,2,8),(3,2,12)][v];ev=(v+2)*(x-v-1)*(x+3);inp=-2;sh=v+1;sk=v+3
        out += [question('S099-line','Find the slope-intercept equation through these two points.',[tex(S.Tuple(*pt1))+r';\ '+tex(S.Tuple(*pt2))],[ans('Equation',eq(y,fm*x+fb),10)]),
          question('S099-graph','Find the intercepts and graph the line on the grid.',[eq(A*x+B*y,C)],[ans('Intercepts',tex(S.Tuple(S.Rational(C,A),0))+r';\ '+tex(S.Tuple(0,S.Rational(C,B))),4),ans('Graph (booklet)',eq(y,-S.Rational(A,B)*x+S.Rational(C,B)),6)],graph={'kind':'blank','answer_lines':[[-A/B,C/B]]}),
          question('S099-eval',f'Evaluate at x = {inp}; show substitution.',[tex(ev)],[ans('Value',tex(exact('S099-eval',ev.subs(x,inp))),10)]),
          question('S099-sqrt','Solve by taking square roots.',[f'3(x-{sh})^2 = {3*sk*sk}'],[ans('Solutions',solution_tex([sh-sk,sh+sk]),10)])]
    assert len(out)==10 and sum(q['id'].startswith('I') for q in out)==6
    for q in out:
        if q['id'].startswith('I'):q['archetype']=['A','B','C'][v];q['institutional_slo']=1 if int(q['id'][-1])<=3 else 2
    return out
