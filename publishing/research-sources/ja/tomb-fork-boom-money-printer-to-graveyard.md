# 数字で読むTomb Fork Boom
## 「Money Printer」が墓場になるまで


## 1. 墓場から始める

暗号資産の歴史には、仕組みそのものより、その仕組みを誰もが真似し始めた瞬間の方が面白いことがある。

2021年末から2022年にかけて、Fantomを中心とするDeFi市場には、Tomb Financeの構造を模倣したプロトコルが次々に現れた。SCARAB、2OMB、3OMB、BASED。名前も、ペグ対象も、報酬設計も少しずつ違う。しかし参加者が見ていた景色には、共通したものがあった。

Cash tokenを流動性プールへ入れる。Share tokenを得る。Share tokenをステークする。プロトコルが拡張局面に入れば新しいCash tokenが発行される。それをまた流動性へ戻す。

Tomb Financeの公式資料は、この循環を飾らなかった。「money printer」という言葉さえ使った。

もちろん、本当に無から富が生まれていたわけではない。新規資金、トークン価格、流動性、発行量、参加者の期待が互いを押し上げているあいだ、その循環が「印刷機」に見えたのである。

そして印刷機が一台うまく動けば、次に起きることは予想しやすい。誰かが二台目を作る。

さらに三台目、四台目が現れる。

やがて市場は、Tomb Financeそのものへ投資する場所から、「次のTomb Finance」を探す場所へ変わった。

本稿では、その短い熱狂を墓場から掘り返す。

目的は、かつての高APRを笑うことではない。Tomb Forkがどのように生まれ、どのくらいの資金を集め、どのような価格をつけ、何度ペグを割り、それでも何度戻り、最後に何が変わったのかを、可能な限り数字で再構築することである。

調査では、当時の公式文書やcommunityの記録だけでなく、Fantom上のpair contractを特定し、過去ブロックとSync / Mint / Burn / Swap eventを再走査した。2OMB/WFTMだけでもSync eventは約60万件に達する。複数のTomb Forkを合わせれば、単にチャートサイトの最高値を見るのとはまったく違う景色が現れる。

最初に見えてきたのは、意外な事実だった。

**ペグを割ること自体は、珍しくなかった。**

4つの主要プロトコルからblock末基準で抽出した177回のdepeg episodeのうち、122回、68.9%は1時間以内にペグへ戻った。3時間以内なら77.4%、6時間以内なら84.2%、24時間以内なら92.7%が戻っている。

研究期間中、一度も戻らないまま終わったepisodeは、わずか3件だった。

Tomb Forkの墓を理解する鍵は、「いつペグを割ったか」ではなかった。

**割れたあと、なぜあるものは戻り、あるものだけが戻れなくなったのか。**

そこから話を始めたい。

## 2. 祖先――BasisからTomb Financeへ

Tomb Financeの系譜を説明するとき、「Basis Cashのforkだった」と一行で済ませるのは正確ではない。

その祖先には、暗号資産で中央銀行のような供給調整を再現しようとしたBasisの構想がある。Basis Cashはその思想をDeFi上へ持ち込んだ代表例の一つだった。しかしTomb Finance自身の説明を追うと、Basisの原案だけでなく、bDollarやsoupなど複数の先行実装から着想を得た三トークン型プロトコルとして位置づけられている。

基本構造は、Cash、Share、Bondである。

Cash tokenは一定の対象資産へのペグを目指す。Share tokenは拡張局面の発行益を受け取る権利に近い。Bond tokenはペグを下回った局面で供給を吸収し、将来の回復に賭ける仕組みとして設計される。

理屈だけを読めば、これは金融工学の小さな実験に見える。

しかしDeFi市場へ置かれた瞬間、その意味は変わった。

Share tokenは「将来の通貨発行益への請求権」であると同時に、極端な高APRを伴う投機対象になった。Cash tokenの需要が増え、ペグを上回り、発行が続く限り、Share tokenの保有者には新しいCash tokenが配られる。

その循環が続くという期待そのものがShare token価格を押し上げ、Share token価格の上昇がさらに参加者を呼び込む。

Tomb Financeは、この構造をFTMへ接続した。

TOMBはFTMへのペグを目指し、TOMB-FTMの流動性、TSHARE、Masonryを中心に経済圏を作った。ここにFantomそのものの成長物語が重なったことが重要だった。

