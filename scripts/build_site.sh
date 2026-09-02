#!/usr/bin/env bash
set -euo pipefail
preview=""
if [[ "${1:-}" == "--preview" ]]; then
  preview="--preview"
fi
python3 scripts/sync_research_editions.py
python3 scripts/render_research_sources.py ${preview}
python3 scripts/build_publication_site.py ${preview}
