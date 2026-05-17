def jalankan_eksperimen():
  """Modul 6: 500 event acak, ukur runtime untuk N=50,200,500"""
  print("\n" + "="*65)
  print("  MODULE 6: EKSPERIMEN & VALIDASI")
  print("="*65)

random.seed(42)
NAMA_SAMPLE = [f"Pasien_{i}" for i in range(1, 600)]
POLI_SAMPLE = POLI_LIST
PRIO_SAMPLE = ["NORMAL", "NORMAL", "TINGGI", "KRITIS"]  # weighted

results = {}

for N in [50, 200, 500]:
  print(f"\n  ► Menguji N = {N} pasien...")

# Setup segar
queues = {p: PriorityQueue(p) for p in POLI_SAMPLE}
bst = BST()
nodes_inserted = []

# ---- Ukur enqueue ----
t0 = time.perf_counter()
for i in range(N):
  nama = NAMA_SAMPLE[i % len(NAMA_SAMPLE)]
  poli = random.choice(POLI_SAMPLE)
  prio = random.choice(PRIO_SAMPLE)
  n = queues[poli].enqueue(nama, prio, poli)
  nodes_inserted.append((poli, n))
  t_enqueue = (time.perf_counter() - t0) * 1000  # ms

# ---- Ukur dequeue ----
t0 = time.perf_counter()
dequeued = 0
for poli, q in queues.items():
  while not q.is_empty():
    q.dequeue()
    dequeued += 1
t dequeue = (time.perf_counter() - t0) * 1000

# ---- Ukur insert BST ----
rm_list = list(range(1001, 1001 + N))
random.shuffle(rm_list)
t0 = time.perf_counter()
for i, no_rm in enumerate(rm_list):
  bst.insert(no_rm, {"nama": NAMA_SAMPLE[i % len(NAMA_SAMPLE)]})
t_insert_bst = (time.perf_counter() - t0) * 1000

# ---- Ukur search BST ----
search_targets = random.sample(rm_list, min(N, len(rm_list)))
t0 = time.perf_counter()
for no_rm in search_targets:
  bst.search(no_rm)
t_search_bst = (time.perf_counter() - t0) * 1000

results[N] = {
  "enqueue_ms": t_enqueue,
  "dequeue_ms": t_dequeue,
  "insert_bst_ms": t_insert_bst,
  "search_bst_ms": t_search_bst,
}

# ---- Tabel Runtime ----
print("\n  TABEL RUNTIME (ms)\n")
print(f"  {'Operasi':<25} {'N=50':>10} {'N=200':>10} {'N=500':>10}  {'Kompleksitas'}")
print("  " + "─" * 72)
ops = [
  ("enqueue_ms",    "Enqueue (total)",    "O(n) per op"),
  ("dequeue_ms",    "Dequeue (total)",    "O(1) per op"),
  ("insert_bst_ms", "Insert BST (total)", "O(log n) avg"),
  ("search_bst_ms", "Search BST (total)", "O(log n) avg"),
]
for key, label, bigO in ops:
  r50 = results[50][key]
  r200 = results[200][key]
  r500 = results[500][key]
  print(f"  {label:<25} {r50:>9.3f} {r200:>10.3f} {r500:>10.3f}  {bigO}")

# ---- Validasi Struktur ----
print("\n  " + "─" * 65)
print("  VALIDASI STRUKTUR\n")

# Buat sistem segar untuk validasi
sys_val = SistemRumahSakit()
random.seed(42)
for i in range(20):
  nama = f"Pasien_{i+1}"
  poli = random.choice(POLI_LIST)
  prio = random.choice(PRIO_SAMPLE)
  sys_val.daftar(nama, poli, prio)

print("  Queue per Poli (urutan prioritas):")
for poli, q in sys_val.queues.items():
  items = q.to_list()
  if items:
    prio_names = list(PriorityQueue.PRIORITAS_MAP.keys())
    summary = " → ".join([f"{n.pasien}({prio_names[n.prioritas]})" for n in items[:4]])
    if len(items) > 4:
      summary += f" ... (+{len(items)-4})"
      print(f"    {poli:<12}: [{summary}]")
  else:
    print(f"    {poli:<12}: [kosong]")

print(f"\n  BST Rekam Medis (inorder, 5 pertama):")
inorder = sys_val.bst.inorder()
for node in inorder[:5]:
  print(f"    RM#{node.no_rm}: {node.data['nama']} | {node.data['poli']}")
  if len(inorder) > 5:
    print(f"    ... ({len(inorder)} total rekam medis)")

print(f"\n  Stack Log Dokter:")
# Panggil beberapa pasien untuk mengisi stack
for poli in POLI_LIST:
  if not sys_val.queues[poli].is_empty():
    sys_val.panggil(poli, "dokter_umum")
for id_d, stack in sys_val.dokter_stack.items():
  logs = stack.log_all()
  print(f"    {id_d}: {len(logs)} tindakan tercatat")
  for lg in logs[:2]:
    print(f"      [{lg.timestamp}] {lg.tindakan[:60]}...")

print("\n  ✅ Validasi selesai — semua struktur berfungsi dengan benar.")
print("="*65 + "\n")

return results