単なるアルゴリズム型ステーブルコインではない。「Fantomの成長へ乗るためのDeFi装置」という物語を持つことになったからである。

## 3. 一度死にかけたTomb Finance

Tomb Financeの歴史が後のfork文化に与えた影響を考えるうえで、一度の失敗は重要である。

Tomb Financeは初めから順調だったわけではない。2021年には深刻な危機を経験し、プロジェクトはnear-collapseへ追い込まれた。その後Harry Yehによるtakeoverを経て復活する。

公式回顧に基づく数字では、その後およそ4か月でTVLは約250万ドルからpeak約16億ドルへ膨張した。

単純倍率で約640倍である。

この成功は、後発forkに二つの物語を与えた。

一つは、「この仕組みは巨大化できる」という成功物語。

もう一つは、「一度ペグが危なくなっても復活できる」という回復物語である。

後から見ると、この二つ目が特に重要だった可能性がある。ペグ割れが即死を意味しないことは、実際に今回のオンチェーン再構築でも確認された。問題は、どこまでを「いつもの一時的なdepeg」と見なし、どこからを回復不能と見るかだった。

当時の参加者には、その境界線は見えていなかった。

そしてTomb Financeが巨大化すると、市場の関心は本家だけでは収まらなくなった。

## 4. 「Tombに乗り遅れた」

2021年12月のcommunity記録を読むと、後発forkの供給より先に、需要が生まれていたことが分かる。

「Tomb Financeにはもう乗り遅れた。次のTomb Forkで短期のdegen playをしたい。」

そうした発想が、2omb Financeの登場前から確認できる。

これはTomb Fork Boomを理解するうえで重要である。

コピーを作った開発者だけを見ていると、なぜ短期間にあれほど多くのforkが成立したのかを説明できない。市場の側に「次のTomb」を求める需要があった。

2021年12月にはScarab Finance、2022年1月には2omb Financeと3omb Finance、2月にはBased Financeが続く。

新しいforkが登場するたび、参加者は本家Tomb Financeとの技術差だけを比較していたわけではない。

むしろ重要だったのは、「まだ早いか」である。

Tomb Financeで得られたはずの初期利益を逃した参加者にとって、新しいforkはsecond chanceだった。

この時点で、Tomb Financeの仕組みは金融プロトコルであると同時に、複製可能な投機フォーマットになっていた。

## 5. 22日で8.7倍――2omb Finance

2omb Financeは、その「second chance」が市場として成立したことを最も分かりやすく示す例である。

同時代資料で追うと、2omb FinanceのTVLは2022-01-17頃の約920万ドルから、2022-02-08頃には約8,000万ドルへ膨らんだ。約22日で8.7倍である。

同じ時期、Tomb FinanceのTVLは約8.3億ドルから約4.96億ドルへ縮小していた。

この二つの数字だけを並べると、「Tomb Financeから2omb Financeへ資金が移った」と書きたくなる。しかし、それはまだ証明されていない。Fantom全体にも大量の資金が流入していたからである。2022年1月、Fantom全体のTVLは短期間に大きく増えていた。

したがって本稿では、時間的な並行をcapital migrationそのものとは扱わない。Figure 17は、この2時点のreported TVLを「同時進行」のEvidenceとしてのみ示す。

それでも、2omb Financeが極端な速度で巨大化した事実は残る。

さらにオンチェーンへ降りると、「TVL約8,000万ドル」という数字そのものにも別の問題が見つかった。

2022-02-08 11:00 JST付近を当時のcontract構成から再構築すると、2omb FinanceではPool2に約8,254万ドル、2SHARE stakingに約1億6,055万ドル相当がロックされていた。参加者側のロック価値を合算すると、約2億4,309万ドルになる。

8,000万ドルと2億4,000万ドル。

三倍近く違う。

どちらかが単純に間違っているわけではなかった。

問題は、「TVL」という言葉が何を数えていたのかである。

## 6. TVLという数字は存在しない

DeFiを数字で振り返るとき、TVLは最も便利で、最も危険な指標の一つである。

チャートには一本の線として表示される。そのため、まるでブロックチェーン上のどこかに「このプロトコルのTVL」という値が保存されているように見える。

実際にはそうではない。

少なくとも今回調べたTomb Fork群では、何をTVLとして数えるかは集計側のadapter codeによって決まっていた。

2omb Financeのlaunch-era DefiLlama adapterをGit履歴まで遡ると、Pool2とstakingは別のカテゴリーとして扱われていた。その後、3omb FinanceのGenesis Poolが同じadapterへ統合される変更まで入っている。

