# 筆記翻新工坊: 用 Claude Code 把雜記變成互動網頁

每個人手邊多少都有幾份隨手記下的筆記, 可能是讀書心得, 生活觀察, 或是像這裡示範的理財雜記. 這些內容通常很有價值, 卻因為格式鬆散而少有人願意重讀. 這個專案想說明的是, 不需要設計背景, 也不需要從零學習網頁開發, 只要善用 AI 工具, 就能把手邊已經存在的生活紀錄, 重新變成一頁值得分享的互動網頁. 從自己熟悉的愛好或日常筆記開始練習, 是認識 AI 協作能力最實際的第一步.

一個最小示範, 說明如何用 Claude Code 的 frontend-design plugin, 把一份隨手寫的 Markdown 筆記, 重新設計成一頁式互動網頁.

## 專案簡介

`認識股票.md` 是一份用 Markdown 格式寫的個人理財筆記, 內容鬆散, 段落順序也未經整理, 是典型的雜記草稿. 透過 Claude Code 呼叫 frontend-design plugin, 先重新編排內容架構與精簡文案, 再提出數種視覺風格讓使用者挑選, 最後產出 `認識股票.frontend-design.html`, 一個可直接雙擊在瀏覽器開啟的互動式網頁.

為了對照差異, `認識股票.html` 是同一份筆記直接用 VS Code 的 Markdown Preview Extension 轉出的網頁, 沒有經過內容重新編排或視覺設計, 可以和 `認識股票.frontend-design.html` 並排比較, 感受兩者的落差.

這個資料夾保留了完整過程, 可以當成 Claude Code 實際操作的參考範例.

## 檔案結構

- `認識股票.md`: 原始筆記, Marp 投影片格式
- `認識股票.frontend-design.html`: 由筆記重新設計產出的互動式網頁
- `認識股票.html`: 用 VS Code Markdown Preview Extension 直接轉出的網頁, 作為對照組
- `assets`: 筆記與網頁共用的圖片素材
- `README.md`: 本文件, 含專案說明與一次完整的操作轉存紀錄

## Claude Code plugins

本示範使用的 plugin 是 frontend-design, 來自官方 marketplace `claude-plugins-official`.

### 安裝

`claude-plugins-official` 是 Claude Code 內建的官方 marketplace, 啟動 Claude Code 後即可直接使用, 不需要另外新增. 安裝 plugin 的指令如下.

```
/plugin install frontend-design@claude-plugins-official
```

### 用法

安裝完成後, 依照 plugin 內 skill 的命名慣例 `plugin名稱:skill名稱` 呼叫, 並附上要處理的檔案與需求說明.

```
/frontend-design:frontend-design @認識股票.md , 互動式 html. (請對敘述進行優化, 每個版面字數越少越好), 定稿前請列出 Theme 風格讓我選擇.
```

Claude Code 會先進入規劃模式, 讀取指定檔案內容, 再用 AskUserQuestion 提出視覺風格選項讓你挑選, 確認後才會實際寫出網頁檔案.

## /export 轉存紀錄

```
❯ /frontend-design @認識股票.md , 互動式 html. (請對敘述進行優化, 每個版面字數越少越好), 定稿前請列出 Theme 風格讓我選擇. 

❯ /frontend-design:frontend-design @認識股票.md , 互動式 html.                  
(請對敘述進行優化, 每個版面字數越少越好), 定稿前請列出 Theme 風格讓我選擇.      
  ⎿  Read 認識股票.md (191 lines)

  Searched for 1 pattern, read 3 files (ctrl+o to expand)

● User answered Claude's questions:
  ⎿  · 互動式頁面要用哪一種視覺風格? → 存摺帳本 Ledger (推薦)

● Updated plan
  ⎿  /plan to preview

● Write(認識股票.html)
  ⎿  Wrote 597 lines to 認識股票.html
       1 <!doctype html>
       3 <head>
       4 <meta charset="UTF-8">
       5 <meta name="viewport" content="width=device-width, initial-scale
       6 <title>認識股票 存摺</title>
       7 <link rel="preconnect" href="https://fonts.googleapis.com">
         gin>
       9 <link href="https://fonts.googleapis.com/css2?family=JetBrains+M
         ono:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&family
      10 <style>
     … +676 lines (ctrl+o to expand)
  Ran 1 shell command (ctrl+o to expand)

● 已依照存摺帳本 Theme 產出互動式頁面 D:\messy-notes\認識股票.html,
  並在預設瀏覽器開啟, 請直接檢視.

  主要設計:

  - 12 個存摺條目式段落(001 到 011), 文案已大幅精簡, 每段只留標題與少量重點,
  表格內容改為卡片, 條列或收據樣式
  - 左側(手機為頂部)有存摺明細線, 隨捲動進度即時累加金額到 100 萬,
  案例段落達成時觸發紅色印章動畫
  - K棒圖改用原生 SVG 重繪, 保留紅漲黑跌與影線標示; 中華電信截圖不直接嵌入,
  改成時間軸文字呈現
  - 交易忠告做成可勾選 checklist,
  底部彩蛋按鈕點開會以夾在存摺裡的紙條樣式顯示原本的 stockjoke.jpg
  - 支援手機版面收合, 尊重減少動態效果設定, 全站可用鍵盤操作

  如果版面或文案有想調整的地方, 請告訴我, 我可以直接修改.

✻ Cogitated for 5m 51s

※ recap: 你請我把 認識股票.md 整理後做成互動式存摺風格網頁, 我已產出 認識股票.html 並在瀏覽器打開讓你檢視, 接下來等你回饋文案或版面要不要調整。 (disable recaps in /config)
```