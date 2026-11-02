"""Fresh practice forms parallel to the current TSM assessment specifications."""
import math
import random
import sympy as S
import build_practice_tests as T
from assessment_content import institutional

x, y = T.x, T.y

def expression(fid, prompt, expressions, answers=None, points=20):
    values = [S.cancel(S.expand(e)) for e in expressions]
    answers = values if answers is None else answers
    assert all(S.simplify(a-b) == 0 for a,b in zip(values,answers))
    labels = [''] if len(values)==1 else ['('+chr(97+i)+')' for i in range(len(values))]
    q=T.question(fid,prompt,[(lab+r'\quad ' if lab else '')+T.tex(e) for lab,e in zip(labels,expressions)],
        [T.ans(lab,T.tex(a),points//len(values)) for lab,a in zip(labels,answers)])
    q['verification']=[dict(kind='expression',input=str(e),answer=str(a)) for e,a in zip(expressions,answers)]
    return q

def solveq(fid, maths, lhs, rhs=0, denoms=(), points=20):
    roots,candidates=T.solved(fid,lhs,rhs,denoms=denoms)
    q=T.question(fid,'Solve. Give the complete solution set.',maths,
        [T.ans('',T.solution_tex(roots) if roots else 'No solution',points,not roots)])
    q['verification']=[dict(kind='equation',lhs=str(lhs),rhs=str(rhs),denominators=list(map(str,denoms)),
        candidates=list(map(str,candidates)),answers=list(map(str,roots)))]
    return q

def reduction(r,prefix):
    values=[]
    for g in [r.choice([2,3,5,7]),r.choice([6,10,14,15,21])]:
        a,b=r.choice([(2,3),(3,4),(3,5),(4,5),(4,7),(5,7),(5,8),(7,9)])
        assert math.gcd(a,b)==1
        values.append((a*g,b*g))
    r.shuffle(values)
    q=T.question(prefix+'-frac','Reduce each fraction to lowest terms.',
        [rf'({chr(97+i)})\quad '+T.frac(a,b) for i,(a,b) in enumerate(values)],
        [T.ans('('+chr(97+i)+')',T.tex(S.Rational(a,b)),10) for i,(a,b) in enumerate(values)])
    q['verification']=[dict(kind='expression',input=f'{a}/{b}',answer=str(S.Rational(a,b))) for a,b in values]
    assert sorted(len(S.factorint(math.gcd(a,b))) for a,b in values)==[1,2]
    return q

def evaluation(r,fid,points=20):
    a=r.choice([-4,-3,-2,2,3,4]);b=r.choice([-4,-3,-2,2,3,4]);c=r.choice([-5,-3,1,3,5])
    px=r.choice([-4,-3,-2]);py=r.randint(1,4);e=a*x+b*y+c;z=e.subs({x:px,y:py})
    q=T.question(fid,f'Evaluate at x = {px}, y = {py}.',[T.tex(e)],[T.ans('',T.tex(z),points)])
    q['verification']=[dict(kind='expression',input=str(e.subs({x:px,y:py})),answer=str(z))]
    return q

def comparison(r,prefix,i):
    k=r.randint(2,6);inputs=[r.randint(1,4),-r.randint(1,4),0]
    if prefix=='A98':
        lhs=(x-k)*(x+k);rhs=x*x-k*k+[0,x,r.randint(2,5)][i%3]
    else:
        a=r.randint(5,8);b=r.randint(5,8)
        lhs=(x*x-a*a)/(x-a)
        delta=[S.Integer(0),x,x-r.randint(9,12)][i%3]
        rhs=(S.expand((x+a+delta)*(x+b)))/(x+b)
        assert all(v not in [a,-b] for v in inputs)
    q=T.comparison(prefix+('-compare' if prefix=='A98' else '-test'),lhs,rhs,inputs,20)
    if prefix=='A99':
        q['math']=[T.frac(x*x-a*a,x-a)+' = '+T.frac(S.expand((x+a+delta)*(x+b)),x+b)]
    matches=[S.simplify(lhs.subs(x,z)-rhs.subs(x,z))==0 for z in inputs]
    assert sum(matches)==[3,1,0][i%3]
    q['verification']=[dict(kind='comparison',lhs=str(lhs),rhs=str(rhs),inputs=inputs,
        left=[str(lhs.subs(x,z)) for z in inputs],right=[str(rhs.subs(x,z)) for z in inputs])]
    return q

def arithmetic98(r,i):
    a,b=r.randint(4,12),r.randint(2,7)
    first=a if i%2==0 else -(a+b)
    comp=(r.randint(9,15),r.randint(2,7))
    if i%2==0:ct=f'-{comp[0]}+{comp[1]}';cv=-comp[0]+comp[1]
    else:ct=f'-{comp[0]}-{comp[1]}';cv=-comp[0]-comp[1]
    zero=(T.frac(a,0),'Undefined') if i%2==0 else (T.frac(0,a),'0')
    signed=(f'(-{a})({b})',str(-a*b)) if i%2==0 else (T.frac(-a*b,-b),str(a))
    tasks=[(f'{first}-(-{b})',str(first+b)),signed,(ct,str(cv)),zero];r.shuffle(tasks)
    signs=T.question('A98-signs','Evaluate each expression.',
        [rf'({chr(97+j)})\quad '+e for j,(e,a) in enumerate(tasks)],
        [T.ans('('+chr(97+j)+')',a,5,True) for j,(e,a) in enumerate(tasks)])
    signs['verification']=[dict(kind='signed',expressions=tasks)]
    a=r.randint(1,3);b=-r.randint(2,6);c=r.choice([-7,-3,2,5]);e=a*x*x+b*x+c
    quad=T.question('A98-quad','Evaluate at (a) x = 10, (b) x = -10, and (c) x = 0.',
        [T.tex(e)],[T.ans('('+chr(97+j)+')',T.tex(e.subs(x,z)),w) for j,(z,w) in enumerate([(10,7),(-10,7),(0,6)])])
    quad['verification']=[dict(kind='expression',input=str(e.subs(x,z)),answer=str(e.subs(x,z))) for z in [10,-10,0]]
    assert len({e.subs(x,z) for z in [10,-10,0]})==3
    return [signs,reduction(r,'A98'),evaluation(r,'A98-eval'),quad,comparison(r,'A98',i)]

def arithmetic99(r,i):
    roots=r.sample(range(4,13),2);parts=[(roots[0]**2,str(roots[0])),(-roots[1]**2,str(roots[1])+'i')];r.shuffle(parts)
    rootq=T.question('A99-root','Evaluate the principal square root in each part.',
        [rf'({chr(97+j)})\quad \sqrt{{{n}}}' for j,(n,a) in enumerate(parts)],
        [T.ans('('+chr(97+j)+')',a,10) for j,(n,a) in enumerate(parts)])
    rootq['verification']=[dict(kind='expression',input=f'sqrt({n})',answer=a.replace('i','*I')) for n,a in parts]
    k=r.choice([2,3,5,7]);p=r.choice([2,3,5])
    rad=expression('A99-simplify','Simplify the square root.',[S.sqrt(k*k*p)])
    rad['math']=[rf'\sqrt{{{k*k*p}}}']
    a=r.choice([1,2]);h=r.randint(1,3);b=r.randint(2,4);inp=r.choice([2,3,4])
    if i%3==2:
        poly=S.expand((2*x-1)*(x-h));aa,bb,cc=S.Poly(poly,x).all_coeffs()
        ev=T.question('A99-formula',f'Evaluate both values in the formula for a = {aa}, b = {bb}, c = {cc}.',
            [r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}'],[T.ans('',T.solution_tex(S.solve(poly,x)),20)])
        ev['verification']=[dict(kind='equation',lhs=str(poly),rhs='0',denominators=[],candidates=list(map(str,S.solve(poly,x))),answers=list(map(str,S.solve(poly,x))))]
    else:
        e=a*x*x-b*x+h if i%3==0 else a*(x-h)*(x+b)
        ev=T.question('A99-eval',f'Evaluate at (a) x = {inp} and (b) x = {-inp}.',
            [T.tex(e)],[T.ans('('+chr(97+j)+')',T.tex(e.subs(x,z)),10) for j,z in enumerate([inp,-inp])])
        ev['verification']=[dict(kind='expression',input=str(e.subs(x,z)),answer=str(e.subs(x,z))) for z in [inp,-inp]]
    return [reduction(r,'A99'),rootq,rad,ev,comparison(r,'A99',i)]

def polynomials98(r,i):
    k=r.randint(1,4);a=r.randint(2,5);b=r.randint(2,5)
    p=a*x**3-b*x*x-k;z=-(a+1)*x**3+k*x+k+2
    u=(k+2)*x**4-2*x*x+x-k;v=3*x**4+(k+1)*x*x-4
    add=expression('P98-addsub','(a) Add and simplify. (b) Subtract and simplify.',[p+z,u-v])
    add['math']=[r'(a)\quad '+T.par(p)+' + '+T.par(z),r'(b)\quad '+T.par(u)+' - '+T.par(v)]
    outside=-r.randint(2,6)*x**r.randint(1,3);inside=2*x**3-k*x+r.randint(2,6)
    dist=expression('P98-dist','Distribute and simplify.',[outside*inside]);dist['math']=[T.tex(outside)+T.par(inside)]
    f,g=r.sample(range(1,6),2);s=-1 if i%2 else 1
    e1=(x+f)*(x+s*g)
    a,c=r.choice([(2,3),(2,5),(3,4),(4,5)]);d=r.randint(1,4);b=r.randint(1,4)
    if a*d-b*c==0:d+=1
    e2=(a*x-b)*(c*x+d)
    mult=expression('P98-binomial','Multiply and simplify both products.',[e1,e2])
    mult['math']=[r'(a)\quad '+T.par(x+f)+T.par(x+s*g),r'(b)\quad '+T.par(a*x-b)+T.par(c*x+d)]
    factors=[(x-k,2*x*x+x+3),(x+2,2*x**3-x*x+3*x-k),(x*x+x-k,2*x*x-x+3)][i%3]
    large=expression('P98-large','Multiply and simplify.',[factors[0]*factors[1]]);large['math']=[T.par(factors[0])+T.par(factors[1])]
    gp=r.randint(2,6)*x**r.randint(1,3)*(2*x*x+3*x+5)
    pairs=[(2,5),(-2,-5),(2,-5),(-2,5),(3,4)]
    f,g=pairs[i%5];mon=S.expand((x+f)*(x+g))
    fac=expression('P98-factor','(a) Factor out the greatest common factor. (b) Factor the trinomial.',
        [S.expand(gp),mon],[S.factor(gp),S.factor(mon)])
    return [add,dist,mult,large,fac]

def polynomials99(r,i):
    a,c=r.choice([(2,3),(3,4),(2,5)]);b=r.randint(1,5);d=r.randint(1,4)
    if a*d-b*c==0:d+=1
    e=(a*x-b)*(c*x+d);mult=expression('P99-mult','Multiply and simplify.',[e]);mult['math']=[T.par(a*x-b)+T.par(c*x+d)]
    g=(r.randint(2,6) if i%2==0 else 1)*x**(1 if i%2==0 else 2)
    p=S.expand(g*(2*x*x+r.choice([-3,-1,1,3])*x+5))
    gcf=expression('P99-gcf','Factor out the greatest common factor.',[p],[S.factor(p)])
    f,h=r.sample(range(1,6),2);f*=(-1 if i%2 else 1);h*=(-1 if i%3 else 1)
    A,B=r.choice([(1,3),(1,7),(2,5),(3,4),(4,3)])
    basic=expression('P99-basic','Factor completely.',[S.expand((x+f)*(x+h)),A*A*x*x-B*B],
        [S.factor((x+f)*(x+h)),(A*x-B)*(A*x+B)])
    smallpool=[2*x*x+3*x-2,2*x*x-5*x+2,3*x*x+5*x+2,3*x*x-5*x+2,5*x*x+6*x+1,2*x*x-x-3]
    primepool=[2*x*x+3*x+3,3*x*x+x+2,2*x*x+x+5,5*x*x+2*x+1,3*x*x-2*x+3]
    vals=[r.choice(smallpool),r.choice(primepool)];r.shuffle(vals)
    small=T.question('P99-small','Factor completely over the integers, or write prime.',
        [rf'({chr(97+j)})\quad '+T.tex(e) for j,e in enumerate(vals)],
        [T.ans('('+chr(97+j)+')','Prime' if S.discriminant(e,x)<0 else T.tex(S.factor(e)),10,S.discriminant(e,x)<0) for j,e in enumerate(vals)])
    small['verification']=[dict(kind='factoring',input=str(e),answer=str(S.factor(e)),prime=bool(S.discriminant(e,x)<0)) for e in vals]
    richpool=[]
    for a,c,b,d in [(3,4,5,3),(3,4,4,5),(3,5,4,3),(2,5,3,12),(3,4,3,5)]:
        for s,t in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            e=S.expand((a*x+s*b)*(c*x+t*d));co=list(map(int,S.Poly(e,x).all_coeffs()))
            if math.gcd(*co)==1 and co[1] and len(S.divisors(abs(co[0]*co[2])))//2>=8 and abs(co[0])<=15 and abs(co[2])<=15:
                richpool.append(e)
    e=r.choice(richpool);rich=expression('P99-group','Factor completely.',[e],[S.factor(e)])
    return [mult,gcf,basic,small,rich]

def fractions98(r,i):
    def pair(op,reduce):
        while True:
            b,d=r.sample(range(3,16),2);a=r.randint(1,b-1);c=r.randint(1,d-1)
            l=math.lcm(b,d);n=a*(l//b)+(1 if op=='+' else -1)*c*(l//d)
            if l<=60 and n>0 and (math.gcd(n,l)>1)==reduce and S.Rational(n,l).q!=1:return [(a,b),(c,d)]
    def q(fid,pairs,op):
        vals=[S.Rational(a,b) for a,b in pairs];z=vals[0]
        for w in vals[1:]:z=z+w if op=='+' else z-w if op=='-' else z*w if op==r'\times' else z/w
        expr=(' '+op+' ').join(str(a) if b==1 else T.frac(a,b) for a,b in pairs)
        result=T.question(fid,'Compute and give the result in lowest terms.',[expr],[T.ans('',T.tex(z),20)])
        plainop={'\\times':'*','\\div':'/'}.get(op,op)
        result['verification']=[dict(kind='expression',input=(' '+plainop+' ').join(f'({a}/{b})' for a,b in pairs),answer=str(z))]
        return result
    n=r.choice([2,4,5,7])
    if i%2==0:mult=[(n,1),(2,3),(3,5)];div=[(r.choice([22,44]),15),(33,25)]
    else:mult=[(14,15),(25,21),(r.choice([7,9,11]),10)];div=[(2*n,1),(4,5)]
    extra=[([(1,7),(2,7)],'+'), ([(7,11),(3,11)],'-'), ([(2,5),(3,7)],r'\times'), ([(2,5),(7,3)],r'\div')][i%4]
    return [q('F98-add',pair('+',i%2==0),'+'),q('F98-sub',pair('-',i%2!=0),'-'),
        q('F98-mult',mult,r'\times'),q('F98-div',div,r'\div'),q('F98-extra',*extra)]

def linear98(r,i):
    h=r.randint(1,5);integer=S.Integer(r.choice([-3,-2,2,3,4]));fraction=r.choice([S.Rational(3,2),S.Rational(5,3),S.Rational(-5,2)])
    z1,z2=(fraction,integer) if i%2==0 else (integer,fraction)
    # All printed coefficients stay integral, including the two distributions.
    lhs=(x+h)/3+(x-1)/6;rhs=S.simplify(lhs.subs(x,z1))
    frac=solveq('L98-frac',[T.frac(x+h,3)+' + '+T.frac(x-1,6)+' = '+T.tex(rhs)],lhs,rhs)
    aa,bb,cc=3,2,3 if z2.q==3 else 2
    # Coefficient of x after collecting is 3, or 2, matching the chosen denominator.
    dd=aa*bb+1-cc
    ll=aa*(bb*x-h)-(dd*x+h+1)+x;rr=S.Integer(cc)*z2-aa*h-h-1
    long=solveq('L98-dist',[f'{aa}({bb}x-{h})-({dd}x+{h+1})+x = '+T.tex(rr)],ll,rr)
    assert rr.is_integer
    def system(fid,general=False):
        px=r.choice([-4,-3,-2,1,2,3,4]);py=r.choice([-4,-2,1,2,3,4])
        if general:ls=[2*x+3*y,3*x+5*y];rs=[2*px+3*py,3*px+5*py]
        elif i%2:ls=[2*x+3*y,3*x-3*y];rs=[2*px+3*py,3*px-3*py]
        else:ls=[y, x+y];rs=[2*x+py-2*px,px+py]
        assert S.solve([l-z for l,z in zip(ls,rs)],[x,y])=={x:px,y:py}
        q=T.question(fid,'Solve the system.',[T.eq(l,z) for l,z in zip(ls,rs)],[T.ans('',T.tex(S.Tuple(px,py)),20)])
        q['verification']=[dict(kind='system',lhs=list(map(str,ls)),rhs=list(map(str,rs)),answer=[px,py])]
        return q
    k=r.randint(2,5);h=r.randint(1,5)
    if i%4<2:
        left=f'{k}(x-{h})+2';right=k*x-k*h+(3 if i%4==0 else 2)
        e=T.question('L98-exception','Solve and state the complete solution set.',[left+' = '+T.tex(right)],
            [T.ans('','No solution' if i%4==0 else 'All real numbers',20,True)])
    else:
        c=r.randint(3,9);delta=1 if i%4==2 else 0
        e=T.question('L98-exception','Solve the system and state the complete solution set.',
            [T.eq(2*x+3*y,c),T.eq(4*x+6*y,2*c+delta)],
            [T.ans('','No solution' if delta else f'Infinitely many solutions: 2x + 3y = {c}',20,True)])
    return [frac,long,system('L98-basic'),system('L98-general',True),e]

def rational99(r,i):
    h=r.randint(2,5);b=r.randint(2,5)
    n=S.expand((2*x+1)*(x-h));d=S.expand(3*(x-h)*(x+b))
    simple=expression('R99-simple','Simplify.',[n/d]);simple['math']=[T.frac(n,d)];simple['rows'][0]['answer']=T.tex(S.factor(S.cancel(n/d)))
    k=h+r.choice([2,3,4]);den=S.expand((x-h)*(x-k))
    if i%2==0:add=(1,k-h);sub=(2,1)
    else:add=(2,1);sub=(1,h-k)
    qs=[simple]
    for fid,pairs,op in [('R99-add',add,'+'),('R99-sub',sub,'-')]:
        a,c=pairs
        e=a/(x-h)+(1 if op=='+' else -1)*c/den
        q=expression(fid,'Add and simplify.' if op=='+' else 'Subtract and simplify.',[e])
        q['math']=[T.frac(a,x-h)+' '+op+' '+T.frac(c,den)];q['rows'][0]['answer']=T.tex(S.factor(S.cancel(e)));qs.append(q)
    # Exactly one addition/subtraction has a cancellable numerator.
    assert sum(S.degree(S.fraction(S.cancel(S.sympify(q['verification'][0]['input'],locals={'x':x})))[1],x)==1 for q in qs[1:])==1
    g=r.choice([(4,6),(6,9),(8,12)]);n=S.expand(g[0]*x*(x-h));d=S.expand(g[1]*(x-h)*(x+b))
    e=n/d*(x+b)/x;q=expression('R99-mul','Multiply and simplify.',[e]);q['math']=[T.frac(n,d)+r'\times'+T.frac(x+b,x)];qs.append(q)
    a=r.randint(2,6);den=S.expand((x-a)*(x+b));e=(x*x-a*a)/den/((x+a)/(x+b))
    q=expression('R99-div','Divide and simplify.',[e]);q['math']=[T.frac(x*x-a*a,den)+r'\div'+T.frac(x+a,x+b)];qs.append(q)
    return qs

def equations99(r,i):
    a,b=r.sample(range(1,7),2);poly=S.expand((x-a)*(x+b))
    factor=solveq('E99-factor',[T.eq(x*x+(b-a)*x,a*b)],poly)
    while True:
        aa=r.randint(2,4);bb=r.choice([-5,-3,-1,1,3,5]);cc=-r.randint(1,6);d=bb*bb-4*aa*cc
        if math.isqrt(d)**2!=d and math.gcd(aa,math.gcd(abs(bb),abs(cc)))==1:break
    p=aa*x*x+bb*x+cc;formula=solveq('E99-formula',[T.eq(p,0)],p)
    h=r.randint(-3,3);k=r.randint(2,5);a=r.randint(2,4);p=a*(x-h)**2
    sqrt=solveq('E99-sqrt',[str(a)+T.par(x-h)+rf'^2 = {a*k*k}'],p,S.Integer(a*k*k))
    h=r.randint(2,5);d=h+1
    if i%2==0:
        z=h+r.randint(1,3);K=h+z-1;A=2*h
    else:
        z,w=r.sample([v for v in range(-3,7) if v not in [-h,h]],2)
        d=h+2;K=z+w-2;A=z*w+d*h-K*h
        if A==0:return equations99(r,i)
    lhs=A/(x*x-h*h)+(x-d)/(x-h);rhs=K/(x+h)
    quad=solveq('E99-rquad',[T.frac(A,x*x-h*h)+' + '+T.frac(x-d,x-h)+' = '+T.frac(K,x+h)],lhs,rhs,[x-h,x+h])
    u=r.randint(1,4);w=u+r.randint(2,4);A=2*r.randint(2,5);c=A//2+1
    z=u+1;B=A//2*(w-u) if i%2 else c*(z-u)-A//2*(z-w)
    ll=A/(2*x-2*u)+B/((x-u)*(x-w));rr=c/(x-w)
    lin=solveq('E99-rlinear',[T.frac(A,2*x-2*u)+' + '+T.frac(B,S.expand((x-u)*(x-w)))+' = '+T.frac(c,x-w)],ll,rr,[x-u,x-w])
    checks=quad['verification']+lin['verification']
    assert sum(len(z['candidates']) for z in checks)==3
    assert sum(len(z['answers']) for z in checks)==2
    return [factor,formula,sqrt,quad,lin]

def graph99(r,i):
    m=r.choice([S.Rational(1,2),S.Rational(2,3),S.Rational(3,2)]);b=r.randint(-4,4)
    def graphq(fid,prompt,maths,rows,lines):
        q=T.question(fid,prompt,maths,rows,graph={'kind':'blank','answer_lines':[[float(m),float(b)] for m,b in lines]})
        q['verification']=[dict(kind='graph',lines=[[str(m),str(b)] for m,b in lines])]
        return q
    slope=graphq('G99-slope','Graph the line on the grid.',[T.eq(y,m*x+b)],[T.ans('Graph',T.eq(y,m*x+b),20)],[(m,b)])
    A,B,C=r.choice([(2,3,12),(3,2,12),(1,2,8),(2,1,8),(3,4,24),(4,3,24)])
    standard=graphq('G99-standard','Find both intercepts and graph the line on the grid.',[T.eq(A*x+B*y,C)],
        [T.ans('Intercepts',T.tex(S.Tuple(S.Rational(C,A),0))+r';\ '+T.tex(S.Tuple(0,S.Rational(C,B))),8),T.ans('Graph',T.eq(y,-S.Rational(A,B)*x+S.Rational(C,B)),12)],[(-S.Rational(A,B),S.Rational(C,B))])
    px=r.choice([-3,-2,-1,1,2,3]);py=r.choice([-3,-2,-1,1,2,3]);m1=r.choice([1,2]);m2=r.choice([-1,-2])
    b1,b2=py-m1*px,py-m2*px
    system=graphq('G99-system','Graph both lines on the same grid and give their intersection.',
        [T.eq(y,m1*x+b1),T.eq(y,m2*x+b2)],[T.ans('Graph','Both lines meet at the reported solution.',12,True),T.ans('Ordered pair',T.tex(S.Tuple(px,py)),8)],[(m1,b1),(m2,b2)])
    rm=r.choice([-S.Rational(1,2),-S.Rational(2,3),-S.Rational(3,2)]);rb=r.randint(-3,3);point=rm.q
    read=T.question('G99-read','Write the equation of the displayed line in slope-intercept form.',[],[T.ans('',T.eq(y,rm*x+rb),20)],graph={'kind':'line','m':float(rm),'b':rb,'point':int(point)})
    read['verification']=[dict(kind='graph',lines=[[str(rm),str(rb)]])]
    pm=r.choice([S.Rational(1,3),S.Rational(2,3),S.Rational(1,2)]);pb=r.randint(-3,3)
    pts=[S.Tuple(t,pm*t+pb) for t in [pm.q,2*pm.q]]
    assert all(v.is_integer for p in pts for v in p)
    points=T.question('G99-points','Find the slope-intercept equation through the two points.',
        [r';\ '.join(T.tex(p) for p in pts)],[T.ans('',T.eq(y,pm*x+pb),20)])
    points['verification']=[dict(kind='line_points',points=[list(map(str,p)) for p in pts],slope=str(pm),intercept=str(pb))]
    return [slope,standard,system,read,points]

UNITS={'98-arithmetic':arithmetic98,'98-polynomials':polynomials98,'98-fractions':fractions98,
    '98-linear':linear98,'99-arithmetic':arithmetic99,'99-polynomials':polynomials99,
    '99-rational':rational99,'99-equations':equations99,'99-graphing':graph99}

def questions(slug,index,seed):
    r=random.Random(seed)
    if not slug.endswith('final'):return UNITS[slug](r,index)
    course='TSM 098' if slug.startswith('98') else 'TSM 099'
    institutional_questions=institutional(course,seed,index%4)
    if course=='TSM 098':
        supplements=[evaluation(r,'S098-eval'),fractions98(r,index)[0],linear98(r,index)[2],polynomials98(r,index)[0]]
        # A single ordinary subtraction broadens coverage without doubling workload.
        q=supplements[-1];q['math']=[q['math'][1].removeprefix(r'(b)\quad ')];q['rows']=[q['rows'][1]];q['rows'][0]['label']='';q['rows'][0]['points']=20;q['verification']=[q['verification'][1]]
    else:
        graph=graph99(r,index)
        supplements=[graph[4],graph[1],arithmetic99(r,index)[3],equations99(r,index)[2]]
    for q in supplements:
        oldtotal=sum(z['points'] for z in q['rows'])
        for row in q['rows']:row['points']=int(row['points']*10/oldtotal)
        assert sum(z['points'] for z in q['rows'])==10
        q['id']='S'+q['id'] if not q['id'].startswith('S') else q['id']
    return institutional_questions+supplements
