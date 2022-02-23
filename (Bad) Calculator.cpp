#include <iostream>
#include <string>
using namespace std;

// +
int main() {
	int num1, num2;
	cout << "Add", '\n';
	cout << "Enter a full Number: ";
	cin >> num1;
	cin.clear();
	cin.ignore(99, '\n');
	cout << "Enter a 2nd full Number: ";
	cin >> num2;
	int sum = num1 + num2;
	cout << "The sum is: " << sum << " Stupid!" ;
	cout << '\n';
}

// -
int main() {
	int num3, num4;
	cout << "Take away", '\n';
	cout << "Enter a full Number: ";
	cin >> num1;
	cin.clear();
	cin.ignore(99, '\n');
	cout << "Enter a 2nd full Number: ";
	cin >> num4;
	int sum2 = num3 - num4;
	cout << "The sum is: " << sum2 << " Stupid!" ;
	cout << '\n';
}

// /
int main() {
	int num5, num6;
	cout << "Divide", '\n';
	cout << "Enter a full Number: ";
	cin >> num5;
	cin.clear();
	cin.ignore(99, '\n');
	cout << "Enter a 2nd full Number: ";
	cin >> num6;
	int sum3 = num5 / num6;
	cout << "The sum is: " << sum3 << " Stupid!" ;
	cout << '\n';
}

// *
int main() {
	int num7, num8;
	cout << "Times", '\n';
	cout << "Enter a full Number: ";
	cin >> num7;
	cin.clear();
	cin.ignore(99, '\n');
	cout << "Enter a 2nd full Number: ";
	cin >> num8;
	int sum4 = num7 * num8;
	cout << "The sum is: " << sum4 << " Stupid!" ;
	cout << '\n';
}





// Decimal Numbers

// +
int main() {
	float num9, num10;
	cout << "Add", '\n';
	cout << "Enter a Decimal Number: ";
	cin >> num9;
	cin.clear();
	cin.ignore(99, '\n');
	cout << "Enter a 2nd Decimal Number: ";
	cin >> num10;
	float sum5 = num9 + num10;
	cout << "The sum is: " << sum5 << " Stupid!" ;
	cout << '\n';
}

// -
int main() {
	float num11, num12;
	cout << "Take away", '\n';
	cout << "Enter a Decimal Number: ";
	cin >> num11;
	cin.clear();
	cin.ignore(99, '\n');
	cout << "Enter a 2nd Decimal Number: ";
	cin >> num12;
	float sum6 = num11 - num12;
	cout << "The sum is: " << sum6 << " Stupid!" ;
	cout << '\n';
}

// /
int main() {
	float num13, num14;
	cout << "Divide", '\n';
	cout << "Enter a Decimal Number: ";
	cin >> num13;
	cin.clear();
	cin.ignore(99, '\n');
	cout << "Enter a 2nd Decimal Number: ";
	cin >> num14;
	float sum7 = num13 / num14;
	cout << "The sum is: " << sum7 << " Stupid!" ;
	cout << '\n';
}

// *
int main() {
	float num15, num16;
	cout << "Times", '\n';
	cout << "Enter a Decimal Number: ";
	cin >> num15;
	cin.clear();
	cin.ignore(99, '\n');
	cout << "Enter a 2nd Decimal Number: ";
	cin >> num16;
	float sum8 = num15 * num16;
	cout << "The sum is: " << sum8 << " Stupid!" ;
	cout << '\n';
}


// ++

int main() {
	int x, y;
	cout << "Enter a full Number: ";
	cin >> x;
	cin.clear();
	cin.ignore(99, '\n');
	cout << "How much do you want to add?: ";
	cin >> y;
	answer = x += y;
	cout << "Answer: " << answer;
	cout << '\n';
}



// + - Add
// - - Minus
// / - Divide
// * - Times
// ++ - Incriment (Add by)
// -- - Decriment (Minus by)
// % - Works out the remainder e.g. 8 divided by 5 equals 1 remainder 3 (1 r3)  x % y

// ! - Not - !false = true and !true = false) or (1 < 2 would be true but !(1 < 2) is false
// && - And - Both the Left and the Right are both true for it to be true (true && true) (false && false is false)
// || - Or - true and true, false and true, true and false are all true but false and false


// int main() {
// bool x = '1' < '2'
// //(True or False)
// }

// < - Less than
// > - Greater than
// <= - Less than or equil to
// >= - Greater than or equail to
// != - Is not equil to
// == - Is equil to


// Uses BIDMAS - Brackets, Indecise, Division, Multiplication, Add, Subtract,