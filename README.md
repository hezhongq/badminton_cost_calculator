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

## Roadmap for iOS Development

### Step 1: Install Prerequisites
1. Install **Xcode** from the Mac App Store.
2. Set up **Command Line Tools**:
   ```bash
   xcode-select --install
   ```
3. Create an Apple Developer account at [Apple Developer](https://developer.apple.com/).
4. Enable Developer Mode on your iPhone (iOS 16+):
   - Go to **Settings > Developer > Developer Mode**.

### Step 2: Create the Project
1. Launch Xcode and create a new project:
   - Choose **App** under iOS.
   - Name the project `Badminton Calculator`.
   - Select **Storyboard** as the interface and **Swift** as the language.

### Step 3: Design the Interface
1. Open `Main.storyboard`.
2. Add UI elements:
   - Labels, Text Fields, a Button, and a Label for the result.
   - Arrange them and set constraints using Auto Layout.

### Step 4: Write the Logic
1. Connect the UI elements to `ViewController.swift` using `@IBOutlet` and `@IBAction`.
2. Add the cost calculation logic to the `calculateCost` function.

### Step 5: Run and Test
1. Connect your iPhone to your Mac via USB.
2. Set your iPhone as the target device in Xcode.
3. Click **Run** to test the app on your iPhone.

### Step 6: Polish and Publish
1. Test the app for responsiveness and usability.
2. If publishing to the App Store:
   - Go to **Product > Archive** in Xcode.
   - Follow the submission process.

---

## File Structure
- `badminton_calculator.py`: Main Python script containing the desktop application logic.

---

## Future Plans
- Develop a mobile app for iOS using Swift.
- Extend to Android using Flutter for cross-platform support.
- Implement cloud storage for tracking past calculations.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.
