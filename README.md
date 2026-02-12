# Proiect: Sistem de Gestiune a Incidentelor de Securitate (Cyber-Incidents)

### 📝 Descriere Generală
Să se scrie un program care ține evidența incidentelor cibernetice dintr-o organizație. Programul trebuie să simuleze un sistem de monitorizare de tip SOC (Security Operations Center) pentru un nivel de începător.

### 🛠️ Funcționalități Meniu
Programul trebuie să dispună de un meniu interactiv cu următoarele opțiuni:

1.  **Adăugare incident** (Exemple: SQL Injection, Brute Force, Malware, Phishing).
2.  **Afișarea incidentelor existente** (Sub formă de listă sau tabel).
3.  **Modificare informații incident existent** (Ex: actualizarea statusului sau a notelor de impact).
4.  **Ștergere incident** (Utilizată pentru eliminarea alarmelor false / False Positives).
5.  **Căutare incident** după Nume Analist sau Tip Atac.
6.  **Afișare incidente în ordinea Scorului de Risc** (Sortare descrescătoare).
7.  **Afișare incidente cu Risc Critic** (Doar cele care au Scorul de Risc peste 5).
8.  **Afișare incidente în ordine alfabetică** (După tipul atacului).

---

### 📊 Structura Datelor
Pentru fiecare incident înregistrat, se vor reține următoarele informații (echivalente cu sistemul de note școlare):

* **Tip Atac** (Numele incidentului)
* **Analist Responsabil** (Numele persoanei care investighează)
* **Impact Tehnic** (Notă de la 1 la 10)
* **Complexitate Atac** (Notă de la 1 la 10)
* **Vulnerabilitate Sistem** (Notă de la 1 la 10)
* **Scor de Risc (Media)** (Media aritmetică a celor 3 note de mai sus)

---

> **Notă Portofoliu:** Acest proiect demonstrează abilități de manipulare a datelor (CRUD), logică de sortare și aplicarea conceptelor de securitate cibernetică în dezvoltarea software.
