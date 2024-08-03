#include <bits/stdc++.h>
using namespace std;
string gett(int k) {
  int place = min(6, k); // maximum number of digits that will be grater than 1
  int have = pow(9, place);
  int summ = place * 9 + (k - place);
  int i = 1;
  while ((have) >= (summ)) {
    have /= 9;
    summ -= 9;
    summ += 1;
  }
  have *= 9;
  // having all digits greater than 1 as 9 and all others as 1
  string s(k, '1');
  int hav2 = have;
  i = 0;
  while (hav2 >= 9) {
    s[i] = '9';
    hav2 /= 9;
    i++;
  }

  i = 0;
  summ += 9 - 1;
  int sum2 = summ;

  // incrementally decreasing the digits from 9
  while (s[i] == '9') {
    int dig = 9;
    for (int j = 1; j <= 9; j++) {
      hav2 = (have / 9) * j;
      sum2 = summ - 9 + j;
      if (hav2 >= sum2) {
        have = hav2;
        summ = sum2;
        dig = j;
        break;
      }
    }
    s[i] = dig + '0';
    i++;
  }
  sort(s.begin(), s.end());
  return s;
}
int main() {
  int k;
  cin >> k;
  cout << gett(k) << endl;
  return 0;
}
