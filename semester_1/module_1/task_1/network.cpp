#include "network.h"

void Network::add_server(Server* server)
{
	servers.push_back(server);
	server->set_network(this);
}

vector<Server*> const& Network::get_servers() const
{
	return servers;
}

void Network::run(bool verbose)
{
	for (int t = 0; t<duration; ++t)
	{
		if(verbose)
			cout << "Step " << t+1 << endl;
		int timestamp = clock();
		step(verbose);
		while (clock()-timestamp+0.0<step_duration*CLOCKS_PER_SEC);
	}
}

void Network::step(bool verbose)
{
	for (Server* server: servers)
		for (Program* program: server->get_programs())
			program->step(verbose);
}

Network::~Network()
{
	for(Server* server: servers)
		delete server;
}