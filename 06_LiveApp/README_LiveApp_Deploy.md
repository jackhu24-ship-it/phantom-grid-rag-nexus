# 🚀 PHANTOM GRID :: Autonomous RAG Knowledge Nexus
## 線上 Demo 部署指南 (Live App Deployment Guide)

本專案支援一鍵部署至 **Hugging Face Spaces**、**Streamlit Cloud** 或 **Render/Vercel**，作為 lablab.ai 官方評審檢視之 Live App。

---

### 一、 本地極速一鍵啟動 (Local Instant Launch)
```bash
# 1. 安裝依賴
pip install -r requirements.txt

# 2. 啟動 FastAPI 服務與互動控制台
python rag_nexus_web_app.py
```
- 本地服務網址：`http://127.0.0.1:8000`
- 交互控制台：直接在瀏覽器開啟 `http://127.0.0.1:8000/` 進行檢索與熱注入
- 官方健康檢查：`http://127.0.0.1:8000/api/v1/health`

---

### 二、 一鍵部署至 Hugging Face Spaces (免費且相容 PyTorch)
1. 前往 [Hugging Face Spaces](https://huggingface.co/spaces)，點擊 **Create new Space**。
2. Space 名稱填寫：`phantom-grid-rag-nexus`
3. SDK 選擇：**Docker** 或 **Streamlit / Gradio**。
4. 將 `rag_nexus_core.py`、`rag_nexus_web_app.py`、`requirements.txt` 上傳至 Space 倉庫。
5. 建立 `Dockerfile`：
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 7860
CMD ["uvicorn", "rag_nexus_web_app:app", "--host", "0.0.0.0", "--port", "7860"]
```
6. 部署完成後，獲得專屬公開線上互動網址：  
   `https://huggingface.co/spaces/jackhu24/phantom-grid-rag-nexus`

---

### 三、 官方提交推薦填寫 Live App URL
- 填寫 URL：`https://jackhu24-rag-nexus.hf.space` 或 GitHub Pages 模擬展示頁
- 備援靜態展示頁：`06_線上Demo部署_LiveApp/index.html`（已包含於代碼庫中）