つまり、同じ「2omb TVL」というラベルでも、時点によって測定対象そのものが変わり得る。

Scarab Financeでは別のcontract集合が使われ、Based FinanceではPool2、BSHARE staking、Treasuryが分離されていた。3omb Financeの初期adapterはGenesis Pool中心だった。

この違いを無視してプロトコル同士のTVLを比較すると、コード上の分類差を経済規模の差と取り違える。

そこで本調査では、比較用に「参加者ロック価値」という分析軸を別に置いた。Pool2、staking、参加者depositを対象とし、Treasuryは除外する。同時代headline TVLとは別系列として保存する。

この定義で過去ブロックから再構築したピークは、2omb Finance約2億4,309万ドル、Based Finance約9,260万ドル、Scarab Finance約1,845万ドル、3omb Finance約1,539万ドルだった。

ここで大事なのは、これを「真のTVL」と呼ばないことである。

これは比較のために定義を揃えた再構築値である。

**TVLは自然観測値ではない。測定方法を伴う数字である。**

この当たり前のことが、過去のDeFiブームを数字で読むときには意外なほど重要になる。

## 7. 「最高値」は本当に最高値か

価格にも似た罠がある。

AMMでは、流動性が極端に薄ければ、ごく少額の取引でも異常な価格がつく。チャートサービスがその瞬間を拾えば、それは「史上最高値」として残る。

今回、3OMB/WFTMの全Sync eventを走査すると、raw peakは約2,437 FTMだった。

数字だけを見れば、3OMBが一時2,000 FTMを超えたことになる。

しかし、その時のpairのquote側流動性は約99 FTMしかなかった。

そこで、事前に定めた流動性条件を満たすeventだけで価格ピークを比較すると、3OMBのpeakは約44.44 FTMになる。

SCARABも同じである。raw peakは約27.54 FTMだったが、十分な流動性がある局面に限定すると約2.77 FTMだった。

raw ATHを削除する必要はない。それも実際にchain上で観測された価格だからである。

ただし、raw ATHと「意味のある規模の資金が存在した市場でのpeak」を同じ列に置いてはいけない。

今回のFigure 05では、その二つを分離した。

この区別を入れると、Tomb Fork Boomは「あり得ない価格が次々についた狂乱」から、もう少し具体的な市場へ変わる。

どの程度の流動性の中で、どの程度のプレミアムが実際に維持されたのか。

その問いの方が、投機市場の構造を理解するには有用である。

## 8. ペグを割ったら死ぬのか

Tomb Forkの履歴を調べ始めたとき、最も自然な区切りは「いつペグを割ったか」だった。

ところが、全Sync eventを追うと、この区切りはほとんど役に立たないことが分かった。

2OMBはローンチ当日から1 FTMを割っている。しかも一度ではない。短時間で下抜け、戻り、また下抜ける。その後、2omb Financeはむしろ巨大化した。

そこで本調査では、2omb Finance、3omb Finance、Scarab Finance、Based Financeについて、同一block内の複数Syncをblock末の最終状態へ畳み込み、`price >= 1`から`price < 1`へ移った時点をdepeg episodeの開始、その後初めて`price >= 1`へ戻ったblock末をre-pegと定義した。event-levelの細かな往復をそのまま数えるのではなく、市場がblock末でどの状態にいたかを見るためである。

抽出されたdepeg episodeは177件だった。

- 2omb Finance：9件
- 3omb Finance：39件
- Scarab Finance：116件
- Based Finance：13件

そのうち、1時間以内にre-pegしたのは122件、68.9%。3時間以内では137件、77.4%。6時間以内では149件、84.2%。24時間以内では164件、92.7%だった。

研究期間内に一度もre-pegしなかったepisodeは3件しかない。2omb Finance、3omb Finance、Scarab Financeに1件ずつで、Based Financeにはなかった。

**Tomb Forkでは、ペグを割ること自体は珍しくない。戻れないことの方が珍しい。**

したがって「first depeg」を崩壊日として扱うと、歴史を大きく誤読する。2omb Financeではローンチ当日のdepegと、2022年2月23日のterminal depegはまったく違う事象である。

Figure 15の再ペグ曲線は、この違いを可視化する。重要なのは、depegの有無ではなく、depeg後にどれだけ長く未回復が続くかである。

## 9. 同じペグ割れでも、死に方は違う

