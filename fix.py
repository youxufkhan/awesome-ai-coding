#!/usr/bin/env python3
"""
Awesome AI Coding Tools, IDEs & Agents — Discovery and Update Tool
Automates the discovery of trending AI coding tools, formats markdown table entries
according to category schemas, and updates README.md with changelogs.
"""

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import sys

WORKSPACE_ROOT = Path(__file__).resolve().parent
README_PATH = WORKSPACE_ROOT / "README.md"

SECTIONS = {
    "CLI Agents": "## 🤖 AI Coding CLI Agents & SWE Systems",
    "IDEs": "## 💻 AI-Native IDEs & Cloud Workspaces",
    "Extensions": "## 🧩 AI Coding Extensions & Plugins",
    "Skills": "## 🔌 Custom Agent Skills & Plugins",
    "Gateways": "## 🛡️ AI Gateways, Proxies & Agent Security",
    "Frameworks": "## ⚙️ AI Agent Frameworks & Multi-Agent Platforms",
    "DevTools": "## 🛠️ LLM DevTools & Orchestration Infrastructure",
    "MCP": "## 📡 Model Context Protocol (MCP) Servers",
    "Inference": "## ⚡ LLM Inference & Local Serving Engines",
    "VectorDB": "## 🗄️ Vector Databases & Vector Stores",
    "Vibe": "## 🎨 Vibe Coding & Generative UI Tools",
    "Learning": "## 📖 AI Learning & Educational Resources",
}

SECTION_SHORT_NAMES = {
    "CLI Agents": "AI Coding CLI Agents",
    "IDEs": "AI-Native IDEs",
    "Extensions": "AI Coding Extensions",
    "Skills": "Custom Agent Skills",
    "Gateways": "AI Gateways & Security Proxies",
    "Frameworks": "AI Agent Frameworks",
    "DevTools": "LLM DevTools",
    "MCP": "MCP Servers",
    "Inference": "LLM Inference Engines",
    "VectorDB": "Vector Databases",
    "Vibe": "Vibe Coding",
    "Learning": "AI Learning",
}

AI_KEYWORDS = [
    "ai", "llm", "agent", "coding", "code", "copilot", "mcp", "rag",
    "developer", "ide", "prompt", "inference", "vibe", "vector",
    "terminal", "editor", "autocomplete", "swe", "eval", "skill",
]

# Non-coding filters to avoid noise (e.g. phone apps, general voice/audio without coding context, etc.)
EXCLUDE_TERMS = [
    "detox", "phone", "satellite", "wallpaper", "movie", "song",
    "music player", "youtube-dl", "android app", "live-chat, email support",
    "voice ai", "elevenlabs alternative", "subdomain service"
]

def get_existing_repos(readme_path=README_PATH):
    existing = set()
    if not readme_path.exists():
        return existing
    with open(readme_path, "r", encoding="utf-8") as f:
        for line in f:
            for m in re.findall(r"github\.com/([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)", line):
                existing.add(m.lower().rstrip("/"))
    return existing

def run_gh_json(cmd):
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(res.stdout)
    except Exception:
        return []

def get_maturity_badge(stars):
    if stars >= 1000:
        return "🟢"
    elif stars >= 500:
        return "🟡"
    return "🔴"

