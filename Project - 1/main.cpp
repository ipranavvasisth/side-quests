#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <fstream>
using namespace std;

const double PI = 3.14159265358979323846;

struct Force {
    double magnitude;
    double angleDegrees;
    double fx;
    double fy;
};

int main() {
    int numForces;
    double sumX = 0, sumY = 0;

    cout << "--- 2D Force System Solver ---" << endl;
    cout << "How many forces are acting on the point? ";
    cin >> numForces;

    vector<Force> forces(numForces);

    for (int i = 0; i < numForces; ++i) {
        cout << "\nEnter details for Force " << i + 1 << ":" << endl;
        cout << "Magnitude (N): ";
        cin >> forces[i].magnitude;
        cout << "Angle (degrees): ";
        cin >> forces[i].angleDegrees;

        double angleRad = forces[i].angleDegrees * (PI / 180.0);


        forces[i].fx = forces[i].magnitude * cos(angleRad);
        forces[i].fy = forces[i].magnitude * sin(angleRad);

        sumX += forces[i].fx;
        sumY += forces[i].fy;
    }


    double resultant = sqrt(pow(sumX, 2) + pow(sumY, 2));


    double resAngleRad = atan2(sumY, sumX);
    double resAngleDeg = resAngleRad * (180.0 / PI);


    cout << fixed << setprecision(2);
    cout << "\n--- Resultant Vector ---" << endl;
    cout << "Sum of Fx: " << sumX << " N" << endl;
    cout << "Sum of Fy: " << sumY << " N" << endl;
    cout << "Resultant Magnitude: " << resultant << " N" << endl;
    cout << "Resultant Angle: " << resAngleDeg << " degrees" << endl;



    ofstream outFile("forces.csv");
    outFile << "label,fx,fy,magnitude,angle\n";
    for (int i = 0; i < numForces; i++) {
        outFile << "F" << i+1 << ","
                << forces[i].fx << ","
                << forces[i].fy << ","
                << forces[i].magnitude << ","
                << forces[i].angleDegrees << "\n";
    }

    outFile << "Resultant," << sumX << "," << sumY << ","
            << resultant << "," << resAngleDeg << "\n";
    outFile.close();
    cout << "Results written to forces.csv" << endl;

    return 0;
}