#ifndef LOGSIMPLE_H
#define LOGSIMPLE_H

#include "entry.h"

class LogSimple: public Entry {
public:
    // explicit
    LogSimple(Entry *parent = 0);
    ~LogSimple(); // destructor
};
#endif // LOGSIMPLE_H
