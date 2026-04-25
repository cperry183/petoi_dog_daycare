<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License" />
</div>

<h1 align="center">🐕 Petoi Dog Daycare Management System</h1>

<p align="center">
  <strong>A Python-based object-oriented system for efficiently managing dog daycare operations, including tracking dogs, scheduling activities, and revenue.</strong>
</p>

---

## 📖 Overview

This project provides a robust and intuitive **Dog Daycare Management System** developed in Python. It leverages an object-oriented design to effectively track individual dogs, manage their daily activities, and handle the financial aspects of a dog daycare. The system is designed to be flexible, allowing for easy customization and extension to meet specific operational needs. It focuses on simplifying the complex tasks associated with running a dog daycare, from check-ins and playtimes to feeding schedules and special care requirements.

### ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 🐶 **Dog Management** | Tracks individual dogs, including their energy levels, hunger, happiness, and any special needs or medical requirements. |
| 🗓️ **Daily Operations** | Facilitates check-in/out processes, schedules group playtime, and manages feeding schedules for all dogs. |
| 💰 **Revenue Tracking** | Automates billing based on daily rates per dog, providing clear financial oversight. |
| 🧠 **Smart Logic** | Implements conditional activities, such as automatically napping tired dogs, to optimize dog welfare and staff efficiency. |
| ❤️ **Special Needs Support** | Allows for the recording and management of dietary restrictions and specific medical requirements for each dog. |

---

## 📂 Repository Structure

```text
petoi_dog_daycare/
├── src/                            # Core application source code
│   ├── __init__.py                 # Initializes the src package
│   ├── cli.py                      # Command-line interface for interacting with the system
│   ├── daycare.py                  # Defines the Daycare class for managing operations
│   ├── dog.py                      # Defines the PetioDog class for individual dog management
│   └── usage.py                    # Example script demonstrating system usage
├── tests/                          # Unit and integration tests
│   └── ...                         # Test files (e.g., test_dog.py, test_daycare.py)
├── .gitignore                      # Specifies intentionally untracked files to ignore
├── requirements.txt                # Lists project dependencies
└── README.md                       # This README file
```

---

## 🚀 Getting Started

Follow these instructions to set up and run the Petoi Dog Daycare Management System on your local machine.

### Prerequisites

*   **Python 3.8+** installed on your system.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/cperry183/petoi_dog_daycare.git
    cd petoi_dog_daycare
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Usage Example

To see the system in action, you can run the `usage.py` script:

```bash
python src/usage.py
```

This script demonstrates how to:
*   Initialize a `Daycare` instance.
*   Register `PetioDog` instances.
*   Perform daily operations like check-in, group play, feeding, and check-out.

---

## ⚙️ Core Components

### `PetioDog` Class (`src/dog.py`)

Represents an individual dog attending the daycare. Each `PetioDog` instance tracks attributes such as name, breed, owner, energy, hunger, happiness, and special needs. It includes methods for checking in/out, eating, and reporting its status.

### `Daycare` Class (`src/daycare.py`)

Manages the overall daycare operations. The `Daycare` class handles dog registration, check-in/out processes, group activities, and revenue tracking. It interacts with `PetioDog` instances to manage their states and activities throughout the day.

---

## 🤝 Contributing

Contributions are highly welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and ensure your code adheres to the project's style guidelines.
4.  Write and run tests to ensure functionality (`pytest tests/`).
5.  Commit your changes (`git commit -m 'Add new feature'`).
6.  Push to the branch (`git push origin feature/your-feature-name`).
7.  Open a Pull Request with a clear description of your changes.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
