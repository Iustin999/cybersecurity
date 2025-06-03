# MD5 File Integrity Checker

## Description (EN)

This project demonstrates a simple and educational Python application used to verify the integrity of .txt files by comparing their MD5 hash values. Developed as a student project, the tool calculates the digital fingerprint (hash) of a selected file and compares it with a user-provided reference value.

The application features a user-friendly GUI built with tkinter and uses Python's hashlib library for hash generation. It is particularly useful for basic file validation tasks, such as checking whether a file was altered during download or transfer.

Although MD5 is no longer recommended for cryptographic applications, it remains a fast and lightweight method for non-critical integrity checks.

### Key Features
- Calculates MD5 hashes from file content
- Verifies integrity by comparing with a reference hash
- Intuitive GUI with real-time feedback
- Uses standard Python libraries (cross-platform)

### Documentation
📄 Full project documentation:  
[MD5-security.pdf](./MD5-security.pdf) (written in Romanian)

---

## Descriere (RO)

Proiectul constă într-o aplicație grafică dezvoltată în Python care permite verificarea integrității fișierelor .txt folosind algoritmul MD5. Utilizatorul selectează un fișier, iar aplicația calculează automat hash-ul acestuia și îl compară cu un hash de referință introdus manual.

Interfața este simplă și accesibilă chiar și celor fără cunoștințe de programare. Soluția este orientată spre aplicații educaționale sau necritice, unde este suficient un mecanism de verificare rapid.

### Funcționalități
- Calcul automat al hash-ului MD5 din conținutul fișierului
- Comparare cu hash-ul introdus pentru verificare integritate
- Interfață grafică simplă (tkinter)
- Ușor de folosit și portabil

### Documentație
📄 Documentația completă a proiectului se găsește aici:  
[MD5-security.pdf](./MD5-security.pdf) (scrisă în limba română)
