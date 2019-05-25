#include "program.h"

int Program::get_id()
{
	return id;
}

void Program::set_server(Server *s)
{
	server = s;
}

void Program::print_message(Message *message)
{
	cout << "From program " << message->from->id << " on server " << message->from->server->get_id() << endl;
	cout << "To program " << message->to->id << " on server " << message->to->server->get_id() << endl;
	cout << "Type: " << message->type << ", size: " << message->size << ", eta: " << message->eta << endl;
}


void Program::send(Message *message, bool verbose)
{
	bool ok = false;
	if (message->from == this && !waits)
		for (int type: sends)
			if(message->type == type)
				ok = true;
	if(ok)
	{
		sending.push_back(message);
		waits = will_wait;
		if (verbose)
		{
			cout << "Message sending started" << endl;
			print_message(message);
			if(waits)
				cout << "Program is waiting" << endl;
			cout << endl;
		}
	}
}

void Program::receive(Message *message, bool verbose)
{
	bool ok = false;
	if(message->to == this && message->eta == 0)
		for (int type: receives)
			if(message->type == type)
				ok = true;
	if(ok)
	{
		if (verbose)
		{
			cout << "Message received" << endl;
			print_message(message);
			if(waits)
				cout << "Program is no longer waiting" << endl;
			cout << endl;
		}
		waits = false;
		received.push_back(message);
	}
}

void Program::step(bool verbose)
{
	vector < Message* > new_sending;
	for (Message *message: sending)
	{
		--message->eta;
		if (message->eta == 0)
			message->to->receive(message, verbose);
		else
			new_sending.push_back(message);
	}
	sending = new_sending;

	if (!waits)
	{
		bernoulli_distribution bd(1.0/period);
		if ( (type && elapsed == period) || (!type && bd(dre) ) )
		{
			elapsed = 0;
			Message *message = random_message();
			if(message)
				send(message, verbose);
		}
		++elapsed;
	}
}

Message* Program::random_message()
{
	queue < Server* > que;
	que.push(server);
	map < Server*, bool > vis;
	vector < pair < Program*, int > > possible;
	while(!que.empty()) // bfs
	{
		Server *now = que.front();
		que.pop();
		if(!vis[now])
		{
			vis[now] = true;
			for(Connection c: now->get_connections())
				que.push(c.server);
			if(now!=server)
				for(int i: sends)
					for(Program *to: now->get_programs())
						for(int j: to->receives)
							if(i==j)
								possible.emplace_back(to, i);
		}   // finding all the accessible programs from this one...
	}
	Message* message = nullptr;
	if(!possible.empty())
	{   // ... and then selecting one of them randomly
		uniform_int_distribution<int> uid(0, possible.size()-1);
		pair<Program*, int> tmp = possible[uid(dre)];
		Program* to = tmp.first;
		int type = tmp.second;
		int distance = server->min_dist()[to->server];
		uid = uniform_int_distribution<int>(0, 5);
		int size = uid(dre)+1;
		message = new Message(this, to, type, size, distance*size);
	}
	return message;
}

void Program::print_stats()
{
	cout << "Received: " << received.size() << ", sending: " << sending.size() << endl;
}

Program::~Program()
{
	for(Message *message: received)
		delete message;
	for(Message *message: sending)
		delete message;
}