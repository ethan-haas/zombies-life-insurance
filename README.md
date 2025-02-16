# Zombies Life Insurance

A Python-based computer vision tool designed to automate the "Life Insurance" exploit (Alt+F4) in Call of Duty: Black Ops 6 Zombies, providing a temporary save state upon player down.  This allows for a single additional "life" per round.

## Description

This utility leverages OpenCV to monitor the game screen in real-time. Upon detection of the player "down" state, it automatically executes the Alt+F4 command, effectively reverting the game to the last save point. This grants the player a second chance within the round.

## Features

*   **Real-time Screen Monitoring:** Utilizes OpenCV for image processing and analysis.
*   **Automated Exploit Execution:** Automatically triggers the Alt+F4 command.
*   **Multi-Monitor Support:** Configurable for various monitor setups.
*   **Screenshot Logging:** Captures screenshots for verification and debugging.
*   **Configurable Detection:** Adjustable settings for personalized performance.

## Requirements

*   Python 3.x
*   OpenCV (`opencv-python`)
*   NumPy (`numpy`)
*   MSS (`mss`)
*   Keyboard (`keyboard`)
*   Colorama (`colorama`)

## Exploit Limitations

The temporary save state functionality has the following limitations:

*   **Round 1 Down:**  The exploit will not function if the player goes down during the first round.
*   **Multiple Downs per Round:** Multiple downs within the same round will not create new save states. A new save state is generated at the start of each new round.

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/ethan-haas/zombies-life-insurance.git
    cd zombies-life-insurance
    ```

2.  Install dependencies:

    ```bash
    pip install opencv-python numpy mss keyboard colorama
    ```

## Usage

1.  Launch Call of Duty: Black Ops 6 Zombies.
2.  Run the script:

    ```bash
    python life_insurance.py
    ```

3.  Press `Ctrl+C` to terminate the script.

## Configuration

The `screen_capture_and_detect` function within the script allows for customization of the following parameters:

*   Detection Threshold (default: 0.6)
*   Monitor Selection
*   Screenshot Saving Options

## Disclaimer

This tool is provided for educational purposes only.  The use of exploits may be a violation of the game's terms of service and could result in account penalties.  Use this tool at your own discretion and risk.

## License

MIT License

## Contributing

Contributions are welcome. For significant changes, please open an issue for discussion beforehand.  Pull requests are encouraged.
