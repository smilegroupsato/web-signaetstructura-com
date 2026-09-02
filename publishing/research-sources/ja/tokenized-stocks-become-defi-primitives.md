# 株は「保有する資産」からDeFiの部品へ――Baseで始まったトークン化株式の利回り市場

## 要約

2026-08-24、Coinbase Tokenized StocksがBase上で稼働を始めた。重要なのは、NVIDIAやAppleなどの株式を表すトークンが24時間売買できるようになったことだけではない。

公開直後から、それらを担保、貸出、LP、金利差取引、複合運用Vaultへ組み込む商品が立ち上がっている。Base公式はAerodrome、Aave、Morpho、Euler、Beefy、Superformなどを対応先として列挙し、株式トークンを「保有する資産」ではなくDeFiで再利用できる金融部品として位置づけている。

2026-09-01に取得したPortals Explorerの表示では、NVDA SuperVaultはAPY 32.87%、TVL約$122.9K。TAUのGOOGLc / AAPLc / METAc / NVDAc運用Vaultは各10.00%で、TVLは約$7.1K〜$14.7K。Beefyの株式トークン–USDC LPには29.71%〜44.90%の表示APYが並ぶ。

ただし、これを「NVIDIAを持つだけで30%」と読むのは誤りである。

現在起きているのは株式の配当利回り上昇ではない。**株式を、DeFiで再利用できる資本の部品へ変える実験**である。

Figure: `scmr-20260901-005-fig01`

## 1. トークン化株式は、24時間売買できる株で終わらない

Base公式によれば、Coinbase Tokenized Stocksは実際の株式を1対1で裏付けとし、規制下の保管機関に倒産隔離された形で保管する。保有者はその株式に対する受益権を表すB20トークンを持つ。

対象は米国外の適格地域に限定されるが、発行後のB20トークンは自己管理型ウォレットへ移動でき、DeFiへ組み込める。Base公式の対応先一覧には、Aerodrome、Aave、Morpho、Euler、Beefy、Superformなどが含まれている。

ここで従来の証券口座との違いが生まれる。

証券口座のNVIDIA株は、基本的には「保有する・売る・証券会社を通じて貸す」資産である。

一方、オンチェーンのNVDAcは、

```text
NVDAc
→ 担保
→ ステーブルコインを借りる
→ 金利差を取る運用
→ 流動性供給
→ 複合運用Vault
```

と、別の金融契約へ連続的に組み込める。

トークン化の本番は発行そのものではなく、発行後にその資産が何へ使われるかで始まる。

## 2. 最初の実験：NVDA SuperVault

SuperformのNVDA SuperVaultは、その最初期の事例の一つである。

2026-09-01取得のPortals ExplorerではAPY 32.87%、TVL約$122.9K。数日前の観測でも30%台後半のAPYと約$100K規模のTVLが報告されており、開始直後から数値は大きく動いている。

Superformが説明する初期戦略は、トークン化されたNVDAを使ったUSDCの金利差運用である。NVDAcを担保として利用し、USDCを借り、借入コストを差し引いても収益が残る局面で資金を運用する。株価変動に応じてLTVを管理し、必要に応じて債務を減らす。

つまり表示APYは、NVIDIAの配当から生まれているわけではない。

少なくとも、

- 貸出と借入の金利差
- レバレッジ
- 開始直後の利用促進報酬
- USDC報酬
- UP / sUP報酬

を分けて見る必要がある。

現在の30%超という数字を、長期的に続く株式利回りとして外挿することはできない。

## 3. さらに小さい市場がすでに生まれている

2026-09-01のPortals Explorerでは、TAUのGOOGLc / AAPLc / METAc / NVDAc運用Vaultがいずれも10.00% APYを表示している。TVLはGOOGLc約$10.3K、AAPLc約$11.6K、METAc約$7.1K、NVDAc約$14.7Kで、まだ極めて小さい。

TAUはCoinbase Tokenized Stocksの開始日に、IPOR Fusion上でこれら4銘柄のCarry Vaultを公開したと説明している。

一方、BeefyはAerodromeの株式トークン–USDCプールを使う集中流動性管理Vaultを開始した。Beefy自身の説明によれば、開始期にはAerodromeの報酬、CoinbaseからMerkl経由で提供されるUSDC報酬、Beefy独自の報酬という三層の利用促進策が重ねられている。

Portals Explorerでは2026-09-01時点で、BeefyのUSDC-METAcが44.90%、USDC-AAPLcが41.51%、USDC-GOOGLcが29.79%、USDC-NVDAcが29.71%の表示APYだった。

Figure: `scmr-20260901-005-fig02`

これらはまだ「成熟した利回り市場」と呼べる規模ではない。むしろ重要なのは、株式トークンが公開されて数日のうちに、現物取引だけでなく貸出、担保、金利差運用、LP、Vaultまで金融市場の階層が作られ始めたことである。

## 4. 株を買わず、株を担保に借りる人へ貸す

もう一つ重要なのがUSDC側である。

