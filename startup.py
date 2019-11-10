# Runs the GPT-2M system inside of a text interface

# Imports
import generalUtilities as gu

# Main Thread
def main():
    # Welcome message
    print("\n<< Welcome to GPT-2M Main Control >>")

    # Enter menu functions
    options = ["Generation Menu"]
    gu.textMenu("GPT-2M Main Menu", options, "Quit", mainMenuFunctions)

    # Safe to exit message
    print("\nGPT-2M has shutdown successfully.\nIt is now safe to close this window.")

# Functions for the main menu
def mainMenuFunctions(answer):
    # Check which option was selected
    if answer == "0":
        # Open the generation menu
        options = ["Option_To_Be_Done"]
        gu.textMenu("Generation Menu", options, "Back to Main Menu", mainMenuFunctions)

# Execute Main Thread
if __name__ == '__main__':
    main()
