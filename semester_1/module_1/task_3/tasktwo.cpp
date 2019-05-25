#include <iostream>
#include <cmath>
#include <regex>

using namespace std;

enum color { red, green, blue };

int mymod(int n, int m)
{
	return ((n%m)+m)%m; // because % is a reminder operator, not modulo, which works differently for negative values
}

pair<color, int> f(int n)
{
	if (n>0)
		return {red, mymod((1 << n)+n*n, 105)};
	else if (n<0)
		// pow() returns floating point number, so I hate using it with integer arguments
		return {green, mymod(n*n*n*n*n+n-1, 205)};
	else
		// In first case argument is positive integer, in second - negative integer. So, if argument is zero, it is seventh case
		return {red, 8395};
}

pair<color, int> f(double n)
{
	return {blue, mymod(round(1.0/sin(log2(n))), 305)};
}

pair<color, int> f(string s)
{
	int ret = 0;
	smatch result;
	while (regex_search(s, result, regex("(^|\\s+)[[:alpha:]]{3,5}($|\\s+)"))) // I can explain.
	{
		s = result.suffix().str();
		++ret;
	}
	return {green, ret};
}

template < typename A, typename B >
pair<color, int> f(pair<A, B> p)
{
	auto res_a = f(p.first);
	auto res_b = f(p.second);
	color ret_color = res_a.first;
	if (res_a.first!=res_b.first)
		// because integers corresponding to 3 different colors in enum sum up to 3 = 0+1+2
		ret_color = color(3-res_a.first-res_b.first);
	// assuming that f(a)^f(b) means powering integers in pairs returned by functions
	return {ret_color, int(round(pow(res_a.second, res_b.second)))%505};
}

template < typename T >
pair<color, int> f(vector<T> v) // there is no difference what exact data structure to use, right?
{
	vector<pair<color, int> > fv;
	for (auto vi: v)
		fv.push_back(f(vi));
	int ret_number = 0, color_count[3] = {0}, max_color_count = 0, ret_color = -1;
	for (int i = 0; i<fv.size(); ++i) {
		ret_number = mymod(ret_number+fv[i].second*fv[fv.size()-1-i].second, 705);
		int cur_color = fv[i].first;
		color_count[cur_color]++;
		if (color_count[cur_color]>=max_color_count) {
			max_color_count = color_count[cur_color];
			ret_color = cur_color;
		}
	}
	return {color(ret_color), ret_number};
}

template < typename T >
pair<color, int> f(T n)
{
	return {red, 8395};
}

void print(string comment, pair<color, int> p)
{
	vector<string> colormap({"red", "green", "blue"});
	cout << comment << colormap[p.first] << ' ' << p.second << endl;
}

int main()
{
	// One demo for each of seven cases from the task
	print("Positive integer: color = red, number = (2^n+n^2) mod 105, f(3) = ", f(3));
	print("Negative integer: color = green, number = (n^5+n-1) mod 205, f(-2) = ", f(-2));
	print("Real number: color = blue, number = [1/sin(log2(n))] mod 305, f(8.0) = ", f(8.0));
	print("String: color = green, number of word with length from 3 to 5 in string, f(\"some unu$u@al string with numbers like 666\") = ",
			f(string("some unu$u@al string with numbers like 666")));
	print("Pair (a, b): color = same or the remaining one, number = f(a)^f(b) mod 505, f((1, (1, \" a abc abcdef 123 !@# \"))) = ",
			f(make_pair(1, make_pair(1, " a abc abcdef 123 !@# "))));
	print("List: color = the last appearing most frequent, number = some sum mod 705, f({1, -2, 3, -4}) = ",
			f(vector<int>({1, -2, 3, -4})));
	print("The remaining case, color = red, number = 8395, f(true) = ", f(true));
	// Swear to god, I manually check all of the outputs - they seem to be correct
	return 0;
}
