# SIGNA ET STRUCTURA Site Design System v0.1

ページ作成日時：2026-08-29 09:02 JST  
最終更新日時：2026-08-29 09:02 JST

## 1. Editorial identity

**Financial Times × academic journal × modern data publication**

編集原則：**Signal → Structure → Evidence**

サイトはcrypto mediaの典型的なdark/neon/trading-terminal表現を避ける。新聞・学術誌の編集秩序と、現代data publicationの図表・provenanceを統合する。

## 2. Visual character

- warm paper background
- dark ink typography
- serif主体のmasthead / headline / body
- sans-serifはmetadata / navigation / source note / UIに限定
- thin rules + occasional heavy rule
- accentは注意・分類・eventに限定
- whitespaceを情報階層として使う
- card UIを乱用しない

## 3. Page hierarchy

### Home
1. masthead
2. navigation / language
3. editorial proposition
4. lead research
5. latest research grid
6. sections / methodology / about
7. disclosure notice
8. footer

### Article
1. content type
2. headline
3. standfirst
4. as-of / updated / risk metadata
5. body + research rail
6. figures integrated into argument
7. evidence
8. falsification / limitations
9. methodology
10. disclosure / provenance / corrections

## 4. Typography

MVPはsystem fontで開始し、外部font依存を避ける。

- editorial serif: Georgia / Times fallback
- UI sans: Arial / Helvetica fallback
- masthead: uppercase, trackingを広めに
- article headline: large serif, tight leading
- body measure: 約760px
- metadata: small sans, letter-spacing

将来fontを導入する場合もlicensed webfontのみとし、font assetを安易にrepoへ複製しない。

## 5. Color roles

色は固定hexではなくroleで扱う。

- paper
- paper-deep
- ink
- ink-soft
- rule
- accent
- positive
- negative

Data Figureのseries識別は色だけに依存しない。

## 6. Figure behavior

- article column内で大きく表示
- SVG primary
- PNG/WebP derivative
- title / caption / source / data as of / methodをfigure unitとして扱う
- observed / reconstructed / estimatedを視覚的に区別
- figureは装飾ではなくEvidence

## 7. Bilingual design

JA / ENで同じinformation architectureを維持する。

日本語でheadlineが長くなること、英語でline break位置が変わることを許容し、pixel-identical layoutは要求しない。

language switchは常時発見可能にする。

## 8. Responsive

Mobileを縮小desktopとして扱わない。

- 3-column cards → 1-column
- article body + rail → body後にrail
- headline sizeを段階的に縮小
- figureはviewport幅を最大活用
- metadataはwrap可能
- tap targetを確保

## 9. Trust surfaces

各記事で読者がすぐ確認できるもの：

- research as of
- updated
- content type
- evidence status
- disclosure
- provenance
- correction status

これらは本文末尾へ隠さない。

## 10. Anti-patterns

- BUY / SELL風CTA
- price tickerをHero化
- neon green/red
- candlestickを装飾背景として使用
- AI生成chartをEvidenceとして使用
- clickbait title
- sourceのない数値card
- mobileで読めないchart

## 11. Current implementation

Current scaffold: `feature/site-scaffold-v01`

Primary files:
- `site/index.html`
- `site/ja/index.html`
- `site/en/index.html`
- `site/ja/research/article-template/index.html`
- `site/en/research/article-template/index.html`
- `site/assets/tokens.css`
- `site/assets/site.css`

## 更新履歴

- 2026-08-29 09:02 JST：v0.1作成。editorial identity、page hierarchy、typography、responsive、trust surfaceを固定。
