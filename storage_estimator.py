Lab 11
#include<iostream>
using namespace std;
int main()
{int T_sec, hours, mins, sec,R_secs ,T_mins;

cout << "Enter a time duration in seconds" << endl;
cin >> T_sec;

hours = T_sec / 3600;
R_secs = T_sec % 3600;
mins = R_secs / 60;
sec = R_secs / 60;
T_mins = T_sec / 60;

cout << " The time duration you entered is equivalent to  " << hours << " hours ," << mins <<
"  minutes and " << sec << " seconds." << endl;
cout << "The duration you entered is represented by " << T_mins << "  minutes.";
return 0;
}