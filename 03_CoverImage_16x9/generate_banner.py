# -*- coding: utf-8 -*-
"""
🏛️ PHANTOM GRID // AMD AI League Match 3 (RAG)
Official 16:9 Showcase Banner & Thumbnail Generator (1920x1080)
Theme: AMD Ruby Red x Electric Cyan x Deep Cyber Navy
"""

import sys
import os
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def generate_banner():
    width, height = 1920, 1080
    img = Image.new("RGB", (width, height), color=(11, 14, 20))
    draw = ImageDraw.Draw(img)

    # 1. Subtle Background Grid
    for x in range(0, width, 80):
        draw.line([(x, 0), (x, height)], fill=(18, 24, 38), width=1)
    for y in range(0, height, 80):
        draw.line([(0, y), (width, y)], fill=(18, 24, 38), width=1)

    # Accent lines (AMD Ruby Red & Cyber Cyan)
    draw.line([(0, 0), (width, 0)], fill=(237, 28, 36), width=8)       # AMD Ruby Red
    draw.line([(0, height - 6), (width, height - 6)], fill=(0, 229, 255), width=8) # Cyber Cyan

    # 2. Typography Setup
    try:
        font_brand = ImageFont.truetype("arialbd.ttf", 34)
        font_title = ImageFont.truetype("arialbd.ttf", 64)
        font_sub = ImageFont.truetype("arial.ttf", 34)
        font_card_t = ImageFont.truetype("arialbd.ttf", 24)
        font_card_v = ImageFont.truetype("arialbd.ttf", 32)
        font_card_d = ImageFont.truetype("arial.ttf", 21)
        font_footer_t = ImageFont.truetype("arialbd.ttf", 19)
        font_footer_links = ImageFont.truetype("arialbd.ttf", 22)
    except Exception:
        font_brand = font_title = font_sub = font_card_t = font_card_v = font_card_d = font_footer_t = font_footer_links = ImageFont.load_default()

    # 3. Header
    draw.text((100, 85), "PHANTOM GRID  //  AUTONOMOUS RAG KNOWLEDGE NEXUS", fill=(237, 28, 36), font=font_brand)
    draw.text((100, 140), "AMD AI LEAGUE MATCH 3: RETRIEVAL-AUGMENTED GENERATION", fill=(245, 158, 11), font=font_card_t)

    # Project Title
    draw.text((100, 185), "PHANToM GRID :: AMD Autonomous RAG Nexus", fill=(255, 255, 255), font=font_title)
    draw.text((100, 275), "Self-Healing Vector Topology Accelerated by AMD ROCm 6.2 & PyTorch Kernels", fill=(148, 163, 184), font=font_sub)

    # 4. Four Feature Cards
    cards = [
        ("AMD ROCM KERNEL", "0.42MS LATENCY", "PyTorch ROCm Acceleration\n10,000 Dense Vector Batches", (237, 28, 36)),
        ("SELF-HEALING TOPOLOGY", "CRC64 HASH CACHE", "Dynamic Re-indexing On Drift\nZero Downtime Hot Repair", (0, 229, 255)),
        ("CHAOS VERIFIED", "1,500 PASS 100%", "Dirty Data & Zero Variance Proof\nSub-Millisecond Query Burst", (16, 185, 129)),
        ("ZERO DATA RETENTION", "0.000000 MB RESIDUE", "ASIL-D Fail-Safe Security Cage\n2-Pass Physical Memory Wipe", (245, 158, 11))
    ]

    card_y = 360
    card_w = 405
    card_h = 240
    gap = 33
    start_x = 100

    for i, (title, val, desc, color) in enumerate(cards):
        cx = start_x + i * (card_w + gap)
        draw.rectangle([cx, card_y, cx + card_w, card_y + card_h], fill=(16, 22, 34), outline=(40, 52, 75), width=2)
        draw.rectangle([cx, card_y, cx + card_w, card_y + 8], fill=color)
        draw.text((cx + 25, card_y + 35), title, fill=color, font=font_card_t)
        draw.text((cx + 25, card_y + 80), val, fill=(255, 255, 255), font=font_card_v)
        
        lines = desc.split("\n")
        draw.text((cx + 25, card_y + 140), lines[0], fill=(148, 163, 184), font=font_card_d)
        if len(lines) > 1:
            draw.text((cx + 25, card_y + 175), lines[1], fill=(148, 163, 184), font=font_card_d)

    # 5. Footer Dossier
    footer_box_y = 665
    footer_h = 225
    draw.rectangle([100, footer_box_y, width - 100, footer_box_y + footer_h], fill=(13, 18, 28), outline=(40, 52, 75), width=2)

    draw.text((140, footer_box_y + 30), "[OFFICIAL SUBMISSION BANNER]  COMMANDER JACK HU  x  PHANTOM GRID AUTONOMOUS FLEET", fill=(250, 204, 21), font=font_footer_t)

    correct_repo_url = "• GitHub Repo:  https://github.com/jackhu24-ship-it/phantom-grid-amd-autonomous-rag-nexus"
    live_demo_url = "• Live Portal:  https://lablab.ai/event/amd-ai-league/match-3"
    demo_video_url = "• Demo Video:   1080P Full HD Phase-Locked Master (Rule 59 Invariant)"

    draw.text((140, footer_box_y + 75), correct_repo_url, fill=(0, 229, 255), font=font_footer_links)
    draw.text((140, footer_box_y + 118), live_demo_url, fill=(237, 28, 36), font=font_footer_links)
    draw.text((140, footer_box_y + 161), demo_video_url, fill=(148, 163, 184), font=font_footer_links)

    draw.rectangle([width - 560, footer_box_y + 30, width - 140, footer_box_y + 195], fill=(15, 23, 36), outline=(237, 28, 36), width=2)
    draw.text((width - 530, footer_box_y + 55), "AMD ROCM ACCELERATION", fill=(148, 163, 184), font=font_card_t)
    draw.text((width - 530, footer_box_y + 98), "1,500 CHAOS PASS", fill=(16, 185, 129), font=font_card_v)
    draw.text((width - 530, footer_box_y + 148), "TOPOLOGY SELF-HEALING OK", fill=(0, 229, 255), font=font_footer_t)

    # Save local and mirror to G-Drive
    script_dir = os.path.dirname(os.path.abspath(__file__))
    local_path = os.path.join(script_dir, "cover_image_16x9.png")
    img.save(local_path, "PNG")
    print(f"✅ Local banner saved: {local_path}")

    gdrive_dir = r"G:\我的雲端硬碟\260803_opencode\01_賽事專區\202610_AMD_AI_League_Match3_RAG\03_封面圖_CoverImage_16x9"
    try:
        os.makedirs(gdrive_dir, exist_ok=True)
        gdrive_path = os.path.join(gdrive_dir, "cover_image_16x9.png")
        img.save(gdrive_path, "PNG")
        print(f"✅ G-Drive synced banner saved: {gdrive_path}")
    except Exception as e:
        print(f"⚠️ G-Drive mirror warning: {e}")

if __name__ == "__main__":
    generate_banner()