では、最後に戻れなくなったとき、各プロトコルは同じように壊れたのだろうか。

答えは、違う。

terminal depeg前後のLP流動性を同じ方法で再構築すると、+24時間の変化は次のようになった。

- 2omb Finance：-68.17%
- 3omb Finance：-42.26%
- Scarab Finance：-2.78%
- Based Finance：+12.04%

Based Financeはterminal例ではなく、同じ時期にストレスを経験しながら回復した対照例である。

2omb Financeでは、ペグを割った後に流動性が急速に消えた。3omb Financeも明確な縮小だが、2omb Financeより緩やかだった。Scarab Financeはterminal episodeであっても、最初の24時間ではLP流動性が大きく消えていない。

つまり「ペグを割ったあとLPが一気に抜ける」という死に方すら、Tomb Fork共通ではない。

+72時間まで延ばしても、2omb Financeは-46.58%、3omb Financeは-65.19%、Scarab Financeは-9.90%。Based Financeは逆に+33.57%だった。

ここで見えてくるのは、単純な一本の崩壊曲線ではなく、複数のterminal pathである。

2omb Financeは急性の流動性崩壊。3omb Financeは時間をかけて深く縮む。Scarab Financeは流動性をある程度残したままre-peg能力を失う。Based Financeはストレスを吸収し、流動性を増やして戻る。

同じ「1を割った」という価格状態から、その後の市場構造はまったく違っていた。Figure 18は2OMB/WFTMの準備金推移を、Figure 20は2OMB / 3OMB / SCARABのbuild-upと準備金半減までの時間を示す。Figure 20の「collapseが速い」という結果は2OMB / 3OMBに限定し、SCARABへ一般化しない。

## 10. LP退出とトークン売りを分解する

流動性が減った理由をさらに分解すると、崩壊は一種類の売りではないことが分かる。

AMM pairのMint / Burn / Swap eventを分けると、quote準備金の減少を「LPそのものの退出」と「Cash token売りによるquote流出」へ近似的に分解できる。

2omb Financeのterminal depeg後24時間では、WFTM側準備金は約768万WFTM減少した。内訳は、BurnからMintを差し引いたLP純退出が約418万WFTM、2OMB売りSwap超過が約352万WFTMだった。

ほぼ半分ずつである。

つまり、2omb Financeの崩壊は「2OMBが売られた」だけではない。LP保有者自身も資本を引き抜き、その退出とトークン売りが同時に進んだ。

3omb Financeでも同様に、LP純退出約136万WFTMと3OMB純売り約124万WFTMが併存した。

一方、Based Financeでは逆方向だった。対照窓ではLPは純追加、BASEDも純買い越しである。価格ストレスがあっても、資本提供者と買い手が退出せず、むしろ吸収側へ回っていた。

この分解から、少なくとも一つの仮説が生まれる。

**崩壊とは、Cash tokenの売り圧だけでなく、LP資本の退出と売りが重なり、それが時間とともに増幅する状態ではないか。**

次の問題は、それを崩壊前に見分けられたかである。

## 11. 崩壊を予測できたのか――反証された単純仮説

最初に有望に見えたのはShare tokenだった。

2SHAREは2OMBのterminal depegよりかなり前にピークをつけ、イベント前にも下落していた。3SHAREにも似た形がある。Share tokenは将来の発行益への期待を価格化しやすいため、Cash tokenより先に期待が剥落するのではないか。

しかし横断比較すると、この仮説はそのままでは成立しなかった。Figure 19は2omb Finance単独では2SHARE弱含みと2OMB stressの時間順序が見えることを示すが、それ自体を横断signalとは扱わない。

BSHAREはBased Financeが回復した対照例であるにもかかわらず、イベント前24時間で約32.1%下落していた。GSCARABのピークはScarab Financeのterminalより約80日前で、時間差が大きすぎた。

177 episode Replayでも同じ結論になった。6時間時点まで未回復だった28件では、Share tokenは25件で下落していた。terminal 3件はすべて含むが、偽陽性は22件。Share token下落をそのままterminal signalとするとprecisionは12%しかない。

terminal 3件のShare token変化中央値は約-26.61%、non-terminalでは約-5.42%だった。差はある。しかしterminalが3件しかない以上、この結果を見てから都合のよい閾値を作ることはしない。

LP退出だけでもだめだった。Cash token売りだけでもだめだった。1時間時点のcombined stressの絶対値でも分離できない。

