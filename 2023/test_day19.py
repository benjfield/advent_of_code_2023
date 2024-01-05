from day19 import *

test_text=r"""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""  

def test_workflow_1():
    assert workflow_1(test_text) == 19114
    
def test_workflow_2():
    assert workflow_2(test_text) == 167409079868000

stress_test=r"""in{x<2:R,ab}
ab{x<3:ash,ac}
ac{x<4:R,ad}
ad{x<5:ash,ae}
ae{x<6:R,af}
af{x<7:ash,ag}
ag{x<8:R,ah}
ah{x<9:ash,ai}
ai{x<10:R,aj}
aj{x<11:ash,ak}
ak{x<12:R,al}
al{x<13:ash,am}
am{x<14:R,an}
an{x<15:ash,ao}
ao{x<16:R,ap}
ap{x<17:ash,aq}
aq{x<18:R,ar}
ar{x<19:ash,as}
as{x<20:R,at}
at{x<21:ash,au}
au{x<22:R,av}
av{x<23:ash,aw}
aw{x<24:R,ax}
ax{x<25:ash,ay}
ay{x<26:R,az}
az{x<27:ash,aab}
aab{x<28:R,abb}
abb{x<29:ash,acb}
acb{x<30:R,adb}
adb{x<31:ash,aeb}
aeb{x<32:R,afb}
afb{x<33:ash,agb}
agb{x<34:R,ahb}
ahb{x<35:ash,aib}
aib{x<36:R,ajb}
ajb{x<37:ash,akb}
akb{x<38:R,alb}
alb{x<39:ash,amb}
amb{x<40:R,anb}
anb{x<41:ash,aob}
aob{x<42:R,apb}
apb{x<43:ash,aqb}
aqb{x<44:R,arb}
arb{x<45:ash,asb}
asb{x<46:R,atb}
atb{x<47:ash,aub}
aub{x<48:R,avb}
avb{x<49:ash,awb}
awb{x<50:R,axb}
axb{x<51:ash,ayb}
ayb{x<52:R,azb}
azb{x<53:ash,aac}
aac{x<54:R,abc}
abc{x<55:ash,acc}
acc{x<56:R,adc}
adc{x<57:ash,aec}
aec{x<58:R,afc}
afc{x<59:ash,agc}
agc{x<60:R,ahc}
ahc{x<61:ash,aic}
aic{x<62:R,ajc}
ajc{x<63:ash,akc}
akc{x<64:R,alc}
alc{x<65:ash,amc}
amc{x<66:R,anc}
anc{x<67:ash,aoc}
aoc{x<68:R,apc}
apc{x<69:ash,aqc}
aqc{x<70:R,arc}
arc{x<71:ash,asc}
asc{x<72:R,atc}
atc{x<73:ash,auc}
auc{x<74:R,avc}
avc{x<75:ash,awc}
awc{x<76:R,axc}
axc{x<77:ash,ayc}
ayc{x<78:R,azc}
azc{x<79:ash,aad}
aad{x<80:R,abd}
abd{x<81:ash,acd}
acd{x<82:R,add}
add{x<83:ash,aed}
aed{x<84:R,afd}
afd{x<85:ash,agd}
agd{x<86:R,ahd}
ahd{x<87:ash,aid}
aid{x<88:R,ajd}
ajd{x<89:ash,akd}
akd{x<90:R,ald}
ald{x<91:ash,amd}
amd{x<92:R,and}
and{x<93:ash,aod}
aod{x<94:R,apd}
apd{x<95:ash,aqd}
aqd{x<96:R,ard}
ard{x<97:ash,asd}
asd{x<98:R,atd}
atd{x<99:ash,aud}
aud{x<100:R,avd}
avd{x<101:ash,awd}
awd{x<102:R,axd}
axd{x<103:ash,ayd}
ayd{x<104:R,azd}
azd{x<105:ash,aae}
aae{x<106:R,abe}
abe{x<107:ash,ace}
ace{x<108:R,ade}
ade{x<109:ash,aee}
aee{x<110:R,afe}
afe{x<111:ash,age}
age{x<112:R,ahe}
ahe{x<113:ash,aie}
aie{x<114:R,aje}
aje{x<115:ash,ake}
ake{x<116:R,ale}
ale{x<117:ash,ame}
ame{x<118:R,ane}
ane{x<119:ash,aoe}
aoe{x<120:R,ape}
ape{x<121:ash,aqe}
aqe{x<122:R,are}
are{x<123:ash,ase}
ase{x<124:R,ate}
ate{x<125:ash,aue}
aue{x<126:R,ave}
ave{x<127:ash,awe}
awe{x<128:R,axe}
axe{x<129:ash,aye}
aye{x<130:R,aze}
aze{x<131:ash,aaf}
aaf{x<132:R,abf}
abf{x<133:ash,acf}
acf{x<134:R,adf}
adf{x<135:ash,aef}
aef{x<136:R,aff}
aff{x<137:ash,agf}
agf{x<138:R,ahf}
ahf{x<139:ash,aif}
aif{x<140:R,ajf}
ajf{x<141:ash,akf}
akf{x<142:R,alf}
alf{x<143:ash,amf}
amf{x<144:R,anf}
anf{x<145:ash,aof}
aof{x<146:R,apf}
apf{x<147:ash,aqf}
aqf{x<148:R,arf}
arf{x<149:ash,asf}
asf{x<150:R,atf}
atf{x<151:ash,auf}
auf{x<152:R,avf}
avf{x<153:ash,awf}
awf{x<154:R,axf}
axf{x<155:ash,ayf}
ayf{x<156:R,azf}
azf{x<157:ash,aag}
aag{x<158:R,abg}
abg{x<159:ash,acg}
acg{x<160:R,adg}
adg{x<161:ash,aeg}
aeg{x<162:R,afg}
afg{x<163:ash,agg}
agg{x<164:R,ahg}
ahg{x<165:ash,aig}
aig{x<166:R,ajg}
ajg{x<167:ash,akg}
akg{x<168:R,alg}
alg{x<169:ash,amg}
amg{x<170:R,ang}
ang{x<171:ash,aog}
aog{x<172:R,apg}
apg{x<173:ash,aqg}
aqg{x<174:R,arg}
arg{x<175:ash,asg}
asg{x<176:R,atg}
atg{x<177:ash,aug}
aug{x<178:R,avg}
avg{x<179:ash,awg}
awg{x<180:R,axg}
axg{x<181:ash,ayg}
ayg{x<182:R,azg}
azg{x<183:ash,aah}
aah{x<184:R,abh}
abh{x<185:ash,ach}
ach{x<186:R,adh}
adh{x<187:ash,aeh}
aeh{x<188:R,afh}
afh{x<189:ash,agh}
agh{x<190:R,ahh}
ahh{x<191:ash,aih}
aih{x<192:R,ajh}
ajh{x<193:ash,akh}
akh{x<194:R,alh}
alh{x<195:ash,amh}
amh{x<196:R,anh}
anh{x<197:ash,aoh}
aoh{x<198:R,aph}
aph{x<199:ash,aqh}
aqh{x<200:R,arh}
arh{x<201:ash,ash}
ash{m<2:R,ath}
ath{m<3:akp,auh}
auh{m<4:R,avh}
avh{m<5:akp,awh}
awh{m<6:R,axh}
axh{m<7:akp,ayh}
ayh{m<8:R,azh}
azh{m<9:akp,aai}
aai{m<10:R,abi}
abi{m<11:akp,aci}
aci{m<12:R,adi}
adi{m<13:akp,aei}
aei{m<14:R,afi}
afi{m<15:akp,agi}
agi{m<16:R,ahi}
ahi{m<17:akp,aii}
aii{m<18:R,aji}
aji{m<19:akp,aki}
aki{m<20:R,ali}
ali{m<21:akp,ami}
ami{m<22:R,ani}
ani{m<23:akp,aoi}
aoi{m<24:R,api}
api{m<25:akp,aqi}
aqi{m<26:R,ari}
ari{m<27:akp,asi}
asi{m<28:R,ati}
ati{m<29:akp,aui}
aui{m<30:R,avi}
avi{m<31:akp,awi}
awi{m<32:R,axi}
axi{m<33:akp,ayi}
ayi{m<34:R,azi}
azi{m<35:akp,aaj}
aaj{m<36:R,abj}
abj{m<37:akp,acj}
acj{m<38:R,adj}
adj{m<39:akp,aej}
aej{m<40:R,afj}
afj{m<41:akp,agj}
agj{m<42:R,ahj}
ahj{m<43:akp,aij}
aij{m<44:R,ajj}
ajj{m<45:akp,akj}
akj{m<46:R,alj}
alj{m<47:akp,amj}
amj{m<48:R,anj}
anj{m<49:akp,aoj}
aoj{m<50:R,apj}
apj{m<51:akp,aqj}
aqj{m<52:R,arj}
arj{m<53:akp,asj}
asj{m<54:R,atj}
atj{m<55:akp,auj}
auj{m<56:R,avj}
avj{m<57:akp,awj}
awj{m<58:R,axj}
axj{m<59:akp,ayj}
ayj{m<60:R,azj}
azj{m<61:akp,aak}
aak{m<62:R,abk}
abk{m<63:akp,ack}
ack{m<64:R,adk}
adk{m<65:akp,aek}
aek{m<66:R,afk}
afk{m<67:akp,agk}
agk{m<68:R,ahk}
ahk{m<69:akp,aik}
aik{m<70:R,ajk}
ajk{m<71:akp,akk}
akk{m<72:R,alk}
alk{m<73:akp,amk}
amk{m<74:R,ank}
ank{m<75:akp,aok}
aok{m<76:R,apk}
apk{m<77:akp,aqk}
aqk{m<78:R,ark}
ark{m<79:akp,ask}
ask{m<80:R,atk}
atk{m<81:akp,auk}
auk{m<82:R,avk}
avk{m<83:akp,awk}
awk{m<84:R,axk}
axk{m<85:akp,ayk}
ayk{m<86:R,azk}
azk{m<87:akp,aal}
aal{m<88:R,abl}
abl{m<89:akp,acl}
acl{m<90:R,adl}
adl{m<91:akp,ael}
ael{m<92:R,afl}
afl{m<93:akp,agl}
agl{m<94:R,ahl}
ahl{m<95:akp,ail}
ail{m<96:R,ajl}
ajl{m<97:akp,akl}
akl{m<98:R,all}
all{m<99:akp,aml}
aml{m<100:R,anl}
anl{m<101:akp,aol}
aol{m<102:R,apl}
apl{m<103:akp,aql}
aql{m<104:R,arl}
arl{m<105:akp,asl}
asl{m<106:R,atl}
atl{m<107:akp,aul}
aul{m<108:R,avl}
avl{m<109:akp,awl}
awl{m<110:R,axl}
axl{m<111:akp,ayl}
ayl{m<112:R,azl}
azl{m<113:akp,aam}
aam{m<114:R,abm}
abm{m<115:akp,acm}
acm{m<116:R,adm}
adm{m<117:akp,aem}
aem{m<118:R,afm}
afm{m<119:akp,agm}
agm{m<120:R,ahm}
ahm{m<121:akp,aim}
aim{m<122:R,ajm}
ajm{m<123:akp,akm}
akm{m<124:R,alm}
alm{m<125:akp,amm}
amm{m<126:R,anm}
anm{m<127:akp,aom}
aom{m<128:R,apm}
apm{m<129:akp,aqm}
aqm{m<130:R,arm}
arm{m<131:akp,asm}
asm{m<132:R,atm}
atm{m<133:akp,aum}
aum{m<134:R,avm}
avm{m<135:akp,awm}
awm{m<136:R,axm}
axm{m<137:akp,aym}
aym{m<138:R,azm}
azm{m<139:akp,aan}
aan{m<140:R,abn}
abn{m<141:akp,acn}
acn{m<142:R,adn}
adn{m<143:akp,aen}
aen{m<144:R,afn}
afn{m<145:akp,agn}
agn{m<146:R,ahn}
ahn{m<147:akp,ain}
ain{m<148:R,ajn}
ajn{m<149:akp,akn}
akn{m<150:R,aln}
aln{m<151:akp,amn}
amn{m<152:R,ann}
ann{m<153:akp,aon}
aon{m<154:R,apn}
apn{m<155:akp,aqn}
aqn{m<156:R,arn}
arn{m<157:akp,asn}
asn{m<158:R,atn}
atn{m<159:akp,aun}
aun{m<160:R,avn}
avn{m<161:akp,awn}
awn{m<162:R,axn}
axn{m<163:akp,ayn}
ayn{m<164:R,azn}
azn{m<165:akp,aao}
aao{m<166:R,abo}
abo{m<167:akp,aco}
aco{m<168:R,ado}
ado{m<169:akp,aeo}
aeo{m<170:R,afo}
afo{m<171:akp,ago}
ago{m<172:R,aho}
aho{m<173:akp,aio}
aio{m<174:R,ajo}
ajo{m<175:akp,ako}
ako{m<176:R,alo}
alo{m<177:akp,amo}
amo{m<178:R,ano}
ano{m<179:akp,aoo}
aoo{m<180:R,apo}
apo{m<181:akp,aqo}
aqo{m<182:R,aro}
aro{m<183:akp,aso}
aso{m<184:R,ato}
ato{m<185:akp,auo}
auo{m<186:R,avo}
avo{m<187:akp,awo}
awo{m<188:R,axo}
axo{m<189:akp,ayo}
ayo{m<190:R,azo}
azo{m<191:akp,aap}
aap{m<192:R,abp}
abp{m<193:akp,acp}
acp{m<194:R,adp}
adp{m<195:akp,aep}
aep{m<196:R,afp}
afp{m<197:akp,agp}
agp{m<198:R,ahp}
ahp{m<199:akp,aip}
aip{m<200:R,ajp}
ajp{m<201:akp,akp}
akp{a<2:R,alp}
alp{a<3:acx,amp}
amp{a<4:R,anp}
anp{a<5:acx,aop}
aop{a<6:R,app}
app{a<7:acx,aqp}
aqp{a<8:R,arp}
arp{a<9:acx,asp}
asp{a<10:R,atp}
atp{a<11:acx,aup}
aup{a<12:R,avp}
avp{a<13:acx,awp}
awp{a<14:R,axp}
axp{a<15:acx,ayp}
ayp{a<16:R,azp}
azp{a<17:acx,aaq}
aaq{a<18:R,abq}
abq{a<19:acx,acq}
acq{a<20:R,adq}
adq{a<21:acx,aeq}
aeq{a<22:R,afq}
afq{a<23:acx,agq}
agq{a<24:R,ahq}
ahq{a<25:acx,aiq}
aiq{a<26:R,ajq}
ajq{a<27:acx,akq}
akq{a<28:R,alq}
alq{a<29:acx,amq}
amq{a<30:R,anq}
anq{a<31:acx,aoq}
aoq{a<32:R,apq}
apq{a<33:acx,aqq}
aqq{a<34:R,arq}
arq{a<35:acx,asq}
asq{a<36:R,atq}
atq{a<37:acx,auq}
auq{a<38:R,avq}
avq{a<39:acx,awq}
awq{a<40:R,axq}
axq{a<41:acx,ayq}
ayq{a<42:R,azq}
azq{a<43:acx,aar}
aar{a<44:R,abr}
abr{a<45:acx,acr}
acr{a<46:R,adr}
adr{a<47:acx,aer}
aer{a<48:R,afr}
afr{a<49:acx,agr}
agr{a<50:R,ahr}
ahr{a<51:acx,air}
air{a<52:R,ajr}
ajr{a<53:acx,akr}
akr{a<54:R,alr}
alr{a<55:acx,amr}
amr{a<56:R,anr}
anr{a<57:acx,aor}
aor{a<58:R,apr}
apr{a<59:acx,aqr}
aqr{a<60:R,arr}
arr{a<61:acx,asr}
asr{a<62:R,atr}
atr{a<63:acx,aur}
aur{a<64:R,avr}
avr{a<65:acx,awr}
awr{a<66:R,axr}
axr{a<67:acx,ayr}
ayr{a<68:R,azr}
azr{a<69:acx,aas}
aas{a<70:R,abs}
abs{a<71:acx,acs}
acs{a<72:R,ads}
ads{a<73:acx,aes}
aes{a<74:R,afs}
afs{a<75:acx,ags}
ags{a<76:R,ahs}
ahs{a<77:acx,ais}
ais{a<78:R,ajs}
ajs{a<79:acx,aks}
aks{a<80:R,als}
als{a<81:acx,ams}
ams{a<82:R,ans}
ans{a<83:acx,aos}
aos{a<84:R,aps}
aps{a<85:acx,aqs}
aqs{a<86:R,ars}
ars{a<87:acx,ass}
ass{a<88:R,ats}
ats{a<89:acx,aus}
aus{a<90:R,avs}
avs{a<91:acx,aws}
aws{a<92:R,axs}
axs{a<93:acx,ays}
ays{a<94:R,azs}
azs{a<95:acx,aat}
aat{a<96:R,abt}
abt{a<97:acx,act}
act{a<98:R,adt}
adt{a<99:acx,aet}
aet{a<100:R,aft}
aft{a<101:acx,agt}
agt{a<102:R,aht}
aht{a<103:acx,ait}
ait{a<104:R,ajt}
ajt{a<105:acx,akt}
akt{a<106:R,alt}
alt{a<107:acx,amt}
amt{a<108:R,ant}
ant{a<109:acx,aot}
aot{a<110:R,apt}
apt{a<111:acx,aqt}
aqt{a<112:R,art}
art{a<113:acx,ast}
ast{a<114:R,att}
att{a<115:acx,aut}
aut{a<116:R,avt}
avt{a<117:acx,awt}
awt{a<118:R,axt}
axt{a<119:acx,ayt}
ayt{a<120:R,azt}
azt{a<121:acx,aau}
aau{a<122:R,abu}
abu{a<123:acx,acu}
acu{a<124:R,adu}
adu{a<125:acx,aeu}
aeu{a<126:R,afu}
afu{a<127:acx,agu}
agu{a<128:R,ahu}
ahu{a<129:acx,aiu}
aiu{a<130:R,aju}
aju{a<131:acx,aku}
aku{a<132:R,alu}
alu{a<133:acx,amu}
amu{a<134:R,anu}
anu{a<135:acx,aou}
aou{a<136:R,apu}
apu{a<137:acx,aqu}
aqu{a<138:R,aru}
aru{a<139:acx,asu}
asu{a<140:R,atu}
atu{a<141:acx,auu}
auu{a<142:R,avu}
avu{a<143:acx,awu}
awu{a<144:R,axu}
axu{a<145:acx,ayu}
ayu{a<146:R,azu}
azu{a<147:acx,aav}
aav{a<148:R,abv}
abv{a<149:acx,acv}
acv{a<150:R,adv}
adv{a<151:acx,aev}
aev{a<152:R,afv}
afv{a<153:acx,agv}
agv{a<154:R,ahv}
ahv{a<155:acx,aiv}
aiv{a<156:R,ajv}
ajv{a<157:acx,akv}
akv{a<158:R,alv}
alv{a<159:acx,amv}
amv{a<160:R,anv}
anv{a<161:acx,aov}
aov{a<162:R,apv}
apv{a<163:acx,aqv}
aqv{a<164:R,arv}
arv{a<165:acx,asv}
asv{a<166:R,atv}
atv{a<167:acx,auv}
auv{a<168:R,avv}
avv{a<169:acx,awv}
awv{a<170:R,axv}
axv{a<171:acx,ayv}
ayv{a<172:R,azv}
azv{a<173:acx,aaw}
aaw{a<174:R,abw}
abw{a<175:acx,acw}
acw{a<176:R,adw}
adw{a<177:acx,aew}
aew{a<178:R,afw}
afw{a<179:acx,agw}
agw{a<180:R,ahw}
ahw{a<181:acx,aiw}
aiw{a<182:R,ajw}
ajw{a<183:acx,akw}
akw{a<184:R,alw}
alw{a<185:acx,amw}
amw{a<186:R,anw}
anw{a<187:acx,aow}
aow{a<188:R,apw}
apw{a<189:acx,aqw}
aqw{a<190:R,arw}
arw{a<191:acx,asw}
asw{a<192:R,atw}
atw{a<193:acx,auw}
auw{a<194:R,avw}
avw{a<195:acx,aww}
aww{a<196:R,axw}
axw{a<197:acx,ayw}
ayw{a<198:R,azw}
azw{a<199:acx,aax}
aax{a<200:R,abx}
abx{a<201:acx,acx}
acx{s<2:R,adx}
adx{s<3:aueb,aex}
aex{s<4:R,afx}
afx{s<5:aueb,agx}
agx{s<6:R,ahx}
ahx{s<7:aueb,aix}
aix{s<8:R,ajx}
ajx{s<9:aueb,akx}
akx{s<10:R,alx}
alx{s<11:aueb,amx}
amx{s<12:R,anx}
anx{s<13:aueb,aox}
aox{s<14:R,apx}
apx{s<15:aueb,aqx}
aqx{s<16:R,arx}
arx{s<17:aueb,asx}
asx{s<18:R,atx}
atx{s<19:aueb,aux}
aux{s<20:R,avx}
avx{s<21:aueb,awx}
awx{s<22:R,axx}
axx{s<23:aueb,ayx}
ayx{s<24:R,azx}
azx{s<25:aueb,aay}
aay{s<26:R,aby}
aby{s<27:aueb,acy}
acy{s<28:R,ady}
ady{s<29:aueb,aey}
aey{s<30:R,afy}
afy{s<31:aueb,agy}
agy{s<32:R,ahy}
ahy{s<33:aueb,aiy}
aiy{s<34:R,ajy}
ajy{s<35:aueb,aky}
aky{s<36:R,aly}
aly{s<37:aueb,amy}
amy{s<38:R,any}
any{s<39:aueb,aoy}
aoy{s<40:R,apy}
apy{s<41:aueb,aqy}
aqy{s<42:R,ary}
ary{s<43:aueb,asy}
asy{s<44:R,aty}
aty{s<45:aueb,auy}
auy{s<46:R,avy}
avy{s<47:aueb,awy}
awy{s<48:R,axy}
axy{s<49:aueb,ayy}
ayy{s<50:R,azy}
azy{s<51:aueb,aaz}
aaz{s<52:R,abz}
abz{s<53:aueb,acz}
acz{s<54:R,adz}
adz{s<55:aueb,aez}
aez{s<56:R,afz}
afz{s<57:aueb,agz}
agz{s<58:R,ahz}
ahz{s<59:aueb,aiz}
aiz{s<60:R,ajz}
ajz{s<61:aueb,akz}
akz{s<62:R,alz}
alz{s<63:aueb,amz}
amz{s<64:R,anz}
anz{s<65:aueb,aoz}
aoz{s<66:R,apz}
apz{s<67:aueb,aqz}
aqz{s<68:R,arz}
arz{s<69:aueb,asz}
asz{s<70:R,atz}
atz{s<71:aueb,auz}
auz{s<72:R,avz}
avz{s<73:aueb,awz}
awz{s<74:R,axz}
axz{s<75:aueb,ayz}
ayz{s<76:R,azz}
azz{s<77:aueb,aaab}
aaab{s<78:R,abab}
abab{s<79:aueb,acab}
acab{s<80:R,adab}
adab{s<81:aueb,aeab}
aeab{s<82:R,afab}
afab{s<83:aueb,agab}
agab{s<84:R,ahab}
ahab{s<85:aueb,aiab}
aiab{s<86:R,ajab}
ajab{s<87:aueb,akab}
akab{s<88:R,alab}
alab{s<89:aueb,amab}
amab{s<90:R,anab}
anab{s<91:aueb,aoab}
aoab{s<92:R,apab}
apab{s<93:aueb,aqab}
aqab{s<94:R,arab}
arab{s<95:aueb,asab}
asab{s<96:R,atab}
atab{s<97:aueb,auab}
auab{s<98:R,avab}
avab{s<99:aueb,awab}
awab{s<100:R,axab}
axab{s<101:aueb,ayab}
ayab{s<102:R,azab}
azab{s<103:aueb,aabb}
aabb{s<104:R,abbb}
abbb{s<105:aueb,acbb}
acbb{s<106:R,adbb}
adbb{s<107:aueb,aebb}
aebb{s<108:R,afbb}
afbb{s<109:aueb,agbb}
agbb{s<110:R,ahbb}
ahbb{s<111:aueb,aibb}
aibb{s<112:R,ajbb}
ajbb{s<113:aueb,akbb}
akbb{s<114:R,albb}
albb{s<115:aueb,ambb}
ambb{s<116:R,anbb}
anbb{s<117:aueb,aobb}
aobb{s<118:R,apbb}
apbb{s<119:aueb,aqbb}
aqbb{s<120:R,arbb}
arbb{s<121:aueb,asbb}
asbb{s<122:R,atbb}
atbb{s<123:aueb,aubb}
aubb{s<124:R,avbb}
avbb{s<125:aueb,awbb}
awbb{s<126:R,axbb}
axbb{s<127:aueb,aybb}
aybb{s<128:R,azbb}
azbb{s<129:aueb,aacb}
aacb{s<130:R,abcb}
abcb{s<131:aueb,accb}
accb{s<132:R,adcb}
adcb{s<133:aueb,aecb}
aecb{s<134:R,afcb}
afcb{s<135:aueb,agcb}
agcb{s<136:R,ahcb}
ahcb{s<137:aueb,aicb}
aicb{s<138:R,ajcb}
ajcb{s<139:aueb,akcb}
akcb{s<140:R,alcb}
alcb{s<141:aueb,amcb}
amcb{s<142:R,ancb}
ancb{s<143:aueb,aocb}
aocb{s<144:R,apcb}
apcb{s<145:aueb,aqcb}
aqcb{s<146:R,arcb}
arcb{s<147:aueb,ascb}
ascb{s<148:R,atcb}
atcb{s<149:aueb,aucb}
aucb{s<150:R,avcb}
avcb{s<151:aueb,awcb}
awcb{s<152:R,axcb}
axcb{s<153:aueb,aycb}
aycb{s<154:R,azcb}
azcb{s<155:aueb,aadb}
aadb{s<156:R,abdb}
abdb{s<157:aueb,acdb}
acdb{s<158:R,addb}
addb{s<159:aueb,aedb}
aedb{s<160:R,afdb}
afdb{s<161:aueb,agdb}
agdb{s<162:R,ahdb}
ahdb{s<163:aueb,aidb}
aidb{s<164:R,ajdb}
ajdb{s<165:aueb,akdb}
akdb{s<166:R,aldb}
aldb{s<167:aueb,amdb}
amdb{s<168:R,andb}
andb{s<169:aueb,aodb}
aodb{s<170:R,apdb}
apdb{s<171:aueb,aqdb}
aqdb{s<172:R,ardb}
ardb{s<173:aueb,asdb}
asdb{s<174:R,atdb}
atdb{s<175:aueb,audb}
audb{s<176:R,avdb}
avdb{s<177:aueb,awdb}
awdb{s<178:R,axdb}
axdb{s<179:aueb,aydb}
aydb{s<180:R,azdb}
azdb{s<181:aueb,aaeb}
aaeb{s<182:R,abeb}
abeb{s<183:aueb,aceb}
aceb{s<184:R,adeb}
adeb{s<185:aueb,aeeb}
aeeb{s<186:R,afeb}
afeb{s<187:aueb,ageb}
ageb{s<188:R,aheb}
aheb{s<189:aueb,aieb}
aieb{s<190:R,ajeb}
ajeb{s<191:aueb,akeb}
akeb{s<192:R,aleb}
aleb{s<193:aueb,ameb}
ameb{s<194:R,aneb}
aneb{s<195:aueb,aoeb}
aoeb{s<196:R,apeb}
apeb{s<197:aueb,aqeb}
aqeb{s<198:R,areb}
areb{s<199:aueb,aseb}
aseb{s<200:R,ateb}
ateb{s<201:aueb,aueb}
aueb{x>1:A,A}

{x=1,m=1,a=1,s=1}"""

def test_workflow_2():
    assert workflow_2(stress_test) == 167409079868000