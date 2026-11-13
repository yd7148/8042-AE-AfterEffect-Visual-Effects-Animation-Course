# 學習路線圖：三個候選版本

這三版使用相同八堂課內容，只改變版面。請比較 GitHub 實際渲染後，選擇要放回首頁的版本。

## 版本 A｜直式單一路線

優點：節點最大、手機閱讀清楚、先後順序最直觀。缺點：頁面較高。

```mermaid
flowchart TB
    C1[Class01｜AE 基礎] --> C2[Class02｜文字動畫]
    C2 --> C3[Class03｜轉場效果]
    C3 --> C4[Class04｜泡泡動態背景]
    C4 --> C5[Class05｜3D Logo / Saber]
    C5 --> C6[Class06｜Logo 反射光澤]
    C6 --> C7[Class07｜商品展示 / 表達式]
    C7 --> C8[Class08｜MG 動畫 / Krita AI]
```

## 版本 B｜雙欄蛇形

優點：比原圖高、又不會像直式版那麼長，桌面與手機較均衡。缺點：閱讀方向需要跟著箭頭轉彎。

```mermaid
flowchart TB
    subgraph R1[基礎操作]
        direction LR
        C1[Class01<br/>AE 基礎] --> C2[Class02<br/>文字動畫]
    end
    subgraph R2[動態設計]
        direction RL
        C4[Class04<br/>泡泡動態背景] --> C3[Class03<br/>轉場效果]
    end
    subgraph R3[進階效果]
        direction LR
        C5[Class05<br/>3D Logo / Saber] --> C6[Class06<br/>Logo 反射光澤]
    end
    subgraph R4[整合延伸]
        direction RL
        C8[Class08<br/>MG 動畫 / Krita AI] --> C7[Class07<br/>商品展示 / 表達式]
    end
    C2 --> C3
    C4 --> C5
    C6 --> C7
```

## 版本 C｜四階段學習地圖

優點：課程概念分組最清楚，適合當課程導覽。缺點：不像 A 版那樣強調每一堂的線性順序。

```mermaid
flowchart TB
    F1[階段 1｜操作基礎]
    F2[階段 2｜轉場與背景]
    F3[階段 3｜Logo 特效]
    F4[階段 4｜表達式與延伸]

    F1 --> C1[Class01｜AE 基礎]
    F1 --> C2[Class02｜文字動畫]
    C1 --> F2
    C2 --> F2
    F2 --> C3[Class03｜轉場效果]
    F2 --> C4[Class04｜泡泡動態背景]
    C3 --> F3
    C4 --> F3
    F3 --> C5[Class05｜3D Logo / Saber]
    F3 --> C6[Class06｜Logo 反射光澤]
    C5 --> F4
    C6 --> F4
    F4 --> C7[Class07｜商品展示 / 表達式]
    F4 --> C8[Class08｜MG 動畫 / Krita AI]
```

## 建議

- 想要節點最大、順序最清楚：選 A。
- 想兼顧高度與寬度：選 B。
- 想呈現課程架構與能力階段：選 C。