3omb Financeでは、11.14時間後に回復したepisodeの1時間combined stressが6.09%だったのに対し、terminal episodeは2.34%だった。強いストレスが必ず死を意味するわけではない。

そこで成熟市場pilotで、絶対値ではなくtrajectoryを見る仮説を固定した。

- 6時間時点で未回復
- combined stressが1h → 3h → 6hで連続増幅
- 6hでもLP純退出が正
- 6hでもCash token純売りが正

この条件を、結果を見てから変更せず、177 episodeの拡張母集団へ適用した。

6時間risk setは28件。そのうち候補陽性は8件だった。terminal判定では真陽性2、偽陽性6、真陰性19、偽陰性1。precision 25.0%、recall 66.7%、specificity 76.0%。

**死亡予測器としては不十分だった。**

しかも反証の形が重要である。2omb Financeと3omb Financeのterminalは捕捉できた。しかし偽陽性6件はすべてScarab Financeで、Scarab Financeのterminal 1件は逆に偽陰性だった。

2omb Financeと3omb Financeで見えた「ストレスが時間とともに増幅する死に方」は、Scarab Financeにはそのまま当てはまらない。

Tomb Forkは同じ設計思想を共有していても、同じ市場ではなかった。

ただし、この候補が完全に無意味だったわけでもない。terminalではなく「24時間以内にre-pegできない」を目的変数にすると、真陽性6、偽陽性2、真陰性13、偽陰性7。precisionは75.0%、specificityは86.7%だった。

つまり、6時間のstress trajectoryは「死ぬか」を当てるより、**ストレスが長引きやすい状態を高いprecisionで拾う補助signal**として読む方が妥当である。

ここで研究上の結論は、予測器を見つけたことではない。

単純な予測器を、かなり明確に壊せたことである。

## 12. 回復能力をどう測るか

では、死亡を一発で当てられないなら、何を見るべきか。

177 episodesの分布が示す最も強い事実は、depegの大半が戻ることである。1時間以内に68.9%、6時間以内に84.2%、24時間以内に92.7%がre-pegした。

重要なのは「危険か安全か」を一回で分類することではなく、状態がどう遷移しているかを見ることだろう。

本調査では、少なくとも次の状態モデルが有用だと考える。

`NORMAL → STRESS → 未回復継続 → protocol-specific deterioration / recovery`

当初は`REVERSAL_ATTEMPT`を、LP追加とCash token買い戻しが始まる明確な回復兆候として想定していた。しかしReplayはここにも反証を与えた。

研究期間内にre-pegした174件を、crossingから実際のre-peg blockまで追うと、回復時間は大きく分かれた。

- 1時間以内：122件、中央値約0.095時間、約5.7分
- 1〜3時間：15件、中央値約1.70時間
- 3〜6時間：12件、中央値約3.99時間
- 6〜24時間：15件、中央値約8.28時間
- 24時間超：10件、中央値約48.24時間

24時間を超えてから戻るepisodeも10件ある。したがって「24時間戻らなければ死亡」も成立しない。

さらに、LP追加とCash token買いを正方向とした累積absorptionを見ると、24時間超回復群の中央値は約-9.31%だった。re-peg時点まで累積フローがなおストレス方向に残っているepisodeが少なくない。

6時間deterioration候補の偽陽性6件はすべてScarab Financeで、回復時間中央値は約31.96時間だった。6時間以後からre-pegまで純absorptionが正だったのは2件だけで、中央値も約-1.90%だった。

つまり、**回復する前には必ずLP流入と買い戻しが明瞭に反転する**という規則も支持されなかった。

AMM価格は、その瞬間の準備金比で決まる。累積フローだけでなく、流動性規模、価格弾力性、bondやtreasuryの設計、外部からの介入、参加者構成などが回復過程に影響する。

Scarab Financeが2omb Financeや3omb Financeと異なる偽陽性・偽陰性を出したことは、そのprotocol固有性を強く示唆する。

したがって、Recovery Signalを作るなら、Tomb Fork横断の単一閾値ではなく、共通観測層とprotocol固有モデルを分離する必要がある。

共通観測層では、未回復時間、LP純退出、Cash token純売り、stress trajectory、Share token、流動性規模を測る。

その上で、protocolごとに、ペグ維持機構、Treasury、Bond、外部介入、主要LP構成などを別の状態変数として持つ。

177 Replayが教えたのは、「正しい閾値は6時間か24時間か」という話ではなかった。

