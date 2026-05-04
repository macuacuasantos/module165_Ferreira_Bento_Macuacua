#!/bin/bash
echo "Attente de MongoDB..."
until python -c "
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
try:
    MongoClient('mongodb://mongo:27017/', serverSelectionTimeoutMS=1000).admin.command('ping')
    exit(0)
except ServerSelectionTimeoutError:
    exit(1)
" 2>/dev/null; do
  sleep 2
done

PUBLIC_PORT=${PUBLIC_PORT:-5000}
echo ""
echo "=========================================="
echo "  Application Pokémon démarrée !"
echo "=========================================="
echo "  Liste       : http://127.0.0.1:${PUBLIC_PORT}/"
echo "  Recherche   : http://127.0.0.1:${PUBLIC_PORT}/search"
echo "  Statistiques: http://127.0.0.1:${PUBLIC_PORT}/stats"
echo "=========================================="
echo ""

exec python app.py
