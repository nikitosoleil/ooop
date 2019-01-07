#include "server.h"

const int MAX_DISTANCE = 1e9;

int Server::get_id()
{
	return id;
}

void Server::add_program(Program* program)
{
	programs.push_back(program);
	program->set_server(this);
}

void Server::add_connection(Connection connection)
{
	connections.push_back(connection);
}

void Server::set_network(Network *n)
{
	network = n;
}

vector<Program*> const& Server::get_programs() const
{
	return programs;
}

vector<Connection> const& Server::get_connections() const
{
	return connections;
}

map<Server*, int> Server::min_dist()
{
	map<Server*, int> min_dist;
	for (Server* server: network->get_servers())
		min_dist[server] = MAX_DISTANCE;
	min_dist[this] = 0;
	map<Server*, bool> vis;
	for (int i = 0; i<network->get_servers().size(); ++i) // dijkstra
	{
		int cur_min_dist = MAX_DISTANCE-1;
		Server* selected;
		for (Server* candidate: network->get_servers())
			if (!vis[candidate] && min_dist[candidate]<cur_min_dist)
			{
				selected = candidate;
				cur_min_dist = min_dist[candidate];
			}
		vis[selected] = true;
		for (Connection c: selected->get_connections())
			min_dist[c.server] = min(min_dist[c.server], min_dist[selected]+c.speed);
	}
	return min_dist;
}

Server::~Server()
{
	for(Program *program: programs)
		delete program;
}