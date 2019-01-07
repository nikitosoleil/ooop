#include <iostream>
#include <random>
#include <ctime>

#include "network.h"

default_random_engine dre(time(0));

Network* build_some_network(int duration, int step_duration, int sn, int pn, int tn) // numbers of servers, programs and messages types
{
	cout << "Building network" << endl << endl;
	Network *n = new Network(duration, step_duration);
	Server *s[sn];
	for (int i=0; i<sn; ++i)
		s[i] = new Server(i, n);
	for (int i=0; i<sn; ++i)
	{
		uniform_int_distribution <int> uid_0_5(0, 5);
		int speed = uid_0_5(dre)+1;
		if (i<sn-1)
		{
			s[i]->add_connection(Connection(s[i+1], speed)); // simple linear network
			s[i+1]->add_connection(Connection(s[i], speed));
		}
		cout << "Connection speed between servers " << i << " and " << i+1 << " is 1/" << speed << endl << endl;
		bernoulli_distribution bd_05;
		for(int j=0; j<pn; ++j)
		{
			vector <int> sends, receives;
			for (int t=0; t<tn; ++t)
			{
				if(bd_05(dre))
					sends.push_back(t);
				if(bd_05(dre))
					receives.push_back(t);
			}
			bool type = bd_05(dre);
			int period = uid_0_5(dre)+1;
			bool will_wait = bd_05(dre);
			Program *p = new Program(j, s[i], type, period, will_wait, sends, receives);
			cout << "Program " << j << ", server " << i << ":\n";
			cout << "Type: " << type << ", period: " << period << ", will_wait: " << will_wait << endl;
			cout << "Sends: ";
			for(auto it: sends)
				cout << it << " ";
			cout << endl << "Receives: ";
			for(auto it: receives)
				cout << it << " ";
			cout << endl << endl;
			s[i]->add_program(p);
		}
		n->add_server(s[i]);
	}
	return n;
}

// this is just some demo, nothing special

int main()
{
	int duration = 30; // number of steps in simulation
	int step_duration = 1; // in seconds
	int sn = 5; // number of servers
	int pn = 2; // number of programs on each server
	int tn = 5; // number of different types of messages
	Network *n = build_some_network(duration, step_duration, sn, pn, tn);
	cout << "Simulating" << endl << endl;
	bool verbose = true; // whether to display sending and receiving process
	n->run(verbose);
	cout << "Displaying results" << endl << endl;
	for(Server *s: n->get_servers())
		for(Program *p: s->get_programs())
		{
			cout << "Program " << p->get_id() << ", server " << s->get_id() << ":\n";
			p->print_stats();
		}
	delete n;
	return 0;
}