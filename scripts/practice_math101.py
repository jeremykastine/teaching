"""Symbolic MATH 101 practice-question constructors."""
from build_practice_tests import *

def unit1(v):
    k=v+2;rad=(v+3)**2*[2,3,5][v]
    q1=question('U1-1','Simplify. In (a), x and y are nonzero; give positive exponents.',[r'(a)\quad \frac{6x^{-'+str(k)+r'}y^3}{3xy^{-1}}',r'(b)\quad \sqrt{'+str(rad)+'}'],[ans('(a)',tex(2*y**4/x**(k+1)),10),ans('(b)',tex(S.sqrt(rad)),10)])
    op=((v+2)*x-3)*(x+v+2);fac=S.expand((2*x+v+1)*(x-v-3))
    q2=question('U1-2','(a) Expand and simplify. (b) Factor completely.',[r'(a)\quad '+par((v+2)*x-3)+par(x+v+2),r'(b)\quad '+tex(fac)],[ans('(a)',tex(exact('U1-2a',op)),10),ans('(b)',tex(S.factor(fac)),10)])
    a=v+2;b=v+4;rn=x*x-a*a;rd=S.expand((x-a)*(x+b));expr=rn/rd
    q3=question('U1-3','Simplify and state all values excluded by the original expression.',[frac(rn,rd)],[ans('Expression',tex(S.factor(exact('U1-3',expr))),14),ans('Excluded values',tex(S.FiniteSet(a,-b)),6)])
    quad=S.expand((x-(v+1))*(x+v+3));qr,_=solved('U1-4a',quad)
    h=v+2;ll=(v+4)/(2*x-2*h)+1/(x-h);rr=S.Rational(v+6,2);rt,_=solved('U1-4b',ll,rr,denoms=[x-h])
    q4=question('U1-4','Solve both equations. In (b), state original restrictions and check your answer.',[r'(a)\quad '+eq(quad,0),r'(b)\quad '+frac(v+4,2*x-2*h)+' + '+frac(1,x-h)+' = '+tex(rr)],[ans('(a)',solution_tex(qr),10),ans('(b), with check',solution_tex(rt)+r';\ x\ne '+str(h),10)])
    boundary=v+3;low=S.Rational(1-boundary,2);high=S.Rational(1+boundary,2)
    q5=question('U1-5','Solve the inequality and write the solution in interval notation.',[r'|2x-1|\leq '+str(boundary)],[ans('Derived bounds',tex(low)+r'\leq x\leq '+tex(high),12),ans('Interval',tex(S.Interval(low,high)),8)])
    return [q1,q2,q3,q4,q5]

def composition(v,points=20,final=False):
    a=v+2+int(final);b=v+1+2*int(final);k=v+3+int(final);f=x*x+k;g=a*x+b;h=f.subs(x,g)
    pairs=[(f,g),(g,f),(x*x+b,a*x+k),(a*x*x+k,x+b)]
    assert sum(S.expand(ff.subs(x,gg)-h)==0 for ff,gg in pairs)==1
    random.Random(v+91+(20 if final else 0)).shuffle(pairs)
    good=next(i for i,(ff,gg) in enumerate(pairs) if S.expand(ff.subs(x,gg)-h)==0)
    maths=[r'h(x)='+par(a*x+b)+r'^2+'+str(k)]+[rf'{chr(65+i)}.\quad f(x)='+tex(ff)+r',\ g(x)='+tex(gg) for i,(ff,gg) in enumerate(pairs)]
    if final:return question('M101-composition','Which pair satisfies h(x) = f(g(x))?',maths,[ans('Choice',chr(65+good),points,True)])
    ff=x*x;gg=x-v-2;z=v+3
    maths += [r'(b)\quad F(x)=x^2,\ G(x)='+tex(gg)+rf',\ x_0={z}']
    return question('U2-3','(a) Choose the pair giving h(x) = f(g(x)). (b) Form F(G(x)) and evaluate it at the supplied input.',maths,[ans('(a) Choice',chr(65+good),8,True),ans('(b) Composition',tex(S.expand(ff.subs(x,gg))),8),ans('(b) Value',tex(ff.subs(x,gg).subs(x,z)),4)])

