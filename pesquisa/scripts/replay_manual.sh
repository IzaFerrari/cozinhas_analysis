#!/usr/bin/env bash
# Replay manual (D-14): regenera a saída de um RUN numa worktree no execution freeze, com o Python
# do .venv por caminho absoluto, e compara byte a byte com o run commit.
# Uso: replay_manual.sh <execution_freeze> <run_commit> <saida> -- <comando relativo à raiz>
set -euo pipefail
ef=$1; rc=$2; out=$3; shift 4
w=$(mktemp -d)
git worktree add -q --detach "$w" "$ef"
(cd "$w" && "$@")
if git show "$rc:$out" | cmp -s - "$w/$out"; then echo EXACT; else echo DRIFT; fi
git worktree remove --force "$w"
