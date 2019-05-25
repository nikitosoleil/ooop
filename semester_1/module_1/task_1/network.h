#pragma once

#include <iostream>
#include <vector>
#include <ctime>
#include <map>

#include "server.h"

using namespace std;

class Network
{
private:
	vector < Server* > servers; // vector of servers in this network
	int duration; // number of steps in simulation
	float step_duration; // in seconds
public:
	Network(int d, float sd): duration(d), step_duration(sd) {}
	~Network();
	vector < Server* > const& get_servers() const; // servers getter
	void add_server(Server *server); // add a server to this network
	void run(bool verbose); // simulation
	void step(bool verbose); // one step of simulation
};