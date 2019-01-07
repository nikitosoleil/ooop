#pragma once

#include "all.h"
#include "program.h"

class Program;

struct Message
{
	Program *from, *to; // sender and recipient
	int type; // integer type of message
	int size; // message size
	int eta; // estimated time of arrival, size * ( sum of speed on the shortest path between two servers)
	Message(Program *from, Program *to, int type, int size, int eta):
		from(from), to(to), type(type), size(size), eta(eta) {}
};