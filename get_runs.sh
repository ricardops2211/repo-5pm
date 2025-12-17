#!/bin/sh

# No hace falta definir variables manualmente.
# GitHub Actions pasará:
#   - REPO_FULL: OWNER/REPO
#   - GITHUB_TOKEN: secret automático

if [ -z "$REPO_FULL" ] || [ -z "$GITHUB_TOKEN" ]; then
  echo "❌ Error: REPO_FULL o GITHUB_TOKEN no definidos"
  exit 1
fi

API_URL="https://api.github.com/repos/$REPO_FULL/actions/runs"
OUTPUT="runs.json"

echo "📥 Obteniendo ejecuciones de workflows de $REPO_FULL..."

curl -s \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "$API_URL" > $OUTPUT

if [ $? -eq 0 ]; then
  echo "✅ Datos guardados en $OUTPUT"
else
  echo "❌ Error al obtener datos"
  exit 1
fi
