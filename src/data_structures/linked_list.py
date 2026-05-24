import time
from dataclasses import dataclass, field
from typing import Optional

# Struktur Data Pasien sesuai starter code
@dataclass
class Pasien:
    no_antrian: int
    nama: str
    poli: str
    prioritas: int  # 1-KRITIS, 2-PRIORITAS, 3-REGULER
    waktu_daftar: float = field(default_factory=time.time)
    waktu_tunggu: float = 0.0

# Node Universal untuk Queue dan Stack
class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['LLNode'] = None

        