SuperformのStocks USDC SuperVaultは、トークン化株式を担保とする市場へUSDCを供給し、借り手が支払う金利を受け取る設計を掲げている。Superformの公開説明では最大8%という案内がある一方、2026-09-01取得のPortals Explorerでは表示APYは3.76%、TVL約$1.47Kだった。

この差自体が、初期市場の表示利回りを固定値として扱えないことを示している。

これはNVIDIA株そのものを買う投資とは異なる。

```text
NVDAの値上がりを取る
```

のではなく、

```text
NVDA等を担保に資金を借りたい需要
→ USDCを貸す
→ 金利を受け取る
```

という投資になる。

今後トークン化株式市場が拡大した場合、株価そのものとは別に「株式担保の信用市場」が独立した市場になる可能性がある。

## 5. 高APYより重要な問い

初期市場では派手なAPYが最も目につく。

しかし本当に見るべきなのは数字の大きさではない。

- APYの何%が借り手の金利か
- 何%が取引手数料か
- 何%が期限付きの利用促進報酬か
- どれだけレバレッジがかかっているか
- どこまで価格が下がると清算されるか
- Vaultの運用者が何を変更できるか
- 退出までどれだけ時間がかかるか
- 報酬が終わったあと何%の利回りが残るか

である。

特にBeefyの開始期は、公式説明だけでも三層の報酬が存在する。表示APYの高さは、株式そのものの収益力ではなく、市場形成のために投入された補助金を相当程度含む可能性がある。

トークン化株式の利回り市場の面白さは「株なのに高利回り」ではない。

**株式がプログラム可能な担保になり、その上へ新しい金融商品を高速で積み上げられるようになったこと**にある。

2021–2022年のDeFiでは、成功したプロトコルのforkが大量に発生した。

2026年に見えているのは、成熟したプロトコル、トークン化された実物資産、価格情報、貸出市場、DEX、Vaultを部品として組み合わせ、新しい金融商品を作る動きである。

Coinbase Tokenized Stocksは、この「組み合わせによる増殖（Composition Boom）」へ新しい大きな原材料を供給し始めた可能性がある。

## Evidence / Sources

- Base, `Stocks just got updated`, 2026-09-01取得：Coinbase Tokenized StocksのB20構造、1:1の実株裏付け、規制下・倒産隔離保管、自己管理、DeFi利用を説明。
- Base, Stocks registry / ecosystem listing, 2026-09-01取得：NVDAc / METAc / AAPLc / GOOGLcと、Aerodrome、Aave、Morpho、Euler、Beefy、Superform等の対応先を掲載。
- Beefy, `Coinbase Tokenized Stocks: As Markets Converge`, 2026-08-24：Aerodrome CLM、Coinbase USDC incentives、Beefy boostsの三層報酬を説明。
- Portals Explorer, Base Stocks, 2026-09-01取得：NVDA SuperVault 32.87% / 約$122.9K、TAU各Vault 10.00%、Stocks USDC SuperVault 3.76%、Beefy株式LPの表示APYを取得。
- Superform / SuperStocks public materials：NVDA SuperVaultのUSDC金利差運用、Stocks USDC SuperVaultの株式担保貸出を説明。
- TAU Labs / IPOR Fusion public materials：GOOGLc / AAPLc / METAc / NVDAc Carry Vaultを開始日から展開。

## Figure

- `publication/sc-markets-research/figures/scmr-20260901-005/`
  - `scmr-20260901-005-fig01` — B20株式トークンがDEX・貸出・金利差運用・LP・Vaultへ接続される構造図。Analytical Diagram。
  - `scmr-20260901-005-fig02` — 2026-09-01時点の代表的な初期商品の表示APY比較。Data Figure。
- Figure Contract / Design System v0.1準拠。Figure 02のsource dataはCSVとして保存。

## 前提・限界・反証条件

- APY / TVLは2026-09-01前後の短期的な観測値であり、恒久的な利回りを示さない。
- Portals Explorerは集約サービスであり、各商品の最終的な投資条件はprotocol自身の画面・contractで再確認する必要がある。
- APYの算出方法と報奨金の含め方は商品ごとに異なるため、Figure 02は同質な収益率のランキングではない。
- Beefyの開始期APYにはAerodrome、Coinbase、Beefyの利用促進報酬が重なる。
- トークン化株式の利用可能地域は商品・取引場所ごとに異なる。Base公式は米国外の適格地域向けと説明する。
- 発行体・保管・法的リスクと、その上に構築されたDeFiプロトコルのリスクは別々に存在する。
- 報酬終了後にTVL・取引・貸出需要が大幅に縮小する場合、「新しい持続的市場形成」という仮説は弱まる。
- 逆に、報酬縮小後も担保利用・借入・LP・Vault利用が残り、新商品が継続的に増えるなら、株式がDeFiの基礎部品になりつつあるという説明は強まる。


## Disclosure

本稿は市場構造の研究を目的とするものであり、Coinbase Tokenized Stocks、NVDAc、AAPLc、METAc、GOOGLc、Superform、TAU、Beefyその他の関連商品・プロトコルへの投資を推奨するものではありません。執筆・発行主体に本稿の対象に関する開示すべき利益相反はありません。
