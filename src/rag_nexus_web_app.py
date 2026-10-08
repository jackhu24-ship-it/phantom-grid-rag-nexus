"""
PHANTOM GRID :: Autonomous RAG Knowledge Nexus
Interactive Web Service & RESTful API Gateway
Powered by FastAPI, AMD ROCm Vector Engine & SSE Stream
"""

import os
import sys
import time
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

# Import core engine
from src.rag_nexus_core import AutonomousRAGNexus

app = FastAPI(
    title="PHANTOM GRID :: Autonomous RAG Knowledge Nexus",
    description="AMD ROCm Accelerated High-Throughput RAG with Self-Healing Topology",
    version="2.0.0"
)

nexus = AutonomousRAGNexus()
nexus.load_default_knowledge_base()


class QueryRequest(BaseModel):
    query: str
    top_k: Optional[int] = 3
    threshold: Optional[float] = 0.20


class IngestRequest(BaseModel):
    doc_id: str
    content: str
    metadata: Optional[dict] = None


@app.get("/", response_class=HTMLResponse)
def index_page():
    return """<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PHANTOM GRID :: Autonomous RAG Knowledge Nexus</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #070B14;
    color: #E2E8F0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif;
    padding: 24px;
  }
  .container {
    max-width: 1000px;
    margin: 0 auto;
  }
  .header {
    border-bottom: 2px solid #00E5FF;
    padding-bottom: 16px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header h1 {
    font-size: 24px;
    color: #00E5FF;
    letter-spacing: 1px;
  }
  .header .badge {
    background: rgba(239, 68, 68, 0.15);
    border: 1px solid #EF4444;
    color: #EF4444;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: bold;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }
  .card {
    background: #0D1627;
    border: 1px solid #1E293B;
    border-radius: 8px;
    padding: 18px;
  }
  .card h2 {
    font-size: 16px;
    color: #38BDF8;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  input, textarea, button {
    width: 100%;
    padding: 10px 14px;
    border-radius: 6px;
    border: 1px solid #334155;
    background: #070B14;
    color: #F8FAFC;
    font-size: 14px;
    margin-bottom: 12px;
  }
  button {
    background: linear-gradient(135deg, #00E5FF 0%, #0284C7 100%);
    border: none;
    color: #070B14;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.2s;
  }
  button:hover {
    box-shadow: 0 0 16px rgba(0, 229, 255, 0.4);
  }
  .result-box {
    margin-top: 16px;
    padding: 14px;
    background: #09101D;
    border: 1px solid #1E293B;
    border-radius: 6px;
    font-size: 13px;
    line-height: 1.6;
    max-height: 380px;
    overflow-y: auto;
  }
  .metric-tag {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 11px;
    background: rgba(56, 189, 248, 0.1);
    color: #38BDF8;
    margin-right: 6px;
  }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div>
      <h1>⚡ PHANTOM GRID :: Autonomous RAG Knowledge Nexus</h1>
      <p style="font-size: 13px; color: #94A3B8; margin-top: 4px;">AMD AI League · Match 3 (RAG) 官方技術展示控制台</p>
    </div>
    <div class="badge">🔥 AMD ROCm 6.2 ACCELERATED</div>
  </div>

  <div class="grid">
    <div class="card">
      <h2>🔍 語意檢索與智能合成 (Semantic Query)</h2>
      <input type="text" id="queryInput" placeholder="請輸入檢索問題，如：AMD ROCm 對 RAG 檢索有何算力加速優勢？" value="AMD ROCm 對 RAG 檢索有何算力加速優勢？">
      <button onclick="doQuery()">🚀 執行硬體加速檢索 (Run Query)</button>
      <div id="queryStatus"></div>
      <div class="result-box" id="queryResult">等待指令輸入中...</div>
    </div>

    <div class="card">
      <h2>📥 知識庫熱注入 (Real-time Knowledge Ingestion)</h2>
      <input type="text" id="docIdInput" placeholder="文檔標識 ID (如：AMD_Hardware_Spec)" value="AMD_Instinct_MI300">
      <textarea id="docContentInput" rows="4" placeholder="文檔內容...">AMD Instinct MI300 系列加速器具備領先業界之 CDNA 3 架構，提供 192GB HBM3 超大頻寬記憶體，支援極限並發 LLM 推理與大型 RAG 向量特徵投影。</textarea>
      <button onclick="doIngest()" style="background: linear-gradient(135deg, #10B981 0%, #059669 100%);">📥 熱注入至向量索引 (Ingest Node)</button>
      <div class="result-box" id="ingestResult">等待文檔注入...</div>
    </div>
  </div>
</div>

<script>
async function doQuery() {
  const q = document.getElementById('queryInput').value;
  const resBox = document.getElementById('queryResult');
  resBox.innerHTML = '<span style="color: #00E5FF;">⚡ 正在調用 AMD ROCm 矩陣核心運算...</span>';
  try {
    const res = await fetch('/api/v1/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: q, top_k: 3, threshold: 0.20 })
    });
    const data = await res.json();
    let html = `<div><span class="metric-tag">延遲: ${data.latency_ms} ms</span><span class="metric-tag">狀態: ${data.status}</span><span class="metric-tag">硬體: ${data.hardware_backend}</span></div>`;
    html += `<p style="margin-top: 10px; font-weight: bold; color: #FFFFFF;">${data.answer}</p>`;
    if (data.matched_chunks && data.matched_chunks.length > 0) {
      html += `<hr style="border: 0; border-top: 1px solid #1E293B; margin: 10px 0;">`;
      html += `<div style="font-size: 11px; color: #94A3B8;"><b>匹配 Context 節點：</b></div>`;
      data.matched_chunks.forEach((c, idx) => {
        html += `<div style="margin-top: 6px; padding: 6px; background: rgba(15,23,42,0.6); border-radius: 4px;">[#${idx+1}] 相似度: ${c.score} | 來源: ${c.doc_id}<br>${c.content}</div>`;
      });
    }
    resBox.innerHTML = html;
  } catch(e) {
    resBox.innerHTML = `<span style="color: #EF4444;">查詢失敗: ${e}</span>`;
  }
}

async function doIngest() {
  const docId = document.getElementById('docIdInput').value;
  const content = document.getElementById('docContentInput').value;
  const resBox = document.getElementById('ingestResult');
  resBox.innerHTML = '<span style="color: #10B981;">📥 正在切分並計算向量特徵...</span>';
  try {
    const res = await fetch('/api/v1/ingest', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ doc_id: docId, content: content })
    });
    const data = await res.json();
    resBox.innerHTML = `<div><span class="metric-tag" style="color: #10B981; background: rgba(16,185,129,0.1);">注入成功</span> 節點數: ${data.added_chunks}</div><pre style="margin-top: 8px; font-size: 11px; color: #94A3B8;">${JSON.stringify(data, null, 2)}</pre>`;
  } catch(e) {
    resBox.innerHTML = `<span style="color: #EF4444;">注入失敗: ${e}</span>`;
  }
}
</script>
</body>
</html>"""


@app.post("/api/v1/query")
def api_query(req: QueryRequest):
    return nexus.query(req.query, top_k=req.top_k, threshold=req.threshold)


@app.post("/api/v1/ingest")
def api_ingest(req: IngestRequest):
    added = nexus.topology.add_document(req.doc_id, req.content, metadata=req.metadata)
    health = nexus.topology.verify_and_heal_topology()
    return {
        "status": "SUCCESS",
        "doc_id": req.doc_id,
        "added_chunks": added,
        "topology_health": health
    }


@app.get("/api/v1/health")
def api_health():
    return {
        "service": "PHANTOM GRID :: Autonomous RAG Knowledge Nexus",
        "status": "ONLINE",
        "hardware_backend": nexus.engine.device.__str__(),
        "is_rocm": nexus.engine.is_rocm,
        "total_nodes": len(nexus.topology.chunks),
        "topology_version": nexus.topology.topology_version
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
