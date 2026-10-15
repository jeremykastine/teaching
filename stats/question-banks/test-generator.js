/* Select one question per topic pool, then shuffle questions and choices.
   Keep version 1's selection rules stable so saved test links remain reproducible. */
(function (root) {
  'use strict';
  const VERSION=1;
  function random(seed) { let a=seed>>>0;return ()=>{a+=0x6D2B79F5;let t=a;t=Math.imul(t^(t>>>15),t|1);t^=t+Math.imul(t^(t>>>7),t|61);return ((t^(t>>>14))>>>0)/4294967296;}; }
  function generate(bank,seed) {
    if(bank.groups.length!==10||new Set(bank.groups.map(g=>g.id)).size!==10)throw new Error('A test requires ten distinct topic pools.');
    const r=random(seed),shuffle=items=>{const a=[...items];for(let i=a.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;};
    const chosen=bank.groups.map(group=>{
      const pool=bank.questions.filter(q=>q.group===group.id);
      if(!pool.length)throw new Error('Every topic pool must contain questions.');
      const q=pool[Math.floor(r()*pool.length)],order=shuffle([0,1,2,3]);
      if(q.choices.length!==4||!Number.isInteger(q.answer_index)||q.answer_index<0||q.answer_index>3)throw new Error('Invalid multiple-choice question.');
      return {...q,choices:order.map(i=>q.choices[i]),answer_index:order.indexOf(q.answer_index)};
    });
    if(new Set(chosen.map(q=>q.id)).size!==10)throw new Error('Each selected question must be distinct.');
    return shuffle(chosen);
  }
  const api={VERSION,generate};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;
  else root.StatisticsTestGenerator=api;
  if(typeof document==='undefined')return;
  const data=document.getElementById('bank-data');if(!data)return;
  const bank=JSON.parse(data.textContent),$=id=>document.getElementById(id);
  let test=[],answers=new Map(),graded=false;
  const node=(tag,text,parent)=>{const e=document.createElement(tag);if(text!==undefined)e.textContent=text;if(parent)parent.append(e);return e;};
  function freshSeed(){if(root.crypto?.getRandomValues){const a=new Uint32Array(1);root.crypto.getRandomValues(a);return a[0];}return Math.floor(Math.random()*4294967296);}
  function markAnswers(focus=true) {
    let correct=0,unanswered=0;
    for(const q of test) {
      const response=answers.get(q.id),feedback=$('feedback-'+q.id),ok=response===q.answer_index;
      if(ok)correct++;if(response===undefined)unanswered++;
      feedback.replaceChildren();feedback.hidden=false;
      feedback.className='feedback '+(ok?'correct':response===undefined?'unanswered':'incorrect');
      node('p',response===undefined?'Not answered.':ok?'Correct.':`Your answer: ${'ABCD'[response]}. ${q.choices[response]}`,feedback);
      const answer=node('p',undefined,feedback);node('strong',`Answer: ${'ABCD'[q.answer_index]}. ${q.choices[q.answer_index]}`,answer);
      node('p',q.explanation,feedback);
      const a=node('a','Review this question in the complete bank',feedback);a.href=`unit-${bank.unit}-question-bank.html#${q.id}`;
    }
    graded=true;$('test-result').hidden=false;
    $('test-result').textContent=`${correct} of 10 correct (${correct*10}%).${unanswered?` ${unanswered} unanswered.`:''} Review the feedback after each question.`;
    if(focus)$('test-result').focus();
  }
  function render(seed) {
    test=generate(bank,seed);answers=new Map();graded=false;
    $('test-result').hidden=true;$('test-result').textContent='';$('copy-fallback').hidden=true;
    const container=$('test-questions');container.replaceChildren();
    test.forEach((q,i)=>{
      const article=node('article',undefined,container);article.className='question';article.id='question-'+q.id;
      node('p',`${q.skill_group} · ${q.id}`,article).className='meta';
      const fieldset=node('fieldset',undefined,article);node('legend',`${i+1}. ${q.stem}`,fieldset);
      if(q.figure){const image=node('img',undefined,fieldset);image.src=q.figure.file;image.alt=q.figure.alt;image.loading='lazy';}
      q.choices.forEach((choice,j)=>{
        const label=node('label',undefined,fieldset);label.className='test-choice';
        const radio=node('input',undefined,label);radio.type='radio';radio.name=q.id;radio.value=String(j);
        radio.addEventListener('change',()=>{answers.set(q.id,j);if(graded)markAnswers(false);});
        node('span',`${'ABCD'[j]}. ${choice}`,label);
      });
      const feedback=node('div',undefined,article);feedback.id='feedback-'+q.id;feedback.className='feedback';feedback.hidden=true;
    });
    const code=seed.toString(16).padStart(8,'0'),url=new URL(location.href);
    url.searchParams.set('v',String(VERSION));url.searchParams.set('seed',code);
    try{history.replaceState(null,'',url);}catch(_){/* Local-file previews may disallow replacing the URL. */}
    $('test-version').textContent=`Unit ${bank.unit} · version ${VERSION} · ${code}`;
    $('test-link').href=url.href;$('test-content').hidden=false;$('check-answers').disabled=false;
    $('generate-test').disabled=false;$('copy-link').disabled=false;
    $('generator-status').textContent='New test ready: ten questions, one from each topic pool. Answers are hidden until you check your work.';
  }
  $('generate-test').addEventListener('click',()=>render(freshSeed()));
  $('check-answers').addEventListener('click',()=>markAnswers());
  $('copy-link').addEventListener('click',async()=>{
    const value=$('test-link').href;
    try{await navigator.clipboard.writeText(value);$('generator-status').textContent='Test link copied. It reopens these same questions in the same order.';}
    catch(_){$('copy-fallback').hidden=false;$('copy-link-text').value=value;$('copy-link-text').focus();$('copy-link-text').select();$('generator-status').textContent='Copy the selected test link manually.';}
  });
  const query=new URLSearchParams(location.search),seed=query.get('seed'),version=query.get('v');
  if((version&&version!==String(VERSION))||(seed&&!/^[0-9a-f]{8}$/i.test(seed))){
    $('generate-test').disabled=false;$('generator-status').textContent='This saved test link is not supported. Select Generate new test to start a fresh version.';
  }else render(seed?parseInt(seed,16):freshSeed());
})(typeof globalThis!=='undefined'?globalThis:this);
