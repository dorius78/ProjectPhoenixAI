import sys
from pathlib import Path

# Cartella principale del progetto
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# Avvio del progetto
from AI.main import main

if __name__ == "__main__":
    main()