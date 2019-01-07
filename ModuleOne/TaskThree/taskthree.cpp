#include <iostream>
#include <typeinfo>
#include <vector>
#include <memory>

using namespace std;

float S = 0; // initial value of global variable S is not specified in the task, I suppose it is zero

class Base
{
private:
	static int M; // number of created instances of Base class
protected:
	int N; // variable described in task, number of this instance
public:
	shared_ptr <Base> A, B; // smart pointers to nested instances
	virtual void pure_virtual_function() = 0; // just to make it abstract
	Base()
	{
		++M;
		N = M;
	}
	virtual void f(float &s) // operations made with variable S when the object is deleted, f() is used in destructor
	{
		s = 3 * s + N - 5;
	}
	virtual void g(float &s) // operations of this class and all of his parents made with variable S, g() is used in predict()
	{
		f(s);
	}
	virtual ~Base()
	{
		f(S);
	}
};

int Base::M = 0;

class Alpha : public Base
{
private:
	static int M;
public:
	void pure_virtual_function() override {};
	Alpha()
	{
		++M;
		N = M;
	}
	void f(float &s) override
	{
		s = s / 3 - N;
	}
	void g(float &s) override
	{
		f(s);
		Base::f(s);
	}
	~Alpha() override
	{
		f(S);
	}
};

int Alpha::M = 0;

class Beta : public Base
{
private:
	static int M;
public:
	void pure_virtual_function() override {};
	Beta()
	{
		++M;
		N = M;
	}
	void f(float &s) override
	{
		s = s + 2 * N + 5;
	}
	void g(float &s) override
	{
		f(s);
		Base::f(s);
	}
	~Beta() override
	{
		f(S);
	}
};

int Beta::M = 0;

class Red : public Alpha
{
private:
	static int M;
public:
	Red()
	{
		++M;
		N = M;
	}
	void f(float &s) override
	{
		s = s - float(N) / 2;
	}
	void g(float &s) override
	{
		f(s);
		Alpha::f(s);
		Base::f(s);
	}
	~Red() override
	{
		f(S);
	}
};

int Red::M = 0;

class Green : public Alpha
{
private:
	static int M;
public:
	Green()
	{
		++M;
		N = M;
	}
	void f(float &s) override
	{
		s = s - float(N) / 2 - 5;
	}
	void g(float &s) override
	{
		f(s);
		Alpha::f(s);
		Base::f(s);
	}
	~Green() override
	{
		f(S);
	}
};

int Green::M = 0;

void f(shared_ptr<Base> now, float &res) // recursive helper function for making prediction
{
	now->g(res); // that is the actual order nested objects are deleted
	if (now->B)
		f(now->B, res);
	if(now->A)
		f(now->A, res);
}

float predict(vector < shared_ptr<Base> > vec) // make a prediction of variable S value after deleting of vec
{
	float ret = S;
	for(auto it: vec)
		f(it, ret);
	return ret;
}

int main()
{
	{   // some vector of objects for demo, big enough to make it convincing
		vector < shared_ptr<Base> > vec;

		auto one = make_shared<Green>();
		one->A = make_shared<Red>();
		one->A->A = make_shared <Alpha> ();
		one->A->B = make_shared <Green> ();
		one->B = make_shared <Beta> ();
		one->B->A = make_shared <Red> ();
		one->B->B = make_shared <Beta> ();
		vec.push_back(one);

		auto two = make_shared<Alpha>();
		vec.push_back(two);

		auto three = make_shared<Red>();
		three->A = make_shared<Green>();
		three->B = make_shared<Beta>();
		vec.push_back(three);

		cout << "Value of variable S after vector of objects deletion" << endl;
		float predicted = predict(vec);
		cout << "Predicted: " << predicted << endl;
	}
	cout << "Actual: " << S << endl;
	// predicted and actual values should match, i tested it for many differently built vectors
	return 0;
}