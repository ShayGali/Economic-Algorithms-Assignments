
# Economic Algorithms – Assignment Solutions

Solutions, code, and documentation for the **Economic Algorithms (course 5785)** module at **Ariel University**.  
The repository accompanies the official course materials published by Dr Erel Segal‑Halevi and aggregates my submissions for the graded programming/explanation exercises.

> **Academic year:** 2024‑2025 · **Semester:** Spring · **Student:** Shay Gali

---

## ✨ Repository layout

```text
.
├── ex02/            # Assignment 2 – Random Serial Dictatorship & Pareto efficiency
├── ex04/            # Assignment 4 – Fair division & Nash‑social‑welfare maximisation
├── ex08/            # Assignment 8 – Matching markets & Top‑Trading‑Cycles
├── ex09/            # Assignment 9 – Competitive equilibrium with budgets
├── ex11/            # Assignment 11 – Combinatorial auctions & VCG mechanisms
│
├── ex01.pdf         # Original PDF of Exercise 1 (problem sheet)
├── ex05.pdf         # Original PDF of Exercise 5
├── ex06.pdf         # Original PDF of Exercise 6
├── ex07.pdf         # Original PDF of Exercise 7
├── ex09.pdf         # Original PDF of Exercise 9 – specification
├── ex10.pdf         # Original PDF of Exercise 10
└── README.md        # You are here 📄
```

Each directory contains:

* **`README.md`** – short task description and my approach  
* **`*.py` / `*.ipynb`** – well‑commented reference implementation 
---

## 📚 Course background

*Economic algorithms* study how to allocate scarce resources among strategic agents while respecting efficiency, fairness, and incentive compatibility.  
Typical topics include:

| Theme | Representative algorithms |
|-------|---------------------------|
| Fair division of indivisible goods | Random Serial Dictatorship (RSD), Probabilistic Serial |
| House allocation & matching | Top‑Trading‑Cycles (TTC) |
| Market equilibria | Fisher / Arrow–Debreu competitive equilibrium computation |
| Social choice | VCG auctions, Gibbard–Satterthwaite impossibility |

The full syllabus, lecture slides, and starter code are available in the [course repository](https://github.com/erelsgl-at-ariel/algorithms-5785).

---

## 🚀 Getting started

```bash
# 1. clone the repo
git clone https://github.com/ShayGali/Economic-Algorithms-Assignments.git
cd Economic-Algorithms-Assignments

# 2. create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. install dependencies
pip install -r requirements.txt    # or: pip install -r environment.yml

# 4. run a notebook or script
cd ex08
jupyter lab          # opens the notebook for Assignment 8
python main.py -h    # view CLI options, if provided
```

> **Tip:** Each assignment folder is self‑contained. Installing top‑level requirements is enough to execute any of them.

### Key Python packages

* **`networkx`** – graph structures & algorithms  
* **`numpy`, `scipy`, `pandas`** – numerical back‑end  
* **`matplotlib` / `seaborn`** – visualising allocations and convergence  
* **`pytest`** – automated grading tests

---

## 🧪 Testing

Run all tests:

```bash
pytest -q
```

Continuous integration (GitHub Actions) re‑runs these tests on every push to ensure solutions stay correct and reproducible.

---

## 📄 License

Unless otherwise stated in a specific sub‑directory, my code is released under the **MIT License**.  
The original problem statements belong to the course staff and are included here for academic, non‑commercial use only.

---

## 🙏 Acknowledgements

* Dr Erel Segal‑Halevi for lecturing the course and providing insightful assignments.  
* Course peers for valuable feedback and discussion.

---

_Last updated: 2025‑06-13_

