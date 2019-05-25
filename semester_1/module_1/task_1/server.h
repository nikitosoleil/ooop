#pragma once

#include <vector>

#include "all.h"
#include "program.h"
#include "network.h"

using namespace std;

struct Connection
{
	Server* server; // server connection leads to
	int speed; // actual connection speed is 1/speed, for processing all the computations in integers
	Connection(Server* server, int speed): server(server), speed(speed) {}
};

class Server
{
private:
	int id; // server id
	Network *network; // server parent network
	vector < Connection > connections; // vector of connections from this server
	vector < Program* > programs; // vector of programs running on this server
public:
	Server(int i, Network *n): id(i), network(n) {}
	~Server();
	int get_id(); // id getter
	void add_program(Program *program); // add a program running on this server
	void add_connection(Connection connection); // add a connection starting from this server
	void set_network(Network *n); // network setter
	vector < Program* > const& get_programs() const; // programs getter
	vector < Connection > const& get_connections() const; // connections getter
	map<Server*, int> min_dist(); // calculates map of distance from this server to all others
};