from src.data_structures.linked_list import Node
class Node:
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

from dataclasses import dataclass, field
from typing import List, Optional
# Struktur Data Rekam Medis sesuai starter code
@dataclass
class RekorMedis:
    no_rm: int
    nama: str
    riwayat: List[str] = field(default_factory=list)

class BSTNode:
    def __init__(self, rekord: RekorMedis):
        self.rekord = rekord
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

class BSTRekamMedis:
    def __init__(self):
        self.root = None

    def insert(self, rekord: RekorMedis):
        """Big-O: rata-rata O(log n), worst-case O(n)"""
        if self.root is None:
            self.root = BSTNode(rekord)
            return
        self._insert_rekursif(self.root, rekord)

    def _insert_rekursif(self, node, rekord):
        if rekord.no_rm < node.rekord.no_rm:
            if node.left is None:
                node.left = BSTNode(rekord)
            else:
                self._insert_rekursif(node.left, rekord)
        elif rekord.no_rm > node.rekord.no_rm:
            if node.right is None:
                node.right = BSTNode(rekord)
            else:
                self._insert_rekursif(node.right, rekord)

    def search(self, no_rm: int):
        """Big-O: rata-rata O(log n)"""
        return self._search_rekursif(self.root, no_rm)

    def _search_rekursif(self, node, no_rm):
        if node is None:
            return None
        if node.rekord.no_rm == no_rm:
            return node.rekord
        elif no_rm < node.rekord.no_rm:
            return self._search_rekursif(node.left, no_rm)
        else:
            return self._search_rekursif(node.right, no_rm)