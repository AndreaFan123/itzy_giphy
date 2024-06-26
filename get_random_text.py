# Create a dictionary 
import random

lyrics = {
    "text_1": "🐺: 실컷 고민해 봤자 (一直煩惱的話)，타이밍만 늦출 뿐이지 (只會錯過時間而)",
    "text_2": "🦥: 그 속에 뛰어들어 in your universe (在當中跳躍 in your universe)",
    "text_3": "🐱: 실컷 고민해 봤자 (一直煩惱的話)，타이밍만 늦출 뿐이지 (只會錯過時間而)",
    "text_4": "🦊: Yeah follow my lead, You ready?",
    "text_5": "🐰: 한 발 내디딘 순간 (邁出一步的瞬間)，펼쳐지는 clear night sky (展開的 clear night sky)",
    "text_6": "🐺🦥🐱🦊🐰: Oh lucky me 너를 만난 건 (Oh lucky me 遇見了你),Lucky you, lucky you 나를 만난 넌 (Lucky you, lucky you 遇見了我的你)",
    "text_7": "🦊: 난 하고 싶은 것만 해 (我只做我想做的事),그래 알아 넌 좀 달라 Anything (沒錯我知道你有點不一樣 Anything)",
    "text_8": "🐺: 더 솔직하게 더 솔직하게 더 솔직하게 더 (更誠實一點 更誠實一點 更誠實一點 更...)",
    "text_9": "🐰: 너 피하지마 너 피하지마 너 피하지마 너 (你不要逃避 你不要逃避 你不要逃避 你...)",
    "text_10": "🐰: 더 자유롭게 더 자유롭게 더 자유롭게 더 (更自由一點 更自由一點 更自由一點 更...)",
    "text_11": "🐱: Cool한 나니까 눈치 볼 마음 없어 Oh (因為是很 Cool 的我 所以並沒有要看眼色的意思)",
    "text_12": "🦥: 내 안에 있는 Dream 난 자신 있어 (在我裡面的 Dream 我有自信)",
    "text_13": "🐺🦥🐱🦊🐰: 너의 틀에 날 맞출 맘은 없어 (我並沒有想要迎合你的框架)",
    "text_14": "🐺: 참 말 많아 난 괜찮아 (話真是多 我沒有差), 계속 Blah blah (繼續 Blah blah)",
    "text_15": "🐺: 왜 숨어있어 뭐가 그리 심각해 (為什麼要躲起來 有那麼嚴重嗎?)",
    "text_16": "🐱: Boom Boom Pow blowing up, Bring my voltage up",
    "text_17": "🐺🦥🐱🦊🐰: 사랑 따위에 목매지 않아 (我才不會糾結在愛情這種東西), 세상엔 재밌는 게 더 많아 (世界上其他有趣的事更多)",
    "text_18": "🐺🦥🐱🦊🐰: 예쁘기만 하고 매력은 없는 (那些只有外貌卻沒魅力的), 애들과 난 달라 달라 달라 (我跟她們 不同 不同 不同)",
    "text_19": "🐺: 네 기준에 날 맞추려 하지 마 (不要以你的基準來約束我), 난 지금 내가 좋아 나는 나야 (我喜歡現在的我 我就是我)",
    "text_20": "🐺🦥🐱🦊🐰: 남 신경 쓰고 살긴 아까워 (只顧慮別人的感受活著太可惜)",
    "text_21": "🐱: 내 맘대로 살 거야 말리지 마 (我要隨我自己的心活著 不要攔著我)",
    "text_22": "🦊: 남들의 시선 중요치 않아 (別人的視線不重要)",
    "text_23": "🐺: 바꿀 생각 없어요 Nope (我沒有要改變的想法 Nope)",
    "text_24": "🦊: 나는 내가 알아 (我了解我自己)",
    "text_25": "🐱: 기죽지 마 절대로 (不要氣餒 好好的), 고개를 들고 네 꿈을 쫓아 (抬起頭追我的夢)",
    "text_26": "🐺🦥🐱🦊🐰: Keep your chin up, We got your back",
    "text_27": "🦊: 잔소리는 Stop it 알아서 할게 (嘮嘮叨叨 Stop it 我自己知道該怎麼做)",
    "text_28": "🦥: 어차피 내가 살아 내 인생 내거니까 (反正我就活著 因為我的人生是我自己的)",
    "text_29": "🐺🦥🐱🦊🐰: I’m just on my way 간섭은 No No 해 (I’m just on my way 干涉 No No 干涉)",
    "text_30": "🐺🦥🐱🦊🐰: 내 앞가림은 내가 해 (我自己會為自己想)",
    "text_31": "🐺🦥🐱🦊🐰: 사람들은 남 말 하기를 좋아해 (人們總喜歡說其他人的是非),남의 인생에 뭔 관심이 많아 왜 (為什麼那麼關心別人的人生)",
    "text_32": "🐺🦥🐱🦊🐰: 못 가지면 어때 괜히 (得不到的話又如何) 망설이다 시간만 가니 (一直猶豫的話是在浪費時間)",
    "text_33": "🐺🦥🐱🦊🐰: 후회하긴 싫으니까 (因為我不想後悔),엔딩 상관없으니까 (結局如何都沒關係)",
    "text_34": "🐺: Hell yeah, I’m untamable (沒錯 我難以駕馭)",
    "text_35": "🐺🦥🐱🦊🐰 : I got a crown on my head (我頭上戴著皇冠)",
    "text_36": "🐺: I know my way, got no limit, I go straight ay (我清楚我的方向 沒有極限 我直直向前 aye)",
    "text_37": "🦊: Love the feeling when I laugh and cry, the real me (我喜歡當我哭和笑時的感覺 真正的我)",
    "text_38": "🐱: 겁나면 내가 할게 그 악역 (如果你害怕 那我來扮演那個壞人吧)",
    "text_39": "🐰: 반짝일 테니 don’t worry (我會閃耀的不用擔心)",
    "text_40": "🐰: 아무나 다 알아보진 못해 like a real diamond (不是隨便一個人就能看得出來的 就像真正的鑽石一樣)",
    "text_41": "🐺🦥🐱🦊🐰: 널 믿지 못할 때면 (如果有不相信你的時候), 그저 날 믿어 봐 (那就相信我看看吧)",
    "text_42": "🐺🦥🐱🦊🐰: I know you’re gonna shine (我知道你會閃耀的), 약속해 I got your back (我保證我會支持你的)",
    "text_43": "🐺🦥🐱🦊🐰: I’m shining like a star, I go boom, go boom (我像星星一般閃耀 I go boom, go boom)",
    "text_44": "🐺🦥🐱🦊🐰: Every step I take is in victory lane, yeah (我走的每一步都是勝利之路 yeah)",
    "text_45": "🐰: 누가 뭐라 해도 I’ma say it louder (不管誰說什麼我都要說得更大聲)",
    "text_46": "🦊: 나를 막는 건 누구든 (阻擋我的不管是誰),내겐 아무런 의미 없을 뿐야 (對我來說只是毫無意義)",
    "text_47": "🐰: I’m untouchable 막아서지 못해 시작됐어 (我是不可觸碰的 無法阻擋 已經開始了), 지금 flow대로 just going on and on (就像現在的 flow一樣就會一直下去)",
    "text_48": "🐰: 끌린 대로 가 만족할 때까지 (隨心所欲的走 直到滿足),항상 내가 원한 길로 (總是走我自己想走的路)",
    "text_49": "🦊: 똑같은 건 뻔해 또 다른 걸 난 원해 chase (同樣的東西太無聊 我要追逐不一樣的東西)",
    "text_50": "🐺: 어떻게 모두를 다 맞춰줘 (怎麼可能讓大家都滿意),존중해 줘 I do me, you do you, you & I (尊重我吧 我做我自己 你做你自己 你和我)",
    "text_51": "🐺: 쉽지 않아 anyway (不簡單 沒關係), 생각대로 everyday (照我所想 每一天)",
    "text_52": "🐰: 고민 고민 대신에 (與其煩惱 煩惱), 나만 생각해 이제 (不如從此只為自己想)",
    "text_53": "🐱: 요즘 꽂힌 말이 하나 있지 (最近有句話讓我深深著迷),My best is yet to come",
    "text_54": "🦥: 필요 없는 기분 저기 다 던져 (把不需要的心情都扔到那吧), 지도에도 없는 곳이 목적지야(地圖上找不到的地方就是目的地)",
    "text_55": "🦥: 남다른 vibe (與眾不同的 vibe), 타고난 멋 I’m satisfied I’m satisfied (與生俱來的帥氣 I’m satisfied I’m satisfied)",
    "text_56": "🐺🦥🐱🦊🐰: I’m lucky lucky lucky, You’re so lucky lucky lucky",
    "text_57": "🐺🦥🐱🦊🐰: 내가 가진 운 가운데 제일 커다란 걸 쓴 게 아닐까 (是不是用掉了我所擁有的運氣當中最巨大的那個),이 세상에 당연한 건 우연이라도 없을 테니까 (因這世上沒有理所當然的偶然)",
}

def get_random_text():
    random_text = random.choice(list(lyrics.values()))
    return f"{random_text}\n\n\n翻譯來源：juinjuin (https://juinjuin.com/)"


get_random_text()