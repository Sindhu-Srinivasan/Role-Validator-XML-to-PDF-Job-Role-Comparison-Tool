# 🧠 AI Role Validator – XML to PDF Job Role Comparison Tool

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-blue?logo=streamlit)](https://thankabharathi-role-validator-xml-to-pdf-job-role-comparison.streamlit.app/)
[![Python](https://img.shields.io/badge/Built%20with-Python%203.9-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **An AI-powered Streamlit app that validates job roles by comparing structured XML definitions with roles extracted from unstructured PDFs. Combines Google Gemini, RAG (via Pinecone), and fuzzy string matching for intelligent role comparison and PDF report generation.**

---

## 🚀 Live Demo

🔗 [Click to Open App](https://thankabharathi-role-validator-xml-to-pdf-job-role-comparison.streamlit.app/)

---

## 📌 Overview

The **AI Role Validator** is an intelligent Python application designed to automate and streamline the process of validating job roles.

It compares a master list of roles (from an XML file) against job roles extracted from unstructured PDF documents.  
With the power of **Google Gemini**, **RAG (via Pinecone)**, and **fuzzy string matching**, it ensures high-accuracy results, highlighting inconsistencies, and saving manual effort.

---

## ✨ Features

✅ **XML Role Extraction** – Parses XML to extract the defined roles  
✅ **PDF Content Extraction** – Uses PyMuPDF to extract structured/unstructured data  
✅ **LLM-Powered Role Extraction** – Extracts roles intelligently using Google Gemini AI  
✅ **RAG-Based Enhancement** – Uses Pinecone to retrieve relevant context from PDFs  
✅ **Fuzzy Matching** – Identifies direct and partial matches, handles typos/abbreviations  
✅ **Validation Report** – Categorizes roles as:
- ✔️ Exact/Fuzzy Matches
- ❌ Unmatched/Incorrect Roles
- 🔧 Configurable similarity threshold

---

## 🧠 How Fuzzy Matching Works

1. **Levenshtein Distance (fuzz.ratio)** – Detects typos and character-level differences  
   - Example: `Tester` vs `Teater` → Similarity ≈ 83.3%

2. **Partial Matching (fuzz.partial_ratio)** – Captures abbreviations/substrings  
   - Example: `Software Engineer` vs `Software Eng.` → Partial ratio = 100%

---

## 🛠️ Technologies Used

- Python 3.9+
- Streamlit
- Google Gemini API
- Pinecone Vector Database
- PyMuPDF (`fitz`)
- TheFuzz (`fuzzywuzzy`)
- lxml
- langchain-text-splitters
- python-dotenv

---

## ⚙️ Setup & Installation

### 🔹 Prerequisites

- Python 3.9+
- Google Gemini API Key
- Pinecone API Key and Environment

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/ThankaBharathi/ThankaBharathi-Role-Validator-XML-to-PDF-Job-Role-Comparison-Tool.git
cd ThankaBharathi-Role-Validator-XML-to-PDF-Job-Role-Comparison-Tool
