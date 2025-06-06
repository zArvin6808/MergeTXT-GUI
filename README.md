# MergeTXT-GUI
TXT 合并精灵 - MergeTXT GUI

> **一个绿色便携、带图形界面的 TXT 文件合并工具**

## 🌟 简介

**MergeTXT GUI** 是一款专为整理 `.txt` 文本文件设计的轻量级工具。  
它可以帮助你将多个 `.txt` 文件按自然顺序（如 `1.txt`, `2.txt`, `10.txt`）一键合并为一个完整文档，支持中文不乱码、进度条显示、无命令行窗口干扰。

非常适合用于整理小说章节、学习笔记、技术文档等长文本内容。

---

## ✅ 主要功能

| 功能 | 描述 |
|------|------|
| 🧾 图形界面操作 | 带窗口按钮，点击选择文件夹即可开始合并，操作简单直观 |
| 🔢 自然排序算法 | 按文件名中的数字正确排序，避免 `1.txt`, `10.txt`, `2.txt` 的乱序问题 |
| 📁 支持拖拽/点击选择 | 可点击“选择文件夹”按钮，也可直接拖入文件夹路径 |
| 🖼️ 自定义图标 | 程序自带美观图标，识别度高，不显示默认控制台黑框 |
| 💾 绿色免安装 | 不写注册表、不依赖系统环境，适合放 U 盘随身携带 |
| 📄 中文友好 | 使用 UTF-8 编码读写文件，支持中文内容不乱码 |
| 📊 实时进度条 | 显示合并进度和当前处理的文件名，让用户清楚知道合并状态 |

---

## 🚀 使用方法

1. 将所有 `.txt` 文件与 `merge_gui.exe` 放在同一目录下（或任意文件夹中）
2. 双击运行 `merge_gui.exe`
3. 点击 “选择文件夹” 或将文件夹直接拖入程序窗口
4. 点击 “开始合并”
5. 合并完成后，会在所选文件夹中生成 `merged.txt`

---

## 📁 文件结构说明

project_root/

│

├── merge_gui.exe # 主程序（绿色免安装）

├── icon/ # 图标资源目录（含 app_icon.ico）

└── README.md # 当前说明文档


## ⚙️ 技术实现

- 编程语言：Python 3.x
- 图形界面：Tkinter
- 打包工具：PyInstaller
- 图标格式：`.ico`（多尺寸嵌入，含 256x256 PNG 层）
- 排序方式：自然排序算法（自动识别文件名中的数字）

---

## 📝 注意事项

- ✅ 支持 Windows 7 / 10 / 11 系统
- ❌ 不支持 macOS/Linux（GUI 版仅限 Windows）
- ✅ 无需安装 Python 运行时，已打包为独立 `.exe` 文件
- ✅ 合并后的文件名为 `merged.txt`，位于原始文件夹内
- ✅ 支持中文内容，使用 UTF-8 编码防止乱码

---

## 🧩 开源与二次开发

本工具基于 Python 开发，提供完整的源码支持，欢迎进行扩展或定制：

### 可拓展方向：
- 导出为 EPUB/PDF 格式
- 添加封面页、目录结构
- 多语言切换（中英文）
- 支持子目录查找 `.txt` 文件
- 拖拽支持、日志记录、批量处理等

如果你希望我为你提供源代码或打包脚本，请告诉我！

---