**同じdepegでも、回復する仕組みと壊れる仕組みがprotocolごとに違う。**

## 13. Tomb Forkの墓が教えるもの

Tomb Fork Boomを一本の物語に縮めるなら、こうなる。

成功したプロトコルが物語を作る。

その物語が模倣される。

模倣先へ「次こそ早く入る」資金が流れる。

高APRとShare tokenの上昇が、Cash token需要と流動性を増やす。

流動性と価格上昇が、さらにAPRと期待を強く見せる。

この反射的な循環が続くあいだ、参加者にはmoney printerが動いているように見える。

しかし、循環が止まり始めると、同じ設計が逆回転する。Share token期待が弱まり、Cash tokenが売られ、LPが退出する。売りと退出が準備金を減らし、価格の弾力性を悪化させ、さらに不安を強める。

ただし、本調査が重要だと考えるのは、この最後の段階さえ一様ではなかったことである。

2omb Finance、3omb Finance、Scarab Financeは、すべてterminal depegを経験した。しかし流動性の抜け方も、stress trajectoryも、Share tokenの動きも違った。Based Financeは強いShare token下落を経験しながら回復した。

だから「Tomb Forkはこう死ぬ」という単一テンプレートは作れない。

むしろ、この市場が示したのは、**似た仕組み・似たナラティブ・似た投機家を持つ市場でも、最終的なfailure modeは同じとは限らない**ということだった。

これは2022年のFantomだけの話ではない。

Meme coin、新規L1/L2、restaking、yield-bearing token、SNS主導の小型株や暗号資産。成功例が出たあと、似たフォーマットが大量に供給され、「本家に乗り遅れた人」が次のsecond chanceへ向かう市場は繰り返し現れる。

そのとき見るべきなのは、名前やAPRだけではない。

何を測ったTVLなのか。

最高値にどれだけの流動性があったのか。

ストレス時に誰が売り、誰がLPを抜き、誰が残ったのか。

そして、同じように見えるプロトコルのどこが違うのか。

Tomb Forkの墓場は、失敗プロジェクトの一覧ではない。

模倣と資本流入と反射性が、どのように市場を急速に膨らませ、そして異なる経路で壊していくかを保存した標本群である。

「Money Printer」は、本当に紙幣を印刷していたわけではなかった。

それは、期待と流動性が互いを増幅しているあいだだけ動く装置だった。

そのことは、印刷機が止まったあとに最もよく見える。

## Evidence / Method

本稿の歴史記述は、同時代の公式資料・community記録・公開TVL資料と、Fantom上のオンチェーン再構築を区別して扱う。Figure 17は2022-02-11公開の近時二次資料に明示されたhistorical snapshotを`reported`として使用し、現在のDefiLlama APIで連続系列を補間しない。Figures 18–20はFantomのhistorical state / eventから再構築する。オンチェーン部分では、主要AMM pairのSync / Mint / Burn / Swap event、historical `getReserves`、block timestampを使用し、同一block内の複数Syncは最終状態へ畳み込んだ。

177 depeg episodesについては、各判定時点まで未回復のepisodeのみをrisk setへ残し、未来のre-peg結果は評価ラベルにだけ用いた。近接episodeへ固定長の事後窓を重複付与する疑似反復を避けている。

主要な再構築data、builder、candidate audit、Replay summaryは`publication/sc-markets-research/figures/scmr-20260829-001/`および`records/research/tomb-fork-cemetery/2026.09.01_45_depeg_episode_replay_complete_result_v0.1.md`に保存している。

## Limitations / Falsification

本調査のterminalは「研究期間内に再ペグしなかった」を意味し、永久的なprotocol deathを意味しない。177 episodesはprotocol内でclusterしており、独立同分布の177標本ではない。terminalは3件しかなく、統計的に安定した死亡予測器を学習できる標本数ではない。

TVLやparticipant-locked valueは測定定義に依存する。Tomb Finance縮小とfork成長の同時進行は確認できるが、wallet-levelの直接資本移動は本稿では証明していない。

Share token、stress、LP退出、Cash token売りについて、結果を見てから閾値を最適化していない。成立しなかった仮説も本文へ残した。


## Disclosure

本稿は過去のDeFi市場を対象とするHistorical Case Studyであり、現在の暗号資産の購入・売却を推奨するものではありません。執筆・発行主体に本稿の対象に関する開示すべき利益相反はありません。
