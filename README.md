# Badminton Cost Calculator

This is a simple Python desktop application with a graphical user interface (GUI) created using the `tkinter` library. The app allows users to calculate the cost per person for badminton birdies based on the cost per birdie, the total number of birdies used, and the names of participants.

---

## Features
- Input fields to specify:
  - **Cost per birdie**
  - **Number of birdies used**
  - **Names of attendees** (comma-separated)
- Output displayed in the format:
  ```
  X颗球，Y个人，$Z/人
  ```
  - **X**: Total number of birdies used
  - **Y**: Number of attendees
  - **Z**: Cost per person (in dollars)

---

## How to Run the Application

### Prerequisites
- Python 3.x installed on your system.

### Steps to Run
1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the following command to start the application:
   ```bash
   python badminton_calculator.py
   ```

### Usage
1. Enter the cost per birdie in the first input field.
2. Enter the total number of birdies used in the second input field.
3. Enter the names of attendees, separated by commas, in the third input field.
4. Click the **Calculate** button.
5. The result will be displayed in a popup window in the format specified.

---

## File Structure
- `badminton_calculator.py`: Main Python script containing the application logic.

---

## Future Plans
- Extend the project to a cross-platform mobile app using Flutter.
- Allow users to save calculations and track their history.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.