def transform(v,points=20,final=False):
    pts=[[-3,0],[-1,v+2],[0,-1],[2,1]];mode=['shift','vertical','horizontal'][v]
    if mode=='shift':
        hh=3+int(final);kk=-2-v;choices=[f'f(x-{hh}){kk:+}',f'f(x+{hh}){kk:+}',f'f(x-{hh}){-kk:+}',f'f(x+{hh}){-kk:+}'];g={'kind':'transform','points':pts,'mode':mode,'h':hh,'k':kk}
    elif mode=='vertical':
        aa=-2-int(final);choices=[f'{aa}f(x)',f'f({aa}x)',f'{-aa}f(x)',f'f(x){aa:+}'];g={'kind':'transform','points':pts,'mode':mode,'a':aa}
    else:
        aa=2+int(final);choices=[f'f({aa}x)',f'{aa}f(x)',r'f(x/'+str(aa)+')',f'f(x-{aa})'];g={'kind':'transform','points':pts,'mode':mode,'a':aa}
    indexed=list(enumerate(choices));random.Random(600+v+int(final)).shuffle(indexed);correct=next(i for i,(j,t) in enumerate(indexed) if j==0)
    return question('M101-transform' if final else 'U2-4','The solid graph is f and the dashed graph is g. Select the expression for g(x).',[rf'{chr(65+i)}.\quad g(x)='+t for i,(j,t) in enumerate(indexed)],[ans('Choice',chr(65+correct),points,True)],graph=g)

def unit2(v):
    h=v+1;k=v+2;a=v+2;f=a*S.Abs(x-h)-k;inp=-v-1
    q1=question('U2-1',rf'For this function, find (a) f({inp}), (b) domain, and (c) range.',[r'f(x)='+tex(f)],[ans('(a) Value',tex(f.subs(x,inp)),6),ans('(b) Domain',r'(-\infty,\infty)',7),ans('(c) Range',tex(S.Interval(-k,S.oo)),7)])
    pts=[[-2-v,0],[0,2+v],[2+v,-2-v],[4+v,1]];rate=S.Rational(1,6+2*v)
    q2=question('U2-2',rf'From the graph, find (a) average rate from x = {-2-v} to x = {4+v}; (b) increasing and decreasing intervals; (c) the two local extrema (ordered pairs).',[],[ans('(a) Rate',tex(rate),6),ans('(b) Increasing',rf'({-2-v},0)\cup({2+v},{4+v})',4),ans('(b) Decreasing',f'(0,{2+v})',4),ans('(c) Local max',tex(S.Tuple(0,2+v)),3),ans('(c) Local min',tex(S.Tuple(2+v,-2-v)),3)],graph={'kind':'behavior','points':pts})
    m=v+2;b=v-1;inv=(x-b)/m
    q5=question('U2-5','(a) Find the linear function through these points, with domain all real numbers. (b) Find its inverse and give the inverse domain and range.',[tex(S.Tuple(1,m+b))+r';\ '+tex(S.Tuple(3,3*m+b))],[ans('(a) Function',r'f(x)='+tex(m*x+b),10),ans('(b) Inverse',r'f^{-1}(x)='+tex(inv),6),ans('(b) Domain',r'(-\infty,\infty)',2),ans('(b) Range',r'(-\infty,\infty)',2)])
    assert S.simplify((m*x+b).subs(x,inv))==x
    return [q1,q2,composition(v),transform(v),q5]