def categorize_repo(name, desc, full_name, topics=None):
    text = f"{name} {desc} {full_name} {' '.join(topics or [])}".lower()

    if any(k in text for k in ["tutorial", "roadmap", "curated list", "collection of", "awesome-", "course", "handbook", "for-beginners", "guide"]):
        return "Learning"
    if "mcp" in text or "model context protocol" in text or "fastmcp" in text:
        return "MCP"
    if any(k in text for k in ["agent skill", "claude skill", "skills", ".claude", "skill", "diagram types for claude"]):
        return "Skills"
    if any(k in text for k in ["ide", "cloud workspace", "desktop assistant"]) and not any(k in text for k in ["extension", "plugin", "proxy", "tutorial"]):
        return "IDEs"
    if any(k in text for k in ["extension", "vs code", "vscode", "plugin", "neovim", "cursor extension"]) and "skill" not in text:
        return "Extensions"
    if any(k in text for k in ["coding agent", "terminal agent", "swe-agent", "cli agent", "pair programmer", "swe", "cli programmer"]) or (name in ["opencode", "codex", "hermes-agent", "pi", "kimi-cli"]):
        return "CLI Agents"
    if any(k in text for k in ["gateway", "proxy", "guardrail", "redact", "pii", "firewall"]):
        return "Gateways"
    if any(k in text for k in ["multi-agent", "swarm", "agent framework", "orchestration framework", "actor"]):
        return "Frameworks"
    if any(k in text for k in ["inference engine", "inference server", "serving engine", "vllm", "sglang", "ollama", "gguf", "llama.cpp", "airllm", "ktransformers"]):
        return "Inference"
    if any(k in text for k in ["vector database", "vector store", "embedding database", "vectordb"]):
        return "VectorDB"
    if any(k in text for k in ["vibe coding", "vibe", "generative ui", "text-to-website", "website cloner", "wireframe"]):
        return "Vibe"
    return "DevTools"

def is_ai_coding_relevant(repo_info):
    text = f"{repo_info['name']} {repo_info['description']} {repo_info['full_name']}".lower()
    if any(ex in text for ex in EXCLUDE_TERMS):
        return False
    return any(kw in text for kw in AI_KEYWORDS)

def discover_candidates(limit_per_query=8):
    existing = get_existing_repos()
    candidates = {}

    queries = [
        ("user_starred", ["gh", "api", "/users/youxufkhan/starred?per_page=40"]),
        ("coding_agent", ["gh", "search", "repos", "coding agent", "--sort", "stars", "--order", "desc", f"--limit={limit_per_query}", "--json", "fullName,name,owner,stargazersCount,description"]),
        ("agent_skill", ["gh", "search", "repos", "agent skill", "--sort", "stars", "--order", "desc", f"--limit={limit_per_query}", "--json", "fullName,name,owner,stargazersCount,description"]),
        ("mcp_server", ["gh", "search", "repos", "mcp server", "--sort", "stars", "--order", "desc", f"--limit={limit_per_query}", "--json", "fullName,name,owner,stargazersCount,description"]),
        ("vibe_coding", ["gh", "search", "repos", "vibe coding", "--sort", "stars", "--order", "desc", f"--limit={limit_per_query}", "--json", "fullName,name,owner,stargazersCount,description"]),
        ("ai_coding", ["gh", "search", "repos", "ai coding", "--sort", "stars", "--order", "desc", f"--limit={limit_per_query}", "--json", "fullName,name,owner,stargazersCount,description"]),
    ]

    for qname, cmd in queries:
        items = run_gh_json(cmd)
        for item in items:
            full_name = item.get("full_name") or item.get("fullName")
            if not full_name:
                continue
            full_lower = full_name.lower()
            if full_lower in existing or full_lower in candidates:
                continue

            owner = item.get("owner", {}).get("login") if isinstance(item.get("owner"), dict) else (item.get("owner") or full_name.split("/")[0])
            name = item.get("name") or full_name.split("/")[1]
            desc = (item.get("description") or "").strip()
            stars = item.get("stargazers_count") if "stargazers_count" in item else item.get("stargazersCount", 0)

            c_info = {
                "full_name": full_name,
                "name": name,
                "owner": owner,
                "stars": stars,
                "description": desc,
            }

            if is_ai_coding_relevant(c_info):
                cat = categorize_repo(name, desc, full_name)
                c_info["category"] = cat
                candidates[full_lower] = c_info

    return sorted(candidates.values(), key=lambda x: x["stars"], reverse=True)

