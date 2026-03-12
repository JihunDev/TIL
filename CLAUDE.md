# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal TIL (Today I Learned) knowledge base — a static documentation site using [Docsify](https://docsify.js.org/) deployed to [Netlify](https://jihun2til.netlify.app/). There is no build pipeline or compilation step; all content is plain Markdown rendered client-side by Docsify.

## Local Development

```bash
npm i docsify-cli -g   # one-time install
docsify serve ./Docs   # serve at http://localhost:3000
```

## Content Creation

Use the automation script for new entries:

```bash
# One-time setup
chmod +x Docs/scripts/create-til.sh
echo 'alias til="/path/to/TIL/Docs/scripts/create-til.sh"' >> ~/.bashrc

# Usage
til quick "topic"       # quick note (80% of use cases)
til tech  "topic"       # technical analysis
til bug   "topic"       # troubleshooting record
til cheatsheet "topic"  # command/tool reference
til code  "topic"       # code analysis
til exp   "topic"       # experiment/benchmark
```

Templates live in `Docs/3-Resources/31-Templates/`.

## Content Organization

Follows **PARA + Johnny Decimal** methodology:

```
Docs/
├── 1-Projects/          # Active project docs (FODRo, LKAS)
├── 2-Areas/             # Long-term knowledge areas
│   ├── 21-Embedded/     # C, hardware, embedded systems
│   ├── 22-ROS2/         # ROS2, Nav2
│   ├── 23-DevOps/       # Git, Linux, CI/CD
│   ├── 24-Network/
│   ├── 25-Vision/       # Image processing, computer vision
│   ├── 26-SignalProcessing/
│   └── 27-SoftwareEngineering/
├── 3-Resources/         # Templates and cheatsheets
├── 4-Archives/          # Completed/retired content
└── scripts/
    └── create-til.sh
```

### File Naming Convention

```
[CategoryNumber].[SequenceNumber]-[Topic].md
[CategoryNumber].[SequenceNumber]-Bug-[Topic].md   # troubleshooting
[CategoryNumber].[SequenceNumber]-Exp-[Topic].md   # experiment/benchmark
```

Example: `23.04-Linux-sudo_Option.md`, `21.02-Bug-CAN_Timeout_Error.md`

### Frontmatter

All documents use YAML frontmatter:

```yaml
---
title: ""
date: YYYY-MM-DD
tags: []
project: ""     # FODRo | LKAS | General
status: active  # active | archived
related: []     # cross-references to other docs
---
```

## Navigation

`Docs/_sidebar.md` is the manually maintained sidebar navigation. When adding new documents, update `_sidebar.md` to include a link to the new file.

## Deployment

Netlify auto-deploys from the `master` branch. Publish directory is `Docs/`. No build command needed.
