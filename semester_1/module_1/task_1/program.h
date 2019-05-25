#pragma once

#include <vector>
#include <random>
#include <queue>
#include <map>

#include "all.h"
#include "server.h"
#include "message.h"

using namespace std;

class Program
{
private:
	int id;
	Server *server; // program parent server
	bool type; // way to generate new messages; random - 0, periodic - 1
	int period; // if type is random: 1/probability of message being generated, else: period between two messages
	int elapsed = 0; // if type is periodic - steps since last message was sent
	bool will_wait; // will program wait for message to continue its work after sending one
	bool waits = false; // does program wait for message to continue its work now
	vector < int > sends, receives; // types of messages program can send and receive
	vector < Message* > received; // vector of received messages by this program
	vector < Message* > sending; // vector of messages currently being sent by this program
	default_random_engine dre; // for generating new random message
	void print_message(Message *message); // helper function to print message if verbose
public:
	Program(int id, Server *server, bool type, int period, bool will_wait, vector < int > sends, vector < int > receives):
		id(id), server(server), type(type), period(period), will_wait(will_wait), sends(sends), receives(receives) {}
	~Program();
	int get_id(); // id getter
	void set_server(Server *s); // server setter
	void send(Message* M, bool verbose); // send message
	void receive(Message* M, bool verbose); // receive message
	void step(bool verbose); // one step of simulation
	void print_stats(); // print number of messages received and number of messages currently being sent
	Message* random_message(); // generate new random message
};