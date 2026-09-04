#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$REPO_DIR/skills"
TIMESTAMP="$(date -u +%Y%m%d-%H%M%S)-$$"

usage() {
  sed -n '1,90p' "$REPO_DIR/README.md"
}

install_to() {
  local target="$1"
  local backup="$target/.ga2-backup/$TIMESTAMP"
  local source name destination

  mkdir -p "$target"

  for source in "$SKILLS_DIR"/ga2-*; do
    name="$(basename "$source")"
    destination="$target/$name"

    if [[ -e "$destination" || -L "$destination" ]]; then
      mkdir -p "$backup"
      mv "$destination" "$backup/$name"
    fi

    cp -R "$source" "$destination"
  done

  printf 'Instaladas 31 skills em %s\n' "$target"
}

if [[ $# -eq 0 ]]; then
  usage
  exit 2
fi

targets=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --todos)
      targets+=(
        "$HOME/.claude/skills"
        "${CODEX_HOME:-$HOME/.codex}/skills"
        "$HOME/.cursor/skills"
        "$HOME/.config/opencode/skills"
        "$HOME/.agents/skills"
      )
      shift
      ;;
    --claude)
      targets+=("$HOME/.claude/skills")
      shift
      ;;
    --codex)
      targets+=("${CODEX_HOME:-$HOME/.codex}/skills")
      shift
      ;;
    --cursor)
      targets+=("$HOME/.cursor/skills")
      shift
      ;;
    --opencode)
      targets+=("$HOME/.config/opencode/skills")
      shift
      ;;
    --agents)
      targets+=("$HOME/.agents/skills")
      shift
      ;;
    --destino)
      if [[ $# -lt 2 || -z "$2" ]]; then
        printf 'Informe uma pasta depois de --destino.\n' >&2
        exit 2
      fi
      targets+=("$2")
      shift 2
      ;;
    --ajuda|-h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Opção desconhecida: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

declare -A seen=()
for target in "${targets[@]}"; do
  if [[ -z "${seen[$target]:-}" ]]; then
    install_to "$target"
    seen[$target]=1
  fi
done