def format_row(repo_info):
    cat = repo_info["category"]
    maturity = get_maturity_badge(repo_info["stars"])
    name = repo_info["name"]
    url = f"https://github.com/{repo_info['full_name']}"
    owner = repo_info["owner"]
    desc = repo_info["description"]
    
    # Strip common GitHub boilerplate
    if "Contribute to " in desc:
        desc = desc.split("Contribute to ")[0].strip()
    desc = desc.rstrip(".- ")
    if not desc.endswith("."):
        desc += "."

    col1 = f"{maturity} **[{name}]({url})** <br> [![Stars](https://img.shields.io/github/stars/{repo_info['full_name']}?style=flat-square&label=%E2%98%85)]({url})"

    # Schema-specific column formatting
    if cat == "Skills":
        target = repo_info.get("target") or "Claude Code / General Agents"
        return f"| {col1} | {owner} | {desc} | {target} |"
    elif cat == "Extensions":
        platform = repo_info.get("platform") or "VS Code / Cursor"
        return f"| {col1} | {platform} | {owner} | {desc} |"
    elif cat == "MCP":
        tools = repo_info.get("features") or "Custom tools & integrations"
        return f"| {col1} | {owner} | {desc} | {tools} |"
    else:
        features = repo_info.get("features") or "Automated, open-source"
        return f"| {col1} | {owner} | {desc} | {features} |"

def extract_tool_name(row_line):
    m = re.search(r"\*\*\[(.*?)\]", row_line)
    return m.group(1).lower() if m else row_line.lower()

def apply_updates(vetted_items, readme_path=README_PATH):
    if not readme_path.exists():
        print(f"Error: README not found at {readme_path}")
        return False

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Changelog
    today = datetime.now().strftime("%Y-%m-%d")
    changelog_lines = []
    for item in vetted_items:
        sec_short = SECTION_SHORT_NAMES.get(item["category"], item["category"])
        changelog_lines.append(f"- [{item['name']}](https://github.com/{item['full_name']}) → {sec_short}")

    changelog_block = f"### {today} — Weekly Update\n**Added:**\n" + "\n".join(changelog_lines) + "\n\n"

    if f"### {today} — Weekly Update" not in content:
        content = content.replace("## 📋 Changelog\n", f"## 📋 Changelog\n\n{changelog_block}", 1)

    # 2. Group items by section header
    items_by_header = {}
    for item in vetted_items:
        header = SECTIONS.get(item["category"])
        if not header:
            continue
        row = format_row(item)
        items_by_header.setdefault(header, []).append(row)

    # 3. Insert rows into markdown tables
    lines = content.split("\n")
    new_lines = []
    i = 0
    curr_target_header = None

    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        # Check if line matches a section header
        for hdr in items_by_header.keys():
            if line.strip().startswith(hdr):
                curr_target_header = hdr
                break
        else:
            if line.startswith("## ") and curr_target_header:
                curr_target_header = None

        if curr_target_header and line.startswith("| :---"):
            table_rows = []
            i += 1
            while i < len(lines) and lines[i].startswith("|"):
                table_rows.append(lines[i])
                i += 1
            
            # Append new rows and sort alphabetically
            table_rows.extend(items_by_header[curr_target_header])
            table_rows.sort(key=extract_tool_name)
            new_lines.extend(table_rows)

            curr_target_header = None
            if i < len(lines):
                new_lines.append(lines[i])
        i += 1

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

    print(f"Successfully added {len(vetted_items)} items to {readme_path} under date {today}.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Update Awesome AI Coding list")
    parser.add_argument("--discover", action="store_true", help="Discover candidate repositories")
    parser.add_argument("--limit", type=int, default=8, help="Limit per query for discovery")
    parser.add_argument("--json", action="store_true", help="Output discovery results in JSON format")
    parser.add_argument("--apply-file", type=str, help="Path to JSON file containing vetted candidates to apply")
    args = parser.parse_args()

    if args.apply_file:
        with open(args.apply_file, "r") as f:
            vetted = json.load(f)
        apply_updates(vetted)
        return

    candidates = discover_candidates(limit_per_query=args.limit)

    if args.json:
        print(json.dumps(candidates, indent=2))
        return

    print(f"\nDiscovered {len(candidates)} candidate repositories:\n")
    print(f"{'Category':<15} | {'Stars':<8} | {'Repository':<35} | {'Description'}")
    print("-" * 90)
    for c in candidates:
        mat = get_maturity_badge(c["stars"])
        print(f"{c['category']:<15} | {mat} {c['stars']:<5} | {c['full_name']:<35} | {c['description'][:50]}")

if __name__ == "__main__":
    main()

