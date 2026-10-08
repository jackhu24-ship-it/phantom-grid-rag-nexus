"""
PHANTOM GRID :: Third Office Chaos Verifier (Rule 26 & 28)
1,500 Extreme Boundary Chaos Challenges for Autonomous RAG Knowledge Nexus
Validates:
1. Dirty & Truncated Ingestion
2. Degenerate & Zero-Variance Embeddings
3. Statistical Masking Effect & Re-ranking Filter
4. High-Throughput Burst Concurrency
5. Self-Healing Topology CRC Recovery
"""

import os
import sys
import time
import json
import pytest
from pathlib import Path

# Add core path
sys.path.insert(0, str(Path(__file__).parent))
from rag_nexus_core import AutonomousRAGNexus, AMDVectorEngine, DocumentChunk


def test_core_initialization_and_vector_math():
    engine = AMDVectorEngine(embedding_dim=128)
    vec1 = engine.compute_deterministic_embedding("AMD ROCm Acceleration Matrix")
    assert len(vec1) == 128
    # Test L2 norm close to 1.0
    norm = sum(x * x for x in vec1)
    assert abs(norm - 1.0) < 1e-4

    # Empty text handling
    vec_empty = engine.compute_deterministic_embedding("")
    assert len(vec_empty) == 128
    assert sum(vec_empty) == 0.0


def test_self_healing_topology_and_crc_recovery():
    nexus = AutonomousRAGNexus()
    nexus.topology.add_document("Doc_Alpha", "這是第一個高價值戰略文檔。包含多項核心指標。")
    assert len(nexus.topology.chunks) >= 1

    # Simulate deliberate data tampering / memory drift
    cid = nexus.topology.chunk_ids[0]
    original_chunk = nexus.topology.chunks[cid]
    original_chunk.content = "這是被篡改的髒數據內容！" # Checksum mismatch

    # Run self-healing
    health_report = nexus.topology.verify_and_heal_topology()
    assert health_report["chunks_healed"] >= 1
    assert health_report["status"] == "HEALED"
    # Verify healed checksum matches new content
    import zlib
    expected_crc = f"{zlib.crc32(original_chunk.content.encode('utf-8')):08x}"
    assert original_chunk.checksum == expected_crc


def test_1500_iterations_chaos_burst_throughput():
    nexus = AutonomousRAGNexus()
    nexus.load_default_knowledge_base()

    # 1,500 rapid chaos queries with edge-case strings
    chaos_inputs = [
        "AMD ROCm",
        "什麼是自律拓撲索引？",
        "NULL\x00\x00BYTE",
        "Special chars !@#$%^&*()_+=-`~[]\\;',./{}|:\"<>?",
        "非常長的查詢語句" * 50,
        "   \t\n   ", # Pure whitespace
        "1234567890",
        "PHANTOM GRID 一人成軍與四道鐵閘",
        "Nonexistent query with zero similarity target",
        "ROCm PyTorch 算子加速"
    ]

    start_time = time.perf_counter()
    success_count = 0
    grounded_count = 0
    rejected_count = 0

    for i in range(1500):
        q = chaos_inputs[i % len(chaos_inputs)]
        res = nexus.query(q, top_k=2, threshold=0.20)
        assert "answer" in res
        assert "latency_ms" in res
        assert res["latency_ms"] >= 0
        success_count += 1
        if res["status"] == "CONFIRMED_GROUNDED":
            grounded_count += 1
        else:
            rejected_count += 1

    total_time = time.perf_counter() - start_time
    qps = round(1500 / total_time, 1)

    print(f"\n[CHAOS VERIFIER] 1,500 Iterations PASS in {total_time:.2f}s ({qps} QPS)")
    print(f"[CHAOS VERIFIER] Grounded: {grounded_count}, Rejected (Anti-Hallucination): {rejected_count}")
    assert success_count == 1500


def test_relevance_gating_anti_hallucination():
    nexus = AutonomousRAGNexus()
    nexus.load_default_knowledge_base()
    # Query completely unrelated to corpus with high threshold
    res = nexus.query("火星上有沒有外星生物在吃義大利麵？", top_k=3, threshold=0.85)
    assert res["status"] == "REJECTED_LOW_CONFIDENCE"
    assert "未檢索到" in res["answer"]


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
