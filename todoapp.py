http://localhost:5000
```  [oai_citation:1‡Week11 - Assignment.pdf](sediment://file_0000000063e871f7b8ede34671d1951f)

---

## ⚙️ Controllers You Need (3 total)

### 1. `/` → Main Page
This does TWO things:
- Shows all tasks in a table
- Shows a form to add a new task  [oai_citation:2‡Week11 - Assignment.pdf](sediment://file_0000000063e871f7b8ede34671d1951f)

---

### 2. `/submit` → Handles Form Submission
This must:
- Get `task`, `email`, `priority`
- Validate:
  - Email is valid
  - Priority is Low / Medium / High
- If invalid → redirect back
- If valid → add to list
- Then redirect back to `/`  [oai_citation:3‡Week11 - Assignment.pdf](sediment://file_0000000063e871f7b8ede34671d1951f)

---

### 3. `/clear` → Clears List
- Empties the list
- Redirects back to `/`  [oai_citation:4‡Week11 - Assignment.pdf](sediment://file_0000000063e871f7b8ede34671d1951f)

---

## 🧱 Your Data Structure (IMPORTANT)
Use a list of dictionaries like this:

```python
todo_list = [
    {"task": "Buy milk", "email": "test@gmail.com", "priority": "High"}
]