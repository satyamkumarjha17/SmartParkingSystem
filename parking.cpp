#include <iostream>
#include <stack>
#include <string>

using namespace std;

stack<string> parkingLot;
stack<string> tempStack;

void parkCar(const string& carNumber) {
    parkingLot.push(carNumber);
    cout << "Car " << carNumber << " parked successfully.\n";
}

void removeCar(const string& carNumber) {
    bool found = false;

    while (!parkingLot.empty()) {
        if (parkingLot.top() == carNumber) {
            parkingLot.pop();
            found = true;
            cout << "Car " << carNumber << " removed from parking.\n";
            break;
        } else {
            tempStack.push(parkingLot.top());
            parkingLot.pop();
        }
    }

    while (!tempStack.empty()) {
        parkingLot.push(tempStack.top());
        tempStack.pop();
    }

    if (!found) {
        cout << "Car " << carNumber << " not found in the parking lot.\n";
    }
}

void displayParkingLot() {
    if (parkingLot.empty()) {
        cout << "Parking lot is empty.\n";
        return;
    }

    cout << "\nCars currently in parking (Top = Last Parked):\n";
    stack<string> displayStack = parkingLot;

    while (!displayStack.empty()) {
        cout << displayStack.top() << endl;
        displayStack.pop();
    }
}

int main() {
    int choice;
    string carNumber;
    string input;

    do {
        cout << "\n======= SMART PARKING SYSTEM MENU =======\n";
        cout << "1. Park Car\n";
        cout << "2. Remove Car\n";
        cout << "3. View Parking Lot\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        getline(cin, input);

        try {
            choice = stoi(input);
        } catch (...) {
            cout << "Invalid choice. Try again.\n";
            continue; // skip rest of loop and ask again
        }

        switch (choice) {
            case 1:
                cout << "Enter car number to park: ";
                getline(cin, carNumber);
                parkCar(carNumber);
                break;

            case 2:
                cout << "Enter car number to remove: ";
                getline(cin, carNumber);
                removeCar(carNumber);
                break;

            case 3:
                displayParkingLot();
                break;

            case 4:
                cout << "Exiting... Thank you!\n";
                break;

            default:
                cout << "Invalid choice. Try again.\n";
        }

    } while (choice != 4);

    return 0;
}
