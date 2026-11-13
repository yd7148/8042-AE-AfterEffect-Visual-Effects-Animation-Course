# Class02｜文字動畫與簡單表達式

日期：2026-04-25｜[完整錄影](https://www.youtube.com/watch?v=29lG0NDNFMs)

## 學習目標與操作

先在 Paragraph／Align 設好文字基準，在文字圖層加入 `Animate > Position`，以 Range Selector 的 Offset 從 `-100%` 到 `100%` 做依序進場，再調 Ramp Up、Ease High／Low。需要更多變化時，逐項加入 Opacity、Tracking 或 Blur。表達式 `myFx = effect("CC Smear")("From"); myFx - [0,30]` 是「取得座標，再把 Y 軸上移 30 px」。

## 參考影片

- [文字 Motion Graphics Animation](https://youtu.be/TS-pK9jilJI) — 完整示範。
- [文字動畫播放清單](https://www.youtube.com/playlist?list=PLsEaLmxyXerAzfNd60oQwP2wb2ID7jFyV) — Offset、Tracking、Blur、Random。
- [Offset、Ramp Up 與 Ease](https://youtu.be/tEDg0XcQa1s) — 本堂核心操作。

## 常見錯誤與檔案

不要把圖層 Position 當成 Animator Position；效果或參數名稱必須和 expression 完全一致。[原始筆記](sources/original-notes.md)｜[來源對照](sources/source-map.json)｜[練習 AEP](aep/)
