/* Browser controls shared by all nine checks; assignments are generated only on request. */
(function () {
  'use strict';
  const api=window.ExcelCheckGenerators, host=document.querySelector('[data-check]');
  if(!api||!host)return;
  const check=Number(host.dataset.check), $=id=>document.getElementById(id);
  const chooser=$('variation'),status=$('task-status');
  let current;
  for(const [value,label] of api.variants[check]) {const o=document.createElement('option');o.value=value;o.textContent=label;chooser.append(o);}
  function freshSeed(){if(window.crypto?.getRandomValues){const a=new Uint32Array(1);crypto.getRandomValues(a);return a[0];}return Math.floor(Math.random()*4294967296);}
  function appendText(parent,tag,text){const node=document.createElement(tag);node.textContent=text;parent.append(node);return node;}
  function list(id,items){const parent=$(id);parent.replaceChildren();for(const value of items)appendText(parent,'li',value);}
  function render(seed,requested,announce='') {
    current=api.generate(check,seed,requested);
    const code=seed.toString(16).padStart(8,'0');
    $('version-code').textContent=`${String(check).padStart(2,'0')} · v${api.VERSION} · ${code}`;
    $('task-title').textContent=current.title;
    const table=$('task-facts');table.replaceChildren();
    for(const [label,value] of current.facts){const row=document.createElement('tr'),th=appendText(row,'th',label);th.scope='row';appendText(row,'td',String(value));table.append(row);}
    list('task-steps',current.steps);$('task-change').textContent=current.change;
    $('task-data-wrap').hidden=!current.data;$('task-data').value=current.data;$('data-help').textContent=current.dataHelp;
    $('task-data').rows=Math.min(14,Math.max(3,current.data.split('\n').length+1));
    list('task-answers',current.answers);$('answers').open=false;$('copy-fallback-wrap').hidden=true;
    const url=new URL(window.location.href);url.searchParams.set('v',String(api.VERSION));url.searchParams.set('seed',code);url.searchParams.set('variant',requested);
    history.replaceState(null,'',url);$('version-link').href=url.href;
    status.textContent=announce;
  }
  function load(){
    const q=new URLSearchParams(location.search),seed=q.get('seed'),v=q.get('v'),requested=q.get('variant')||'mixed';
    const validVariant=requested==='mixed'||api.variants[check].some(x=>x[0]===requested);
    if((v&&v!==String(api.VERSION))||(seed&&!/^[0-9a-f]{8}$/i.test(seed))||!validVariant){
      // Never silently reinterpret a saved version from a future generator.
      $('generator-controls').hidden=true;$('generated-content').hidden=true;
      $('task-status').textContent='This version link is not supported. Open the clean page link to start a new assignment.';
      const a=document.createElement('a');a.href=location.pathname;a.textContent='Start a new assignment';$('task-status').append(' ',a);return;
    }
    chooser.value=requested;render(seed?parseInt(seed,16):freshSeed(),requested);
  }
  function regenerate(){render(freshSeed(),chooser.value,'New assignment ready. Use this version throughout your attempt.');}
  chooser.addEventListener('change',regenerate);$('regenerate').addEventListener('click',regenerate);
  $('live-check').addEventListener('change',e=>{document.body.classList.toggle('live-check',e.target.checked);$('answers').open=false;});
  async function copy(text,success){
    try {await navigator.clipboard.writeText(text);status.textContent=success;}
    catch(_){$('copy-fallback-wrap').hidden=false;$('copy-fallback').value=text;$('copy-fallback').focus();$('copy-fallback').select();status.textContent='Automatic copying is unavailable. Copy the selected text below manually.';}
  }
  $('copy-data').addEventListener('click',()=>copy(current.data,'Data copied. Paste into the spreadsheet as directed.'));
  $('copy-link').addEventListener('click',()=>copy(location.href,'Version link copied. It reopens these same requirements and data.'));
  $('copy-task').addEventListener('click',()=>{
    const text=[`Excel competency check ${check}: ${current.title}`,`Version: ${$('version-code').textContent}`,location.href,'',...current.facts.map(x=>x.join(': ')),'',...current.steps.map((x,i)=>`${i+1}. ${x}`),'',`Follow-up: ${current.change}`,current.data?`\n${current.dataHelp}\n\n${current.data}`:''].join('\n');
    copy(text,'Assignment copied, including requirements, follow-up, and any source data.');
  });
  window.addEventListener('popstate',()=>location.reload());
  load();
})();

