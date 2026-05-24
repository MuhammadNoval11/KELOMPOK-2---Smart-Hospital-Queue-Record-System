# Smart Hospital Queue & Record System

[cite_start]A integrated Command Line Interface (CLI) application designed to simulate an intelligent health information system for **RSUP Dr. Sardjito Yogyakarta**[cite: 6, 10]. [cite_start]This system manages high-volume outpatient visits (50–500 patients/day) by integrating three main data structures: **Priority Queues** for clinics, **Stacks** for doctor action logs, and a **Binary Search Tree (BST)** for Medical Records[cite: 4, 6, 12].

---

## 📌 Project Overview & Architecture

[cite_start]This project is a simulation framework for managing a healthcare facility workflow, consisting of the following core pipelines[cite: 13]:

1. [cite_start]**Multi-Clinic Priority Queue**: Manages 5 major clinics (Umum, Jantung, Ortopedi, Anak, Gigi) using Singly Linked Lists. [cite_start]Patients are categorized into 3 levels: `KRITIS` (1), `PRIORITAS` (2), and `REGULER` (3)[cite: 12]. [cite_start]`KRITIS` patients bypass the regular queue, while a FIFO rule breaks ties among patients with the same priority[cite: 14].
2. [cite_start]**Doctor Action Log (Undo Feature)**: Isolated per-doctor session logs managed by a Linked List-based Stack[cite: 14]. [cite_start]Allows doctors to `UNDO` erroneously logged clinical actions[cite: 9, 14].
3. [cite_start]**Medical Records Search**: A Binary Search Tree (BST) sorted by `no_rekam_medis` for efficient queries over historical records[cite: 14].
4. [cite_start]**Daily Report Generation**: Sorts completed patient records at the end of a session based on waiting time (descending) or queue number (ascending) using **Insertion Sort** or **Selection Sort** implemented directly over a Linked List[cite: 14].

---

## ⏱️ Big-O Complexity Specification

[cite_start]As required by the specification, every operation executed within the interactive CLI will display its respective time complexity[cite: 14]:

| Module / Operation | Mechanism | Average Case | Worst Case |
| :--- | :--- | :--- | :--- |
| **`DAFTAR` (Enqueue)** | Priority Queue (Linked List) | $O(n)$ | [cite_start]$O(n)$ (shift required) [cite: 14] |
| **`PANGGIL` (Dequeue)** | Priority Queue (Linked List) | $O(1)$ | [cite_start]$O(1)$ (head removal) [cite: 14] |
| **`UNDO_DOKTER` (Pop)**| Stack (Linked List) | $O(1)$ | [cite_start]$O(1)$ [cite: 14] |
| **`CARI_RM` (Search)** | Binary Search Tree | $O(\log n)$ | [cite_start]$O(n)$ (unbalanced tree) [cite: 14] |
| **`TAMBAH_RM` (Insert)**| Binary Search Tree | $O(\log n)$ | [cite_start]$O(n)$ (unbalanced tree) [cite: 14] |
| **`LAPORAN_HARI`** | Insertion/Selection Sort | $O(n^2)$ | [cite_start]$O(n^2)$ [cite: 14] |

---

## 💻 CLI Commands

[cite_start]The interactive interface supports the following commands[cite: 14]:

* **`DAFTAR <nama> <poli> <prioritas>`** Registers a new patient into the specified clinic queue[cite: 14].  
  *Priorities: `KRITIS` (1), `PRIORITAS` (2), `REGULER` (3)*[cite: 12].
* [cite_start]**`PANGGIL <poli>`** Calls/dequeues the next eligible patient according to priority and FIFO rules[cite: 14].
* [cite_start]**`UNDO_DOKTER <id_dokter>`** Reverts the last action recorded by the specified doctor[cite: 14].
* [cite_start]**`CARI_RM <no_rm>`** Searches for a patient's historical medical record via BST[cite: 14].
* [cite_start]**`TAMBAH_RM <data>`** Inserts a new record into the Medical Record BST[cite: 14].
* [cite_start]**`LAPORAN_HARI`** Triggers daily sorting and lists out completed session reports[cite: 14].
* [cite_start]**`BANTUAN`** Displays the list of all available commands[cite: 106].
* [cite_start]**`KELUAR`** Exits the application[cite: 14].

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher
* [cite_start]NumPy (`pip install numpy`) — *Required for the simulation seed mechanism*[cite: 22, 25].

### Installation & Executions
1. Clone this repository or navigate to your source directory:
   ```bash
   cd path/to/smart-hospital-queue
   
