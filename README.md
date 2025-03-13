# National Health Service System (NHSS)

## Overview
The **National Health Service System (NHSS)** is a command-line application built using Python and Click. It allows users to manage doctors, nurses, patients, and their relationships efficiently within a hospital setting.

## Features
- Add new doctors, nurses, and patients
- Assign nurses to doctors
- Associate patients with doctors and wards
- List all doctors along with their assigned nurses and patients
- Interactive command-line interface

## Requirements
- Python 3.x
- Click (Command-line interface framework)
- SQLAlchemy (Database ORM)

## Installation
1. **Clone the repository:**
   
  git@github.com:geekirui120/NHS-SYSTEM.git
   cd NHS-SYSTEM
   
2. **Create and activate a virtual environment:**
   
   python -m venv venv
   source venv/bin/activate  
   
3. **Install dependencies:**
   
   pip install -r requirements.txt
   

## Usage
Run the interactive system by executing:

python nhss.py

### Menu Options
| Option | Action |
|--------|--------|
| 1      | Add a Doctor |
| 2      | Add a Nurse |
| 3      | Add a Patient |
| 4      | List All Doctors |
| 5      | Exit System |

## Database
The system uses SQLAlchemy for database management. Ensure your database is set up before running the application.

## Contributing
Feel free to submit issues or pull requests to improve the system.

## License
This project is licensed under the MIT License.


