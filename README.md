# 🐍 貪吃蛇遊戲

一個使用 HTML5 Canvas 和 JavaScript 開發的經典貪吃蛇遊戲。

## 📋 功能特性

- **經典遊戲玩法**：控制蛇吃掉食物，避免碰撞
- **難度選擇**：提供簡單、中等、困難三個難度級別
- **分數系統**：實時顯示當前分數和最高分
- **暫停功能**：支持遊戲暫停和繼續
- **鍵盤控制**：支持方向鍵和按鈕控制
- **響應式設計**：適配各種屏幕尺寸
- **本地存儲**：自動保存最高分記錄

## 🎮 遊戲規則

1. 使用方向鍵或屏幕按鈕控制蛇的移動方向
2. 吃掉紅色的食物來增加分數和蛇的長度
3. 避免碰到牆壁或蛇自己的身體，否則遊戲結束
4. 選擇不同的難度來改變遊戲速度
5. 挑戰最高分吧！

## 🚀 快速開始

### 方式一：直接打開文件
1. 下載或克隆本倉庫
2. 在瀏覽器中打開 `index.html` 文件
3. 點擊「開始遊戲」按鈕開始遊戲

### 方式二：使用本地服務器
```bash
# 使用 Python 3
python3 -m http.server 8000

# 或使用 Python 2
python -m SimpleHTTPServer 8000

# 或使用 Node.js (需要安裝 http-server)
npm install -g http-server
http-server
```

然後在瀏覽器中訪問 `http://localhost:8000`

## 🎯 控制方式

### 鍵盤控制
- **↑** 向上移動
- **↓** 向下移動
- **←** 向左移動
- **→** 向右移動
- **空格鍵** 暫停/繼續

### 按鈕控制
- 使用屏幕上的方向按鈕控制蛇的移動
- 點擊「開始遊戲」開始遊戲
- 點擊「暫停」暫停遊戲

## 🎨 技術棧

- **HTML5**：頁面結構和 Canvas 元素
- **CSS3**：現代化的樣式設計和響應式布局
- **JavaScript (ES6+)**：遊戲邏輯和交互功能

## 📱 瀏覽器兼容性

支持所有現代瀏覽器：
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Opera 76+

## 🎮 難度說明

| 難度 | 速度 | 適合人群 |
|------|------|--------|
| 簡單 | 慢 | 初學者 |
| 中等 | 中 | 普通玩家 |
| 困難 | 快 | 高手玩家 |

## 💾 數據存儲

遊戲使用瀏覽器的 LocalStorage 功能自動保存最高分，關閉瀏覽器後數據不會丟失。

## 🐍 Python 版本 (Pygame)

除了網頁版，我們還提供了一個功能更豐富的 Python 版本。

### 🛠️ 環境要求
- Python 3.x
- Pygame 庫

### 🚀 如何運行 Python 版本

#### Windows
1. 安裝 Python (從 python.org)
2. 打開終端或命令提示符，運行：
   ```bash
   pip install pygame
   python snake_game.py
   ```

#### Linux / macOS
1. 確保已安裝 Python 3
2. 運行啟動腳本：
   ```bash
   chmod +x run_game.sh
   ./run_game.sh
   ```

### 🎮 Python 版控制方式
- **方向鍵**：控制蛇的移動
- **C 鍵**：遊戲結束後重新開始
- **Q 鍵**：遊戲結束後退出

## 📝 代碼結構

```
.
├── index.html          # 網頁版 (HTML5/JS)
├── snake_game.py       # Python 版 (Pygame)
├── run_game.sh         # Linux/macOS 啟動腳本
└── README.md           # 項目說明文檔
```

## 🎓 學習資源

這個項目適合學習以下技術：
- HTML5 Canvas API
- JavaScript 遊戲開發基礎
- 事件監聽和處理
- 狀態管理
- 本地存儲 API

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

## 📄 許可證

MIT License

## 🎉 享受遊戲！

祝您遊戲愉快！如有任何問題或建議，歡迎提出。

---

**最後更新**：2026年1月4日