def polynomial_graph(v,final=False):
    roots=[[-2,1],[-1,2],[-3,1]][v] if not final else [[-1,3],[-2,2],[-3,2]][v]
    a=[1,-1,2][v] if not final else [S.Rational(1,2),-1,1][v];p=a*(x-roots[0])*(x-roots[1])**2;point=(0,p.subs(x,0))
    g={'kind':'polynomial','roots':roots,'multiplicities':[1,2],'a':float(a),'point':[0,float(point[1])]}
    if final:return question('M101-polygraph','Write a polynomial of the least possible degree matching this graph and the labeled point. Give factored form.',[],[ans('Polynomial',tex(a)+par(x-roots[0])+par(x-roots[1])+'^2',10)],graph=g)
    left=r'-\infty' if a>0 else r'\infty';right=r'\infty' if a>0 else r'-\infty'
    return question('U3-2','Write the least-degree polynomial in factored form matching the graph and labeled point. State its end behavior in both directions.',[],[ans('Polynomial',tex(a)+par(x-roots[0])+par(x-roots[1])+'^2',16),ans('Left end',r'x\to-\infty:\ f(x)\to'+left,2),ans('Right end',r'x\to\infty:\ f(x)\to'+right,2)],graph=g)

def zeros(v,final=False):
    rr,bb,cc=([(2,1,-1),(-1,3,1),(1,1,-3)] if not final else [(3,1,-1),(-2,3,1),(-1,2,-2)])[v]
    q=x*x+bb*x+cc;p=S.expand((x-rr)*q);coeff=S.Poly(p,x).all_coeffs();candidates=sorted(set(S.Rational(t,d)*sgn for t in S.divisors(abs(int(coeff[-1]))) for d in S.divisors(abs(int(coeff[0]))) for sgn in [-1,1]))
    assert len(candidates)<=8 and S.div(p,x-rr)==(q,0)
    others=S.solve(q,x);assert len(others)==2 and all(z.is_real and z.is_irrational for z in others)
    weights=[2,4,4] if final else [5,7,8]
    return question('M101-zeros' if final else 'U3-3',rf'Find all zeros: (a) list Rational Root Theorem candidates, then test only {rr} and {-rr}; (b) use polynomial long division by the confirmed linear factor; (c) use the quadratic formula on the quotient. Record all zeros.',[r'p(x)='+tex(p)],[ans('(a) Candidates/root',tex(S.FiniteSet(*candidates))+rf';\ x={rr}',weights[0]),ans('(b) Quotient',tex(q)+r';\ R=0',weights[1]),ans('(c) Other zeros',solution_tex(others),weights[2])])

def rational_behavior(v,final=False):
    h=-(v+2) if final else v+1;a=v+3;b=v+5
    f=(x-h)*(x+a)/((x-h)*(x-b));hole=S.cancel(f).subs(x,h);yi=S.cancel(f).subs(x,0)
    w=[2,2,1,1,2,2] if final else [4,4,3,3,3,3]
    return question('M101-rational' if final else 'U3-4','Find (a) domain; (b) hole, vertical asymptote, and horizontal asymptote; (c) both intercepts.',[r'f(x)='+frac(S.Mul(x-h,x+a,evaluate=False),S.Mul(x-h,x-b,evaluate=False))],[ans('(a) Domain',r'\mathbb{R}\setminus '+tex(S.FiniteSet(h,b)),w[0]),ans('(b) Hole',tex(S.Tuple(h,hole)),w[1]),ans('(b) Vertical',f'x={b}',w[2]),ans('(b) Horizontal',r'y=1',w[3]),ans('(c) x-intercept',tex(S.Tuple(-a,0)),w[4]),ans('(c) y-intercept',tex(S.Tuple(0,yi)),w[5])])

def radical_behavior(v,final=False):
    h=-[1,4,9][v] if not final else -[4,9,16][v];a=v+1;k=-(v+2)*a;f=a*S.sqrt(x-h)+k;xi=h+(v+2)**2;yi=a*S.sqrt(-h)+k
    w=[2,2,1,1,3,1] if final else [4,4,3,3,4,2]
    return question('M101-radical' if final else 'U3-5','Find (a) domain and range; (b) both intercepts; (c) behavior as x tends to infinity and as x approaches the finite domain endpoint from within the domain.',[r'f(x)='+tex(f)],[ans('(a) Domain',tex(S.Interval(h,S.oo)),w[0]),ans('(a) Range',tex(S.Interval(k,S.oo)),w[1]),ans('(b) x-intercept',tex(S.Tuple(xi,0)),w[2]),ans('(b) y-intercept',tex(S.Tuple(0,yi)),w[3]),ans('(c) Infinite end',r'x\to\infty:\ f(x)\to\infty',w[4]),ans('(c) Finite end',rf'x\to {h}^+:\ f(x)\to {k}',w[5])])

