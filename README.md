
<div align="center">

# 🐱 NekoLog

### Professional Pet Finance Management System

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![SQLite](https://img.shields.io/badge/sqlite-3.0%2B-07405e?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/) [![Rich](https://img.shields.io/badge/UI-Rich-ff00ff?style=for-the-badge)](https://github.com/Textualize/rich) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com/)

**A production-ready CLI application for tracking pet expenses with enterprise-grade architecture**

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#install">Install</a> •
  <a href="#structure">Structure</a>
</p>

</div>

## 📋 Table of Contents

-   [Overview](#overview)
-   [Features](#features)
-   [Architecture](#architecture)
-   [Tech Stack](#tech)
-   [Installation](#install)
-   [Usage](#usage)
-   [Project Structure](#structure)
-   [Contributing](#contributing)
-   [License](#license)

----------

## <a id="overview"></a>🎯 Overview

**NekoLog** is a sophisticated terminal-based financial management system engineered for pet owners who demand professional-grade expense tracking. Built on **SOLID principles** and **Clean Architecture**, it transforms simple record-keeping into a powerful analytics platform.

### Why NekoLog?


| Problem | NekoLog Solution |
|--|--|
| 📊 Scattered expense records | Centralized SQLite database with ACID compliance |
|🔍 No visibility into spending patterns | Real-time analytics dashboard with aggregated reports|
|📝 Manual data entry errors|Input validation and data integrity constraints|
|🎨 Boring spreadsheets|Beautiful terminal UI with Rich library|
|🔄 No relationship tracking|Proper Foreign Key relationships between entities|

### Target Users

-   🏠 **Pet Owners**: Track individual expenses per pet
-   💼 **Pet Businesses**: Manage expenses across multiple animals
-   📈 **Data Enthusiasts**: Analyze spending patterns with built-in analytics
-   🎓 **Students**: Learn Clean Architecture principles through practical example

----------

## <a id="features"></a>✨ Features

### Core Functionality

#### 🐈 Cat Profile Management

-   **Full CRUD Operations**: Create, Read, Update, Delete with validation
-   **Attribute Tracking**: Name, breed, age, and custom notes
-   **Unique Constraints**: Prevent duplicate entries
-   **Soft Delete Support**: Archive without losing historical data

#### 💰 Expense Tracking

-   **Relational Design**: Link expenses to specific cat profiles via Foreign Keys
-   **Category System**: Organize by food, medical, grooming, toys, etc.
-   **Multi-Currency Support**: (Roadmap feature)
-   **Date-Range Filtering**: Query expenses by time period
-   **Receipt Notes**: Attach detailed descriptions to each transaction

#### 📊 Analytics Dashboard

-   **Sultan Leaderboard**: Rank cats by total spending with SQL aggregations
-   **Visual Reports**: Beautiful tables rendered with Rich library
-   **Trend Analysis**: Monthly/yearly spending summaries

#### 🎨 User Experience

-   **Interactive Navigation**: Arrow-key driven menus with Questionary
-   **Smart Search**: Fuzzy matching for quick entity selection
-   **Input Validation**: Real-time feedback on form entries
-   **Color-Coded Output**: Status indicators and semantic highlighting
-   **Responsive Design**: Adapts to terminal width

----------

## <a id="architecture"></a>🏗️ Architecture

NekoLog follows the **Model-View-Controller (MVC)** pattern with a clear separation of concerns:

```
      ┌───────────────────────────────────────────────┐
      │                 CONTROLLER                    │
      │                 (main.py)                     │
      │  Orchestrates application flow & logic loop   │
      └───────┬───────────────────────┬───────────────┘
              │                       │
      ┌───────▼───────┐       ┌───────▼───────┐
      │     VIEW      │       │     MODEL     │
      │   (UI Layer)  │       │  (Data Layer) │
      │ ───────────── │       │ ───────────── │
      │ • main_view.py│       │ • cat.py      │
      │ • cat_view.py │       │ • expense.py  │
      │ • expense_view│       │               │
      └───────────────┘       └───────┬───────┘
                                      │
                              ┌───────▼───────┐
                              │  DB CONNECTOR │
                              │ (database/db.py)│
                              └───────┬───────┘
                                      │
                              ┌───────▼───────┐
                              │    DATABASE   │
                              │   (SQLite3)   │
                              └───────────────┘
```



----------

## <a id="tech"></a>🛠️ Tech Stack

### Core Technologies
| Technology | Version | Purpose |
|--|--| -- |
| **Python** | 3.8+ | Primary language |
|**SQLite3**|3.0+|Embedded ACID-compliant relational database
|**Rich**|Latest|Terminal formatting, tables, and panels
**Questionary**|Latest|Interactive CLI prompts and forms|

### Development Tools

-   **Black**: Code formatting (PEP 8 compliance)
-   **Pylint**: Static code analysis
-   **pytest**: Unit testing framework (coming soon)
-   **mypy**: Static type checking (coming soon)

----------

## <a id="install"></a>📦 Installation

### Prerequisites
-   Python 3.8 or higher
-   pip package manager
-   Virtual environment (recommended)

### Step-by-Step Setup

#### 1. Clone Repository

```bash
git clone https://github.com/yourusername/nekolog.git
cd nekolog

```

#### 2. Create Virtual Environment

**Windows:**

```cmd
python -m venv venv
venv\Scripts\activate

```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate

```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

#### 4. Initialize Database (Automatic)

The database is auto-created on first run. No manual setup required!

#### 5. Run Application

```bash
python main.py

```

----------

## <a id="usage"></a>🚀 Usage

### Basic Workflow

```bash
# Start the application
python main.py

# Navigate using arrow keys
# Select options with Enter
# Exit with Ctrl+C or "Exit" option

```

### Common Operations

#### Adding a New Cat

```
Main Menu > Manage Cats > Add New Cat
→ Enter name: "Whiskers"
→ Enter breed: "Persian"
→ Enter age: 3
→ Enter notes: "Loves tuna"

```

#### Recording an Expense

```
Main Menu > Manage Expenses > Add New Expense
→ Select cat: [Use arrows] Whiskers
→ Enter amount: 50000
→ Select category: Food
→ Enter description: "Premium cat food"
→ Enter date: 2024-01-15

```

#### Viewing Leaderboard

```
Main Menu > Show Leaderboard
→ See ranked list of cats by total spending

```

----------

## <a id="structure"></a>📂 Project Structure

```
nekolog/
├── 📁 database/
│   ├── db.py                 # Singleton database connection manager
|	└── 📄 nekolog.db         # SQLite database (auto-generated)
│
├── 📁 models/                # Data Access Layer (DAO Pattern)
│   ├── __init__.py
│   ├── cat.py                # Cat entity CRUD operations
│   └── expense.py            # Expense entity CRUD operations
│
├── 📁 views/                 # Presentation Layer
│   ├── __init__.py
│   ├── main_view.py          # Main navigation dashboard
│   ├── cat_view.py           # Cat management UI (forms + tables)
│   └── expense_view.py       # Expense tracking UI
│
├── 📁 tests/                 # Unit & Integration Tests 
│   ├── conftest.py
│   ├── test_cat.py
│   └── test_expense.py
│
├── 📄 main.py                # Application entry point (Controller)
├── 📄 requirements.txt       # Python dependencies
├── 📄 .gitignore             # Git exclusion rules
├── 📄 LICENSE                # MIT License
└── 📄 README.md              # This file


```

----------


## <a id="contributing"></a>🤝 Contributing

We love contributions! Here's how you can help:

### Development Setup

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/nekolog.git
cd nekolog

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and test
python main.py

# Commit with conventional commits
git commit -m "feat: add amazing feature"

# Push and create PR
git push origin feature/amazing-feature

```

### Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

-   `feat:` New feature
-   `fix:` Bug fix
-   `docs:` Documentation changes
-   `style:` Code style (formatting, no logic change)
-   `refactor:` Code restructuring
-   `test:` Adding tests
-   `chore:` Maintenance tasks

### Code Style

-   Follow PEP 8 guidelines
-   Use type hints where possible
-   Add docstrings to all functions
-   Keep functions under 50 lines
-   Write descriptive variable names

----------
## <a id="license"></a>📄 License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="center">
  Copyright © 2025 <strong>Aditya Dhafa Priputra</strong>
</p>

----------
## 🙏 Acknowledgments

-   [Rich](https://github.com/Textualize/rich) - Beautiful terminal formatting
-   [Questionary](https://github.com/tmbo/questionary) - Interactive prompts
-   [SQLite](https://www.sqlite.org/) - Reliable embedded database
-   The Python community for excellent documentation

----------

## 📞 Support

-   📧 Email: aditdhafa@gmail.com
-   🐛 Issues: https://github.com/adityadhafa/nekolog/issues
-   🌟 Star this repo if you find it helpful!

----------

<div align="center">

**Built with ❤️ and ☕ by Aditya Dhafa Priputra**

[![GitHub followers](https://img.shields.io/github/followers/adityadhafa?style=social)](https://github.com/adityadhafa) 

</div>
