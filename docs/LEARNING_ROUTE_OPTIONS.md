# 學習路線圖：六個候選版本

六版使用相同八堂課內容，只改變版面。A～C 是第一輪；D～F 是針對「不要太長或太寬、折線填滿單一畫面」新增的緊湊版本。

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

## 版本 D｜4 × 2 寬螢幕蛇形

四個節點一排、共兩排，適合桌面 README。順序沿第一排向右，再折到第二排向左；比例接近寬螢幕，但不會像原版八節點一字排開。

```mermaid
flowchart TB
    subgraph TOP[基礎到動態設計]
        direction LR
        D1[01｜AE 基礎] --> D2[02｜文字動畫] --> D3[03｜轉場效果] --> D4[04｜泡泡背景]
    end
    subgraph BOTTOM[特效到整合延伸]
        direction RL
        D5[05｜3D Logo] --> D6[06｜反射光澤] --> D7[07｜表達式] --> D8[08｜MG / Krita AI]
    end
    D4 --> D5
```

## 版本 E｜3–2–3 緊湊網格

上、下各三堂，中間兩堂作為銜接，長寬最接近一般內容區塊。折線只有兩次，仍可依箭頭讀出 Class01 → Class08。

```mermaid
flowchart TB
    subgraph EROW1[建立基本功]
        direction LR
        E1[01｜AE 基礎] --> E2[02｜文字動畫] --> E3[03｜轉場效果]
    end
    subgraph EROW2[視覺特效核心]
        direction RL
        E4[04｜泡泡背景] --> E5[05｜3D Logo / Saber]
    end
    subgraph EROW3[完成與延伸]
        direction LR
        E6[06｜反射光澤] --> E7[07｜表達式] --> E8[08｜MG / Krita AI]
    end
    E3 --> E4
    E5 --> E6
```

## 版本 F｜2 × 4 配對階梯

每列兩堂、四列交錯折返，整體接近方形；每一列也剛好形成一個合理的學習配對。

```mermaid
flowchart TB
    subgraph FROW1[操作基礎]
        direction LR
        F1[01｜AE 基礎] --> F2[02｜文字動畫]
    end
    subgraph FROW2[動態設計]
        direction RL
        F3[03｜轉場效果] --> F4[04｜泡泡背景]
    end
    subgraph FROW3[Logo 特效]
        direction LR
        F5[05｜3D Logo / Saber] --> F6[06｜反射光澤]
    end
    subgraph FROW4[整合延伸]
        direction RL
        F7[07｜表達式] --> F8[08｜MG / Krita AI]
    end
    F2 --> F3
    F4 --> F5
    F6 --> F7
```

## 選擇建議

- A：最大節點、純直式，但頁面最長。
- B：第一輪雙欄蛇形。
- C：強調四個能力階段，但連線較多。
- D：偏寬螢幕，適合桌面首頁。
- E：長寬最均衡，建議優先比較。
- F：接近方形，手機與桌面都容易閱讀。