def unit3(v):
    h=v-1;a=v+1;r=v+2;k=-a*r*r;f=a*(x-h)**2+k
    q1=question('U3-1','Find (a) the vertex and the minimum or maximum value (state which); (b) all zeros.',[r'f(x)='+tex(f)],[ans('(a) Vertex',tex(S.Tuple(h,k)),6),ans('(a) Minimum',tex(k),4),ans('(b) Zeros',solution_tex([h-r,h+r]),10)])
    return [q1,polynomial_graph(v),zeros(v),rational_behavior(v),radical_behavior(v)]

def exponentials(v,final=False):
    curves=[[(1,2),(2,1.5),(1,.5),(2,2/3)],[(2,2),(3,1.5),(2,.5),(3,2/3)],[(1,3),(2,2),(1,1/3),(2,.5)]][v]
    if final:curves=[(a+1,b) for a,b in curves]
    random.Random(810+v+int(final)).shuffle(curves);order=[2,0,3,1];display=[curves[i] for i in order]
    maths=[rf'({chr(97+i)})\quad '+tex(S.Integer(a))+'('+tex(S.Rational(str(b)).limit_denominator(10))+')^x' for i,(a,b) in enumerate(display)]
    # Integer parts totaling 10 for the cumulative exam, equal parts for the unit.
    weights=[3,2,3,2] if final else [5]*4
    return question('M101-exponential' if final else 'U4-1','Match each function to graph A, B, C, or D. Each letter is used once.',maths,[ans('('+chr(97+i)+')',chr(65+j),weights[i],True) for i,j in enumerate(order)],graph={'kind':'exponential','curves':curves})

def logarithmic_behavior(v,final=False):
    base=v+2;h=v+1+int(final);k=v+1;xi=h+S.Rational(1,base**k)
    w=[2,2,1,1,2,2] if final else [4,4,3,3,3,3]
    return question('M101-logarithm' if final else 'U4-2','Find (a) domain and range; (b) vertical asymptote and x-intercept; (c) behavior at both ends of the domain.',[r'f(x)=\log_{'+str(base)+'}(x-'+str(h)+')+'+str(k)],[ans('(a) Domain',tex(S.Interval.open(h,S.oo)),w[0]),ans('(a) Range',r'(-\infty,\infty)',w[1]),ans('(b) Asymptote',rf'x={h}',w[2]),ans('(b) x-intercept',tex(S.Tuple(xi,0)),w[3]),ans('(c) Left end',rf'x\to {h}^+:\ f(x)\to-\infty',w[4]),ans('(c) Right end',r'x\to\infty:\ f(x)\to\infty',w[5])])

def log_properties(v,final=False):
    pair=([('0.2','500',2),('0.4','2500',3),('0.5','20000',4)] if not final else [('0.25','400',2),('0.8','1250',3),('0.05','200000',4)])[v];base=v+3+3*int(final);q=v+2+int(final);w=5 if final else 10
    return question('M101-logproperties' if final else 'U4-3','Evaluate exactly using logarithmic properties; show the property used. Here log means base 10.',[r'(a)\quad \log('+pair[0]+r')+\log('+pair[1]+')',r'(b)\quad \frac{\log_{'+str(base)+'}('+str(q**3)+r')}{\log_{'+str(base)+'}('+str(q**2)+')}'],[ans('(a)',str(pair[2]),w),ans('(b)',tex(S.Rational(3,2)),w)])

