"""토닥곰 | GitHub + Streamlit Community Cloud
같은 폴더에 requirements.txt를 두고 streamlit run app.py 실행.
GitHub에 두 파일을 올리고 Streamlit Community Cloud에서 app.py 배포.
배포된 공개 주소의 QR코드를 만들면 스마트폰으로 접속할 수 있습니다.
금액 입력은 브라우저 안에서만 계산합니다. 별도 저장·계좌 연동 없음.
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="토닥곰 · 내 돈 돌보기", page_icon="🐻", layout="centered")
st.markdown("""<style>
[data-testid="stHeader"],[data-testid="stToolbar"],footer{display:none!important}
[data-testid="stAppViewContainer"]{background:#f1f7f5}
.block-container,[data-testid="stMainBlockContainer"]{padding:0!important;max-width:500px!important}
[data-testid="stVerticalBlock"]{gap:0!important}
iframe{display:block;width:100%;height:100svh!important;border:0}
</style>""", unsafe_allow_html=True)
PAGE = r'''<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<style>
*{box-sizing:border-box}html,body{margin:0;background:#f1f7f5;color:#191f28;font-family:system-ui,-apple-system,'Apple SD Gothic Neo','Malgun Gothic',sans-serif}body{padding:16px}main{max-width:460px;margin:auto}h1{font-size:25px;letter-spacing:-1px;margin:0 0 5px}.intro{font-size:15px;color:#596574;margin:0 0 14px;line-height:1.45}.card{background:white;padding:17px;border-radius:20px;margin-bottom:10px}h2{font-size:18px;margin:0 0 12px;letter-spacing:-.5px}.unit{font-size:13px;color:#596574;font-weight:400;float:right;margin-top:3px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px 14px}label{font-size:15px;font-weight:600;display:block}.hint{font-size:12px;font-weight:400;color:#596574;display:block;margin-top:2px}.field{display:flex;align-items:center;border-bottom:1px solid #c5cdd7;margin-top:3px;gap:4px}.field:focus-within{border-color:#2266e8;box-shadow:0 1px #2266e8}input{min-width:0;width:100%;height:42px;background:none;border:0;outline:0;color:#191f28;font:600 20px system-ui;text-align:right}input::placeholder{color:#9aa4b1;font-size:16px;font-weight:400}.field span{font-size:13px;color:#596574;white-space:nowrap}.line{display:flex;justify-content:space-between;gap:10px;align-items:center;font-size:15px}.line strong{font-size:22px;letter-spacing:-.5px;overflow-wrap:anywhere;text-align:right}.sub{font-size:14px;color:#596574;line-height:1.5;margin:8px 0 0}.blue{color:#2266e8}.purchase{display:flex;align-items:center;gap:14px}.purchase label{flex:1}.purchase .field{width:48%;margin:0}.answer{font-size:20px;line-height:1.35;letter-spacing:-.5px;margin:13px 0 0;font-weight:750}.fine{font-size:12px;line-height:1.5;color:#596574;margin:8px 3px}.warn{color:#ad4615}.safe{color:#2266e8}
@media(max-height:760px){body{padding:10px 13px}.intro{margin-bottom:10px}.card{padding:13px 15px;margin-bottom:8px}h2{margin-bottom:9px}.grid{gap:8px 13px}input{height:37px}.answer{margin-top:9px;font-size:19px}.sub{margin-top:6px}.fine{font-size:11px;margin-top:6px}h1{font-size:23px}}

/* 토닥곰 캐릭터는 CSS 그림으로, 추가 이미지 파일 없이 표시됩니다. */
html,body{color:#243d36}body{padding:12px 14px}h1{font-size:25px;color:#214e40}.hero{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:10px}.hero .intro{margin:4px 0 0;font-size:14px}.card{border-radius:25px;padding:15px 16px;box-shadow:0 3px 16px #245c3e06}.field{background:#f3f7f5;border:1px solid transparent;border-radius:13px;padding:0 9px;margin-top:6px}.field:focus-within{border-color:#25856b;box-shadow:0 0 0 2px #25856b18}.field input{height:40px}input::placeholder{color:#6f8079}.hint{color:#5a7067}.sub,.fine,.unit,.field span{color:#536b61}.safe,.blue{color:#19745b}.answer{font-size:19px}.summary{background:#e3f3ec}.saving{margin-top:10px;background:#fff4d9;border-radius:15px;padding:10px 12px;font-size:14px;color:#624d24;line-height:1.5}.saving strong{color:#51401e}.pig-wrap{width:82px;height:76px;position:relative;flex-shrink:0}.pig{position:absolute;left:6px;top:23px;width:70px;height:47px;background:#ffd7ce;border-radius:45% 48% 44% 42%;box-shadow:inset -5px -5px #f7bdaf}.pig:before{content:'';position:absolute;width:17px;height:20px;background:#ffc8bb;left:17px;top:-10px;border-radius:8px 12px 0 0;transform:rotate(-20deg)}.pig:after{content:'';position:absolute;width:24px;height:17px;right:-6px;top:20px;border-radius:50%;background:#ffb9a8}.eye{position:absolute;width:4px;height:5px;background:#5e4d42;right:16px;top:14px;border-radius:50%;z-index:1}.smile{position:absolute;width:10px;height:6px;border:solid #865f4c;border-width:0 0 2px;border-radius:50%;left:30px;top:26px}.feet{position:absolute;bottom:-3px;left:13px;width:10px;height:9px;background:#efb3a3;border-radius:0 0 5px 5px;box-shadow:35px 0 #efb3a3}.coin{position:absolute;left:32px;top:0;width:22px;height:22px;background:#f8cf6b;border:3px solid #ffe7a6;border-radius:50%;color:#866216;font-size:11px;line-height:16px;text-align:center;font-weight:700}.fine{font-size:11px;line-height:1.45}.grid{gap:10px 12px}
@media(max-height:760px){body{padding:8px 12px}.hero{margin-bottom:8px}.card{padding:11px 14px;margin-bottom:8px}.field input{height:36px}.hint{font-size:11px}.saving{padding:8px 10px;margin-top:8px}.pig-wrap{height:68px}.pig{top:18px}.coin{top:-3px}.grid{gap:7px 12px}.hero .intro{font-size:13px}h1{font-size:24px}}

.pig{left:9px;top:20px;width:65px;height:55px;background:#c9976b;border-radius:46%;box-shadow:inset -4px -3px #b78660}
.pig:before{width:21px;height:21px;left:0;top:-8px;background:#c9976b;border:5px solid #b78660;border-radius:50%;transform:none}
.pig:after{width:21px;height:21px;right:0;top:-8px;background:#c9976b;border:5px solid #b78660;border-radius:50%}
.eye{right:16px;top:21px;background:#3f3028;box-shadow:-28px 0 #3f3028}
.smile{left:21px;top:29px;width:23px;height:17px;border:0;background:#f6dfc5;border-radius:50%;z-index:2}
.smile:before{content:'';position:absolute;left:8px;top:3px;width:7px;height:5px;border-radius:50%;background:#513d30}
.smile:after{content:'';position:absolute;left:8px;top:8px;width:7px;height:5px;border-bottom:2px solid #513d30;border-radius:50%}
.feet{display:none}.coin{left:31px;top:-2px;z-index:3}

.periods{display:flex;gap:8px;margin-top:12px}.periods button{flex:1;border:0;border-radius:13px;background:#edf3f0;color:#426254;padding:10px 4px;font-size:15px;font-weight:650;cursor:pointer}.periods .selected{background:#22795f;color:white}.tiny{font-size:11px;color:#536b61;text-align:center;margin:6px 0}dialog{border:0;border-radius:28px;padding:0;max-width:370px;width:calc(100% - 32px);color:#243d36;background:#fff;max-height:92svh;overflow:auto}dialog::backdrop{background:#19382d66}.welcome-inner{padding:24px 20px;text-align:center}.welcome-bear{font-size:62px}.welcome-inner h2{font-size:23px;margin:10px 0 22px}.steps{display:flex;align-items:center;justify-content:space-between;gap:5px}.steps div{flex:1}.steps span{display:block;font-size:32px;margin-bottom:9px}.steps b{font-size:13px}.steps i{font-style:normal;color:#90a99c}.welcome-inner p{font-size:14px;color:#536b61;margin:20px 0}.welcome-inner #start{width:100%;border:0;background:#22795f;color:white;font-size:18px;font-weight:700;padding:15px;border-radius:17px;cursor:pointer}.welcome-inner .terms{font-size:11px;line-height:1.6;margin:14px 0 0}button:focus-visible{outline:3px solid #e9b94e;outline-offset:3px}
</style></head><body><main>
<header class="hero"><div><h1>토닥곰</h1><p class="intro">차곡차곡, 함께 해요.</p></div><div class="pig-wrap" role="img" aria-label="동전을 모으는 웃는 곰, 토닥곰"><div class="coin">₩</div><div class="pig"><i class="eye"></i><i class="smile"></i><i class="feet"></i></div></div></header>
<section class="card" aria-labelledby="entry"><h2 id="entry">내 돈을 알려주세요 <span class="unit">단위: 만원</span></h2>
<div class="grid">
<label for="cash">통장에 있는 돈<div class="field"><input id="cash" type="text" inputmode="decimal" maxlength="12" placeholder="예: 500" autocomplete="off"><span>만원</span></div></label>
<label for="invest">주식·펀드<div class="field"><input id="invest" type="text" inputmode="decimal" maxlength="12" placeholder="없으면 0" autocomplete="off"><span>만원</span></div></label>
<label for="locked">집·보증금<div class="field"><input id="locked" type="text" inputmode="decimal" maxlength="12" placeholder="없으면 0" autocomplete="off"><span>만원</span></div></label>
<label for="debt">갚을 돈<div class="field"><input id="debt" type="text" inputmode="decimal" maxlength="12" placeholder="없으면 0" autocomplete="off"><span>만원</span></div></label>
</div></section>
<section class="card summary" aria-live="polite" aria-atomic="true"><div class="line"><span>빚을 뺀 내 재산</span><strong id="net">—</strong></div><p class="sub" id="liquid">통장 잔액부터 적어 주세요.</p></section>
<section class="card" aria-labelledby="buy"><h2 id="buy">사기 전에, 잠깐만요</h2>
<div class="grid"><label for="monthly">한 달 꼭 쓰는 돈<div class="field"><input id="monthly" type="text" inputmode="decimal" maxlength="12" placeholder="예: 150" autocomplete="off"><span>만원</span></div></label>
<label for="price">사고 싶은 물건값<div class="field"><input id="price" type="text" inputmode="decimal" maxlength="12" placeholder="예: 100" autocomplete="off"><span>만원</span></div></label></div>
<div role="status" aria-live="polite" aria-atomic="true"><p class="answer" id="answer">두 금액을 적어 주세요</p><p class="sub" id="detail">생활비 3개월치가 남는지 확인해요.</p></div>
<div class="periods" aria-label="저축 기간"><button type="button" data-month="3" aria-pressed="false">3개월</button><button type="button" data-month="6" aria-pressed="false">6개월</button><button type="button" data-month="12" aria-pressed="true" class="selected">1년</button></div><div class="saving" id="saving" aria-live="polite">🌱 물건값을 적으면, 모아서 사는 방법도 알려드려요.</div>
</section>


<p class="tiny">만원 단위 · 기기에 저장 안 함 · 참고용 계산</p>
</main>
<dialog id="welcome" aria-labelledby="welcomeTitle"><div class="welcome-inner"><div class="welcome-bear" aria-hidden="true">🐻</div><h2 id="welcomeTitle">토닥곰과 시작해요</h2><div class="steps"><div><span>👛</span><b>내 돈 적기</b></div><i>→</i><div><span>🛍️</span><b>물건값 적기</b></div><i>→</i><div><span>🌱</span><b>모을 돈 확인</b></div></div><p>금액만 적으면, 토닥곰이 계산해요.</p><button id="start" type="button">시작하기</button><p class="terms">현금 일시불 기준 · 생활비 3개월치와 비교<br>집값은 빚을 빼기 전 금액 · 같은 돈은 한 번만<br>수입·세금·자산 매각 제외 · 적금 가입 기능 없음</p></div></dialog>
<script>
'use strict';
const ids=['cash','invest','locked','debt','monthly','price'];
const el=id=>document.getElementById(id);
const money=n=>n.toLocaleString('ko-KR',{maximumFractionDigits:2})+'만원';
const round=n=>Math.round(n*100)/100;
function analyze(c,i,l,d,m,p){const total=round(c+i+l);const after=round(c-p);const target=round(m*3);return {total,net:round(total-d),ratio:total>0?c/total*100:null,after,target,shortage:round(Math.max(0,target-after)),limit:round(Math.max(0,c-target)),state:after<0?'short':m<=0?'missing':after<target?'reserve':'ok'};}
let timer; let savingMonths=12;
function update(){
 const vals=ids.map(id=>Number(el(id).value)||0);const [c,i,l,d,m,p]=vals;
 const monthlyGoal=Math.ceil((p/savingMonths)*100)/100;
 el('saving').textContent=el('price').value!==''&&p>0?'🌱 매달 '+money(monthlyGoal)+' × '+savingMonths+'개월 · 이자 제외':'🌱 물건값을 적어 주세요';
 const a=analyze(...vals);const any=ids.slice(0,4).some(id=>el(id).value!=='');
 el('net').textContent=any?money(a.net):'—';
 el('liquid').textContent=a.total>0?'바로 쓸 돈 '+money(c)+' · '+a.ratio.toLocaleString('ko-KR',{maximumFractionDigits:1})+'%':any?'현재 바로 쓸 수 있는 돈은 0원이에요.':'통장 잔액부터 적어 주세요.';
 if(a.net<0)el('liquid').textContent+=' 빚이 더 많아요.';
 const answer=el('answer'),detail=el('detail');answer.className='answer';
 if(el('cash').value===''){answer.textContent='통장에 있는 돈부터 적어 주세요';detail.textContent='현금 기준으로 확인해요.';return;}
 if(el('monthly').value===''||el('price').value===''){answer.textContent='생활비와 물건값을 적어 주세요';detail.textContent='생활비 3개월치가 남는지 확인해요.';return;}
 if(a.state==='short'){answer.textContent='통장에 '+money(-a.after)+'이 부족해요';answer.classList.add('warn');detail.textContent='통장 잔액 기준이에요.';return;}
 if(a.state==='missing'){answer.textContent='구매 후 '+money(a.after)+'이 남아요';detail.textContent='생활비를 0보다 크게 적어 주세요.';return;}
 if(a.state==='reserve'){answer.textContent='조금 더 모아볼까요?';answer.classList.add('warn');detail.textContent='구매 후 '+money(a.after)+' · 비상금 '+money(a.shortage)+' 부족';}
 else{answer.textContent='생활비 여유가 남아요';answer.classList.add('safe');detail.textContent='구매 후 '+money(a.after)+' · 비상금 기준 '+money(a.target);}
}
ids.forEach(id=>el(id).addEventListener('input',()=>{let v=el(id).value.replace(/[^0-9.]/g,'');const parts=v.split('.');v=parts[0].slice(0,8)+(parts.length>1?'.'+parts.slice(1).join('').slice(0,2):'');if(v!==el(id).value)el(id).value=v;clearTimeout(timer);timer=setTimeout(update,220);}));
document.querySelectorAll('[data-month]').forEach(b=>b.addEventListener('click',()=>{savingMonths=Number(b.dataset.month);document.querySelectorAll('[data-month]').forEach(x=>{x.classList.toggle('selected',x===b);x.setAttribute('aria-pressed',String(x===b));});update();}));
const welcome=el('welcome');el('start').addEventListener('click',()=>{welcome.close();el('cash').focus();});
update();welcome.showModal();
</script></body></html>'''
components.html(PAGE, height=850, scrolling=True)
