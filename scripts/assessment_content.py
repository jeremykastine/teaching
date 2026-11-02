"""Fresh, bounded assessment parameters with symbolic verification."""
import random, math
from functools import reduce
import build_practice_tests as T
S=T.S;x=T.x;y=T.y

def institutional(course,seed,archetype):
    r=random.Random(seed);n=lambda a=1,b=6:r.randint(a,b);kind=archetype%4;letter='ABCD'[kind]
    def q(fid,prompt,maths,answer,plain=False):
        z=T.question(fid,prompt,maths,[T.ans('',answer,10,plain)])
        z.update(archetype=letter,institutional_slo=1 if int(fid[-1])<=3 else 2)
        return z
    out=[]
    if course=='TSM 098':
        a,c=n(2,4),1 if kind<2 else n(2,4);b,d=n(1,6),n(1,6)
        if kind in [0,3]:b=-b
        else:d=-d
        if a*d+b*c==0:d+=1
        p=(a*x+b)*(c*x+d);out.append(q('I098-1','Multiply and simplify.',[T.par(a*x+b)+T.par(c*x+d)],T.tex(S.expand(p))))
        a=(-1 if kind in [1,3] else 1)*n(2,5);e=n(1,4);inside=n(1,3)*x**(3 if kind>1 else 2)+(-1 if kind%2==0 else 1)*n(1,5)*x**(2 if kind==3 else 1)+n(1,6)*(-1 if kind==1 else 1)
        p=a*x**e*inside;out.append(q('I098-2','Distribute and simplify.',[T.tex(a*x**e)+T.par(inside)],T.tex(S.expand(p))))
        if kind==0:p=n(2,6)*x*x+n(1,6)*x-n();z=-x*x-n(2,7)*x-n()
        elif kind==1:p=n(2,5)*x**3-n()*x*x+n()*x-n();z=n(1,4)*x*x-x+n()
        elif kind==2:p=n(2,5)*x**4+n()*x*x-n();z=-x**4+n()*x-n()
        else:p=n(3,6)*x**3-x+n();z=-n(1,2)*x**3+n()*x*x-n()
        out.append(q('I098-3','Add and simplify.',[T.par(p)+' + '+T.par(z)],T.tex(S.expand(p+z))))
        while True:
            a,b,c,d,e=n(2,7),n(-8,8),-n(1,4),n(-8,8),n(1,3)
            if a-c-e==0:continue
            root=S.Rational(d-b,a-c-e)
            if root and abs(root.p)<=20 and root.q<=8:break
        out.append(q('I098-4','Solve.',[T.tex(a*x+b)+' = '+T.tex(c*x)+' '+('+' if d>=0 else '-')+' '+str(abs(d))+' + '+T.tex(e*x)],T.solution_tex([root])))
        a,h,b=n(2,5),n(1,6),n(-6,6);same=kind in [1,2];rhs=a*x-a*h+b+(0 if same else n(1,3))
        lhs=f'{a}(x-{h})'+(f'+{b}' if b>=0 else str(b))
        out.append(q('I098-5','Solve and state the complete solution set.',[lhs+' = '+T.tex(rhs)],'All real numbers' if same else 'No solution',True))
        while True:
            h=n(1,7);a=n(1,4)
            if kind==0:ll=S.Rational(2,3)*x+S.Rational(h,2);rr=(a*x-n(1,6))/9
            elif kind==1:ll=x/4+S.Rational(h,3);rr=(3*x+a)/6
            elif kind==2:ll=(3*x-h)/5-x/2;rr=S.Rational(a,10)
            else:ll=(2*x+h)/6+x/4;rr=S.Rational(a,2)
            roots,_=T.solved('I098-6',ll,rr)
            if len(roots)==1 and abs(roots[0].p)<=40 and roots[0].q<=12:break
        out.append(q('I098-6','Solve.',[T.eq(ll,rr)],T.solution_tex(roots)))
    else:
        while True:
            a,c=n(2,5),n(2,5);b,d=n(1,5),n(1,5)
            if kind in [0,2]:b,d=-b,-d
            elif kind==1:d=-d
            else:b=-b
            p=S.expand((a*x+b)*(c*x+d));co=S.Poly(p,x).all_coeffs()
            if reduce(math.gcd,map(int,co))==1 and co[1] and S.discriminant(p,x)>0:break
        out.append(q('I099-1','Factor completely.',[T.tex(p)],T.tex(S.factor(p))))
        a,b,c=n(2,6),n(7,9),n(2,5)
        if kind==0:pieces=[x*x-a*a,S.expand((x+b)*(x-c)),x+b,x*x+a*x]
        elif kind==1:pieces=[x*x-a*a,S.expand((x-a)*(x+b)),x-a,S.expand((x+a)*(x+b))]
        elif kind==2:pieces=[x*x-a*a,S.expand((x+a)*(x-b)),x-b,x*x-a*x]
        else:pieces=[c*(x*x-a*a),S.expand((x-a)*(x-b)),x-b,x*x+a*x]
        A,B,C,D=pieces;expr=A/B*C/D
        out.append(q('I099-2','Multiply and simplify.',[T.frac(A,B)+r'\times'+T.frac(C,D)],T.tex(S.factor(S.cancel(expr)))))
        while True:
            a,b,c,d=n(1,5),n(1,5),n(1,5),n(1,5)
            if kind==0:den1=x*x-a*x;den2=x*x-a*a
            elif kind==1:den1=x*x+(a+1)*x;den2=S.expand((x+a)*(x+a+1))
            elif kind==2:den1=x*x-a*a;den2=S.expand((x-a)*(x+a+1))
            else:den1=x*x-a*x;den2=S.expand((x-a)**2)
            combined=c/den1+d/den2;rawnum=c*den2+d*den1
            reduced=S.cancel(combined);num,den=S.fraction(reduced)
            lcd=S.lcm(den1,den2)
            if S.degree(den,x)==S.degree(lcd,x):break
        out.append(q('I099-3','Add and simplify.',[T.frac(c,den1)+' + '+T.frac(d,den2)],T.tex(S.factor(reduced))))
        a,b=n(1,7),n(1,7)
        if kind in [0,1]:roots=[-a,-(b+1)]
        elif kind==2:roots=[a,-b]
        else:roots=[a,a+b]
        if roots[0]==roots[1]:roots[1]-=1
        p=S.expand((x-roots[0])*(x-roots[1]));co=S.Poly(p,x).all_coeffs()
        expression=T.eq(x*x,-co[1]*x-co[2]) if kind==0 else T.eq(x*x+co[1]*x,-co[2])
        out.append(q('I099-4','Solve.',[expression],T.solution_tex(roots)))
        while True:
            a,b,c=n(2,7),n(-6,6),-n(1,7);disc=b*b-4*a*c
            if b and math.isqrt(disc)**2!=disc:break
        p=a*x*x+b*x+c;roots,_=T.solved('I099-5',p)
        out.append(q('I099-5','Solve. Give exact simplified solutions.',[T.eq(a*x*x,-b*x-c)],T.solution_tex(roots)))
        h=n(-4,5);m=n(2,4);A=m*n(3,10);b=(-1 if kind==2 else 1)*n(1,3);z=h+n(2,5)
        A=A+m if A//m+b==0 else A
        rhs=S.Rational(A//m+b,z-h);lhs=A/(m*x-m*h)+b/(x-h);roots,_=T.solved('I099-6',lhs,rhs,[z],[x-h])
        op=' + ' if b>0 else ' - '
        out.append(q('I099-6','Solve.',[T.frac(A,m*x-m*h)+op+T.frac(abs(b),x-h)+' = '+T.tex(rhs)],T.solution_tex(roots)))
    return out

def math101_solving(v,seed):
    r=random.Random(seed);h=r.randint(1,5);base=r.choice([2,3,4]);category=v%4;subtype=(v//4)%2
    if category==0:
        if subtype==0:
            lhs=S.sqrt(x+h);rhs=x-h;roots=S.solve(lhs-rhs,x);expr=T.eq(lhs,rhs)
        else:
            d=r.randint(3,6);k=r.randint(1,d-1);lhs=S.sqrt((x-h)**2+d*d-k*k);rhs=d;roots=[h-k,h+k];expr=T.eq(lhs,rhs)
        assert all(S.simplify(lhs.subs(x,z)-rhs.subs(x,z) if hasattr(rhs,'subs') else lhs.subs(x,z)-rhs)==0 for z in roots)
        kind='radical'
    elif category==1:
        a,b=r.randint(1,5),r.randint(1,5);root=3*a+2*b;expr=rf'8^{{x-{a}}}=4^{{x+{b}}}';roots=[root];kind='exponential'
        assert 3*(root-a)==2*(root+b)
    elif category==2:
        sub=v//4%3
        if sub==0:
            c=r.randint(2,5);expr=rf'\log_{{{base}}}(x-{h})+\log_{{{base}}}({c})=2';roots=[h+S.Rational(base*base,c)]
        elif sub==1:
            c=r.randint(1,4);expr=rf'\log_{{{base}}}(x-{h})-\log_{{{base}}}(x-{h+c})=1';roots=[h+S.Rational(base*c,base-1)]
        else:
            base=r.choice([2,3]);c=base*base-1;expr=rf'\log_{{{base}}}(x-{h})+\log_{{{base}}}(x-{h+c})=2';roots=[h+base*base]
        kind='logarithmic'
    else:
        if subtype==0:
            a=r.randint(1,4);p=x*x;line=a*x+2*a*a;rr=S.solve(p-line,x);pts=[S.Tuple(z,z*z) for z in rr];maths=[T.eq(y,p),T.eq(y,line)]
        else:
            k=r.randint(1,4);radius=1+(1+k)**2;pts=[S.Tuple(1,1+k),S.Tuple(-k-1,-1)];maths=[T.eq(x*x+y*y,radius),T.eq(y,x+k)]
        q=T.question('M101-solving','Solve the nonlinear system.',maths,[T.ans('',r';\ '.join(T.tex(p) for p in pts),10)]);q['category']='system';return q
    q=T.question('M101-solving','Solve exactly.',[expr],[T.ans('',T.solution_tex(roots),10)]);q['category']=kind;return q