def nonlinear(v):
    if v==1:
        lhs=x*x;line=x+2;rs=S.solve(lhs-line,x);pts=[(z,lhs.subs(x,z)) for z in rs]
        maths=[eq(y,lhs),eq(y,line)];ineq=[r'y\geq x^2',r'y<x+2'];check='At (0,0): 0 >= 0 and 0 < 2; yes, in the region.'
    else:
        k=v+1;radius=1+(1+k)**2;pts=[(1,1+k),(-k-1,-1)]
        maths=[eq(x*x+y*y,radius),eq(y,x+k)];ineq=[r'x^2+y^2\leq '+str(radius),r'y>x+'+str(k)];check=f'At (0,0): 0 <= {radius}, but 0 > {k} is false; not in the region.'
        for px,py in pts:assert px*px+py*py==radius and py==px+k
    return maths,pts,ineq,check

def unit4(v):
    root=v*3+4;assert 2*(root-v-1)==root+v+2
    h=v+1;base=v+2;logroot=h+S.Rational(base**2,v+3)
    q4=question('U4-4','Solve both equations exactly. Check the logarithmic domain in (b).',[r'(a)\quad 4^{x-'+str(v+1)+r'}=2^{x+'+str(v+2)+'}',r'(b)\quad \log_{'+str(base)+'}(x-'+str(h)+r')+\log_{'+str(base)+'}('+str(v+3)+')=2'],[ans('(a)',solution_tex([root]),8),ans('(b), with domain',solution_tex([logroot])+rf';\ x>{h}',12)])
    px=v+2;py=v+1;lins=[eq(x+y,px+py),eq(x-y,px-py)];maths,pts,ineq,check=nonlinear(v)
    q5=question('U4-5','(a) Solve the linear system. (b) Solve the nonlinear system algebraically. (c) Test whether (0,0) belongs to the region given by the inequalities; show both comparisons.',[r'(a)\quad '+lins[0],lins[1],r'(b)\quad '+maths[0],maths[1],r'(c)\quad '+ineq[0]+r',\ '+ineq[1]],[ans('(a) Ordered pair',tex(S.Tuple(px,py)),6),ans('(b) Intersections',r';\ '.join(tex(S.Tuple(*p)) for p in pts),10),ans('(c) Membership',check,4,True)])
    return [exponentials(v),logarithmic_behavior(v),log_properties(v),q4,q5]

def final(v):
    out=[composition(v,10,True),transform(v,10,True),polynomial_graph(v,True),zeros(v,True),rational_behavior(v,True),radical_behavior(v,True),exponentials(v,True),logarithmic_behavior(v,True),log_properties(v,True)]
    category=random.Random(20261012+v).choice(['radical','exponential','logarithmic','system'])
    if category=='system':
        maths,pts,_,_=nonlinear(v);q=question('M101-solving','Solve the nonlinear system algebraically.',maths,[ans('Intersections',r';\ '.join(tex(S.Tuple(*p)) for p in pts),10)])
    elif category=='exponential':
        root=5*v+7;assert 3*(root-v-1)==2*(root+v+2)
        q=question('M101-solving','Solve exactly.',[r'8^{x-'+str(v+1)+r'}=4^{x+'+str(v+2)+'}'],[ans('Solution',solution_tex([root]),10)])
    elif category=='logarithmic':
        h=v+2;base=v+2;root=h+S.Rational(base**2,v+4)
        q=question('M101-solving','Solve exactly; check the domain.',[r'\log_{'+str(base)+'}(x-'+str(h)+r')+\log_{'+str(base)+'}('+str(v+4)+')=2'],[ans('Solution/domain',solution_tex([root])+rf';\ x>{h}',10)])
    else:
        h=v+2;lhs=S.sqrt(x+h);rhs=x-h;rt=S.solve(lhs-rhs,x);candidates=S.solve(x+h-(x-h)**2,x)
        q=question('M101-solving','Solve the one-radical equation. Check all candidates in the original equation.',[eq(lhs,rhs)],[ans('Valid solutions',solution_tex(rt),7),ans('Rejected candidate',tex(next(z for z in candidates if z not in rt)),3)])
    q['category']=category;out.append(q);return out
